from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from writings.models import Writing
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.base import ContextMixin
def writings(request):
	writings = Writing.objects.order_by('-write_date')
	paginator = Paginator(writings, 4)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = {
		'writings': paged_listings
	}
	
	return render(request, 'writings/writings.html', context)

class WritingListView(ListView):
	model = Writing
	template_name='writings/writings.html'
	context_object_name='writings'
	ordering=['-write_date']
	
class UserWritingListView(ListView):
	model = Writing
	template_name='writings/user_posts.html'
	context_object_name='writings'
	
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Writing.objects.filter(author=user).order_by('-write_date')

class WritingDetailView(DetailView):
	model = Writing

class WritingCreateView(LoginRequiredMixin,CreateView):
	model = Writing
	fields=['title','short_description','description','categories']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class EventsCreateView(LoginRequiredMixin,CreateView):
	model = Writing
	template_name='pages/events.html'
	fields=['title','short_description','description','categories']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class WritingUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Writing
	fields=['title','short_description','description','categories']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		writing=self.get_object()
		if self.request.user == writing.author:
			return True
		return False

class WritingDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Writing
	success_url=''

	def test_func(self):
		writing=self.get_object()
		if self.request.user == writing.author:
			return True
		return False