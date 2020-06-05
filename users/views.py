from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm 
 #from django.db.models import Q
from marandmor.models import Post

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account Has being created, you can log in directly.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html', {'form':form})
 
@login_required
def profile(request):
	return render(request, 'users/profile.html')

def search(request):

	if request.method == 'GET':
		query = request.GET.get('q')
		submitbutton = request.GET.get('submit')

#		lookups = Q(Item__contains=query)| Q(Created_By__contains=query)
		 
		if query is not None:

		    
			
			posts = Post.objects.filter(Item__icontains=query)

			context = {'posts': posts, 'submitbutton': submitbutton}
			 
			return render(request, 'users/search.html', context)

		else:

			return render(request, 'users/search.html')


	else:
		return render(request, 'users/search.html')
				
