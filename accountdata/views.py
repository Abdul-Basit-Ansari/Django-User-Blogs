from django.contrib import messages 
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from . models import Blog,Blogcomment


# Create your views here.





def signin(request):

	if request.method=="POST":
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		uname = request.POST.get('uname')
		email = request.POST.get('email')
		pass1 = request.POST.get('pass1')
		pass2 = request.POST.get('pass2')
		if not fname.isalpha():
			messages.error(request,"Please Remove Symbles Or Numbers Of First Name")
			dic={}
			# return redirect('signin',dic)

		if not lname.isalpha():
			messages.error(request,"Please Remove Symbles Or Numbers Of Last Name")
			dic={}
			# return redirect('signin',dic)

		if not uname.isalnum():
			messages.error(request,"User Name Is Must Be Alpha Numaric")
			dic={}
			# return redirect('signin',dic)

		if len(uname) < 8 :
			messages.error(request,"User Name Is Must Be  8 Character")
			dic={}
			# return redirect('signin',dic)  

		if len(pass1) < 8:
			messages.error(request,"Password IsTo Small Please Create 8 Character Password")
			dic={}
			# return redirect('signin',dic)


		if pass1 != pass2:
			messages.error(request,"Passwords Is Not Same")
			dic={}
			# return redirect('signin',dic)


		user = 	User.objects.create_user(uname,email,pass1)
		user.save()
		user=authenticate(username= uname, password= pass1)
		if user is not None:
			login(request, user)
			messages.success(request,"You Logedin You Account Is Created")
			return redirect('blogs')
		# login(request,user)
		messages.success(request,"You Account Is Created")
		dic={}
		# return redirect('signin',dic)

	
	dic={}
	return render(request,'signin.html',dic)



def userlogin(request):
	user = request.user
	if user.is_authenticated:
		return redirect('blogs')
	else:
		if request.method == "POST":
			# Get the post parameters
			loginusername = request.POST['loginuname']
			loginpassword = request.POST['loginpass']

			user=authenticate(username= loginusername, password= loginpassword)
			if user is not None:
				login(request, user)
				messages.success(request, "Successfully Logged In")
				return redirect('blogs')

			else:
				messages.error(request, "Invalid credentials! Please try again")
				# return redirect("home")

				return render(request,'login.html')
		return render(request,'login.html')




def userlogout(request):
	logout(request)
	messages.success(request, "Successfully logged out")

	return redirect('blogs')



def addblog(request):
	user = request.user
	if user.is_authenticated:
		if request.method == "POST":
			title = request.POST.get('blogtitle')
			bwritter = f"{user.first_name} {user.last_name}"  
			text = request.POST.get('blogcontent')

			blog = Blog(title=title,writter=bwritter,slug=title,content=text)
			blog.save()
			messages.success(request,"YOUR BLOG HAS BEEN SAVE")

			return redirect('blogs')



		return render(request,'addblog.html')
	return redirect('blogs')



def blogs(request):

	b = Blog.objects.all()
	dic={'blog':b}

	return render(request,'index.html',dic)

def blogpost(request , slug):

	# b = Blog.objects.all()
	blog=Blog.objects.filter(slug=slug).first()
	comments= Blogcomment.objects.filter(blog=blog,parent=None)
	# replies= Blogcomment.objects.filter(blog=blog).exclude(parent=None)
	# replydic={}
	# for reply in replies:
	# 	if reply.parent.sno not in replydic.keys():
	# 		replydic[reply.parent.sno]=[reply]
	# 	else:
	# 		replydic[reply.parent.sno].append(reply)

	# for comment in comments:
	# 	getval = get_val(replydic,comment.sno)
		
	dic={"blog":blog,'comments':comments,'user': request.user}

	return render(request,'blogpost.html',dic)

def blogcomment(request):
	if request.method == "POST":
		comment=request.POST.get('comment')
		user=request.user	
		blogsno =request.POST.get('blogsno')
		blog= Blog.objects.get(sno=blogsno)
		parentsno=request.POST.get('commentsno')
		if parentsno==None:
			comment=Blogcomment(comment= comment, user=user, blog=blog)
			comment.save()
			messages.success(request, "Your comment has been posted successfully")
		else:
			parent= Blogcomment.objects.get(sno=parentsno)
			comment=Blogcomment(comment= comment, user=user, blog=blog,parent=parent)
			comment.save()
			messages.success(request, "Your replay has been posted successfully")
			

	
	return redirect(f"blog/{blog.slug}")