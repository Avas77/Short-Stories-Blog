from django.urls import path
from . import views
from .views import WritingListView,WritingDetailView,WritingCreateView,WritingUpdateView,WritingDeleteView,EventsCreateView,UserWritingListView


urlpatterns = [
	path('', views.writings, name = 'writings'),
	path("writing/<int:pk>/",WritingDetailView.as_view(),name="writing-detail"),
	path("user/<str:username>/",UserWritingListView.as_view(),name="user-posts"),
	path("writing/new/",WritingCreateView.as_view(),name="writing-create"),
	path("writing/events/new",EventsCreateView.as_view(),name="event-create"),
	path("writing/<int:pk>/update/",WritingUpdateView.as_view(),name="writing-update"),
	path("writing/<int:pk>/delete/",WritingDeleteView.as_view(),name="writing-delete"),
]