from django.db import models
# Create your models here.

# Validation
class ShowManger(models.Manager):
  def basic_validator(self,postData):
    errors={}
    if len(postData['title']) < 2:
        errors['title']='Title should be at least 2 characters'
    if len(postData['network']) < 3:
        errors['network']='Network should be at least 10 characters'
    if 'desc' in postData and postData['desc']:
      if len(postData['desc']) < 10:
          errors['desc']='Description should be at least 10 characters' 
    return errors

#Database
class Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=255)
  release_date = models.DateField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True )
  
  objects = ShowManger()
  
#Function to recall in 
# Get all shows
def all_show():
  return Show.objects.all()

#Create show
def add_show(POST):
  return Show.objects.create(title=POST['title'],
                      network=POST['network'],
                      release_date=POST['release_date'],
                      desc=POST['desc'])
  
# def update_show(id):
#         show=Show.objects.get(id=id)
#         show.title=show['title']
#         show.network=show['network']
#         show.release_date=show['release_date']
#         show.desc=show['desc']
#         show.save() 

def get_show(id):
  return Show.objects.get(id=id)

def remove_show(id):
  remove =get_show(id)
  remove.delete()

