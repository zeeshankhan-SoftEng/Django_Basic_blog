"""blogWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import path
from home.views import HomeView, CreateBlogView, DetailsBlogView, DeleteBlogView,  UpdateBlogView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('details/<uuid:id>/', DetailsBlogView.as_view(), name='details_blog'),
    path('delete/<uuid:id>/', DeleteBlogView.as_view(), name='delete_blog'),
    path('update/<uuid:id>/', UpdateBlogView.as_view(), name='update_blog'),
]


