from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView,  DetailView, DeleteView
from . models import Post



def home(request):
	context = {
	'posts':Post.objects.all()
	}

	return render(request, 'marandmor/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = "marandmor/home.html"
	context_object_name = 'posts'
	ordering = ['-Date_Posted']

class PostDetailView(DetailView):
	model = Post

 
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['Item','Price', 'Specification']
	
	def form_valid(self, form):
		form.instance.Created_By = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['Item','Price', 'Specification']
	
	def form_valid(self, form):
		form.instance.Modified_By = self.request.user
		form.instance.Modified_Date = timezone.now()
		return super().form_valid(form)

	
#	def test_func(self):
#		post = self.get_object()
#		if self.request.user == post.Created_By:
#			return True
#		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

	model = Post
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Created_By:
			return True
		return False
		    	

			

		
def specification(request):
	return render( request, 'marandmor/specification.html')


