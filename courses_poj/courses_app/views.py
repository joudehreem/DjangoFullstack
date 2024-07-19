from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

from django.conf import settings

# from django.http import Http404

# Create your views here.

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '505.html', status=500)
  
#render the index.html and recall all course from models
def index(request):
  context={
    'courses':all_course(),
    'description':all_description()
  }
  return render(request,'index.html',context)

#Handel post request from form course
def add_courses(request):
  if request.method == 'POST':
    errors = Course.objects.basic_validator(request.POST)
          # check if the errors dictionary has anything in it
    if len(errors) > 0:
      # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
      for key, value in errors.items():
          messages.error(request, value)
      # redirect the user back to the form to fix the errors
      return redirect('/')
    else:
        name = request.POST['name']
        desc = request.POST['desc']
        description=create_description(desc)
        create_course(name, description)
        
  return redirect('/')
    
#render to the destroy page
def review_course(request,id):
  context={
    'course':get_data_course(id),
    'description':get_data_description(id)
  }
  return render(request,'delete.html',context)
# remove the course and redirect to the main page
def remove_course(request):
  if request.method =='POST':
        delete_course(request.POST['course_id'])
        return redirect('/')

        return render(request,'delete.html',context)    
  
def comment(request,id):
  context={
  'comments':all_comments(),
  'course':get_data_course(id)
  }
  
  return render(request,'comment.html',context)

def add_comment(request,id):
  if request.method =='POST':
    course=get_data_course(id)
    content=request.POST['comment']
    create_comment(content,course)
    return redirect(f'/course/{course.id}/comment')
  # else:
  #   return render(request, 'comment.html')

