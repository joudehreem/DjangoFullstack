from django.db import models
import re
import bcrypt
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        # if len(postData['dob']) < 10:
        #   errors["dob"] = "Blog description should be at least 10 characters"
        if len(postData['password']) < 2:
          errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_pw']:
          errors["confirm_pw"] = "Passwords are not match "
        return errors
    # def validate_login(request):
    #   user = User.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here?
    #   if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
    #       print("password match")
    #   else:
    #       print("failed password")

class User(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  # dob = models.DateField()
  email = models.CharField(max_length=225)
  password = models.CharField(max_length=50)
  confirm_pw=models.CharField(max_length=50)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()


def create_user(POST):
  password = POST['password']
  return User.objects.create(
    first_name=POST['first_name'],
    last_name =POST['last_name'],
    email=POST['email'],
    password= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
    # confirm_pw=POST['password']
    )

# def get_user(session):
#   return User.objects.get(session['user_id'])

def login(POST):
  user_login = User.objects.filter(email=POST['email']) 
  return user_login