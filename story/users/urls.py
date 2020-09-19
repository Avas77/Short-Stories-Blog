from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.register, name = 'register'),
	path("profile",views.profile,name="profile"),
	path("logout",views.logout,name="logout"),
	path("password-update/",views.password_update,name="password-update")

]