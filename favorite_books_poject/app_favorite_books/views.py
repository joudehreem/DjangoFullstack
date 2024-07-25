from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'login&reg.html')

def books(request):
  if 'user_id' not in request.session:
      return redirect('/')
  else:
      context = {
          'user': get_user(request.session),
          'books': get_books(),
          # 'upload_by':upload_by()
      }
  return render(request, 'add_book.html',context)


#handel request post to registration, and pass data to the method to it there are an error shown a msg and redirect to registration page, else create the data and go to the success
def registration(request):
  if request.method == 'POST':
      errors = User.objects.basic_register(request.POST)
      if len(errors) > 0:
          for key, value in errors.items():   
              messages.error(request, value)    
          return redirect('/')
      else:
          user = create_user(request.POST)
          request.session['user_id'] = user.id
          messages.success(request, "Successfully Registered")
          return redirect('/books')
  return redirect('/books')


#handel request post to login by user email, and pass data to the method if there are an error display a msg and redirect to main page, else create the data and go to the success page
def login(request):
  if request.method == 'POST':
        errors = User.objects.basic_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = check_email(request.POST) 
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/books')
        # user = User.objects.get(email=request.POST['email'])
        # request.session['user_id'] = user.id
        # messages.success(request, "Successfully logged in")
        # return redirect('/books')
  else:
        return redirect('/')

# clear the session of user to logout
def logout(request):
    if request.method=='POST':
        request.session.clear()
        return redirect('/')

###################

def add_book(request):
  if request.method== 'POST':
      errors = Book.objects.basic_add_book(request.POST)
      if len(errors) > 0:
          for key, value in errors.items():   
              messages.error(request, value)    
          return redirect('/books')
      else:
        book=create_book(request.POST,request.session)
        like_book(request.session,book.id )
        return redirect(f'/books/{book.id}')
  else:
    return render(request,'add_book.html')


# edit information of the book

def detail_book(request,id):
  context={
    'book':book(id),
    'user': get_user(request.session),
  }    
  return render(request,'detail_book.html',context)

def form_edit_book(request,id):
  context={
    'book':book(id),
    'user': get_user(request.session)
  }    
  return render(request,'edit_book.html',context)

def edit_book(request,id):
  if request.method =='POST':
    update_book(request.POST,id)
    return redirect(f'/books/{id}')
  # return render(request,'detail_book.html',context)

# remove book from data
def remove_book(request):
  if request.method =='POST':
    delete_book(request.POST)
    return redirect('/books')
  


def add_favorite(request, id):
    if request.method == 'POST':
        like_book(request.session, id)
        messages.success(request, "Book added to favorites!")
    return redirect('/books')



def remove_favorite(request, id):
    if request.method == 'POST':
        unlike(request.session, id)
        messages.success(request, "Book removed from favorites!")
        return redirect('/books')