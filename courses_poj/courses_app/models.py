from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Course Name should be at least 10 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Description  should be at least 15 characters"
        return errors

class Description(models.Model):
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CourseManager()    # add this line!


class Course(models.Model):
  name = models.CharField(max_length=255)
  description = models.OneToOneField(Description,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CourseManager()    # add this line!

  
class Comment(models.Model):
  content = models.TextField()
  course = models.ForeignKey(Course, related_name='comments',on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

def all_course():
  return Course.objects.all()


def create_description(desc):
    return Description.objects.create(desc=desc)

def create_course(name, description):
    Course.objects.create(
        name=name,
        description=description
    )


def get_data_course(id):
  return Course.objects.get(id=id)

def get_data_description(id):
  return Description.objects.get(id=id)
  
def delete_course(id):
  course=get_data_course(id)
  course.delete()
  
def all_description():
  return Description.objects.all()

def create_comment(content,course):
  Comment.objects.create(content=content,course=course)
  
def all_comments():
  return Comment.objects.all()


