from django.shortcuts import render
from writings.models import Writing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.models import User
from users.models import Profile
def home(request):
	return render(request, 'pages/home.html')

def about(request):
	return render(request, 'pages/about.html');

def search(request):
	writings = Writing.objects.order_by('-write_date')
	profile=Profile.objects.all()

	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			writings = writings.filter(Q(title__icontains = keyword) | 
			Q(description__icontains = keyword) | 
			Q(categories__icontains = keyword))

	if 'writer' in request.GET:
		writer = request.GET['writer']
		if writer:
			writings = writings.filter(author__first_name__icontains = writer)

	context = {
		'writings': writings
	}

	return render(request, 'pages/search.html', context)

def delete(request, writing_id):
	writings = get_object_or_404(Writing, pk = writing_id)
	writings.delete()
	return redirect('index')