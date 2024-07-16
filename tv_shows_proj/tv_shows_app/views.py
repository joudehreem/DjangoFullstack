from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages



# Create your views here.

#redirect '/' to page '/show'
def redirect_shows(request):
  return redirect('/shows')

def index(request):
  context={
    'shows':all_show(),
    
  }
  return render(request,'index_shows.html',context)

# def new_show(request):
#   return render(request,'new_show.html')

def create_show(request):
    if request.method == 'POST':
      
      errors = Show.objects.basic_validator(request.POST)
          # check if the errors dictionary has anything in it
      if len(errors) > 0:
          # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
          for key, value in errors.items():
            messages.error(request, value)
          # redirect the user back to the form to fix the errors
          return render(request, 'new_show.html',{'form_data': request.POST})
      else:      
      
        # title=request.POST['title']
        # network=request.POST['network']
        # release_date=request.POST['release_date']
        # desc=request.POST['desc']  
        show=add_show(request.POST)
        return redirect(f'/shows/{show.id}')
    return render(request, 'new_show.html')
    
def edit(request,id):
  context = {
      'show' : get_show(id) 
  }
  return render(request,'edit_show.html',context)

def update_show(request,id):
  if request.method=='POST':
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:

        for key, value in errors.items():
          messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{id}/edit')
    else:   
        show=Show.objects.get(id=id)
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.desc=request.POST['desc']
        show.save() 
        return redirect(f'/shows/{show.id}')

def tv_show(request,id):
  context={
    'show':get_show(id)
  }
  return render(request,'tv_show.html',context)

def destroy(request,id):
  remove_show(id)
  return redirect('/')