from django.db import models
import re
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
# Create your models here. 

class UserManager(models.Manager): # validation for login and registration
    def basic_register(self, postData): # function for registration 
        errors = {}
        if len(postData['first_name']) < 2:# validated first name
            errors["first_name"] = "First Name should be at least 2 characters"## as list ""if satament
            # errors["first_name"].append=('')
        if len(postData['last_name']) < 2:# validated last name
            errors["last_name"] = "Last Name should be at least 2 characters"
        # validated dob to required in database and age grater than 13"
        #validated format of mail and unique email used
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):             
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email_used'] = "Email already in use!"
        # validated pass to be greater than 8 char and match with confirm pass 
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_pw']:
            errors["confirm_pw"] = "Passwords are not match "
        return errors
    
    def basic_login(self, postData):# function for login 
            errors = {}
            try:
                user = User.objects.get(email=postData['email'])
            except ObjectDoesNotExist:
                errors['email'] = "Email not found."
                return errors
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Invalid password."
            return errors
class BookManager(models.Manager): # validation for login and registration
    def basic_add_book(self, postData): # function for registration 
        errors = {}
        if len(postData['title']) < 2:# validated first name
            errors["title"] = "Title should be at least 2 characters"## as list ""if satament
        if len(postData['desc']) < 5:# validated Description
            errors["desc"] = "Description should be at least 5 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=225)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User,related_name='books_uploaded',on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User,related_name='liked_books')
    objects = BookManager()



# create user 
def create_user(POST):
    password = POST['password']
    return User.objects.create(
        first_name=POST['first_name'],
        last_name =POST['last_name'],
        email=POST['email'],
        password= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
        )
# get user to session
def get_user(session):
    return User.objects.get(id=session['user_id'])


#check user mail
def check_email(POST):
    return User.objects.filter(email=POST['email'])
# create book form
def create_book(POST,session):
    return Book.objects.create(
        title=POST['title'],
        desc =POST['desc'],
        uploaded_by=get_user(session),
        )
    
# all Books

def get_books():
    return Book.objects.all()

def book(id):
    return Book.objects.get(id=id)
def user(id):
    return User.objects.get(id=id)
def update_book(POST,id):
    # book_id=POST['id']
    # title=POST['title']
    # desc=POST['desc']
    book=Book.objects.get(id=id)
    book.title=POST['title']
    book.desc=POST['desc']
    book.save()

def delete_book(POST):
    book_remove=book(POST['book_id'])
    book_remove.delete()


def like_book(session,id):
    user = get_user(session)
    book = Book.objects.get(id=id)
    book.users_who_like.add(user)
    


def unlike(session,id):
    user = get_user(session)
    book = Book.objects.get(id=id)
    book.users_who_like.remove(user)
    