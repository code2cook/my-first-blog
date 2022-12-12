from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    
    
    # post/ means that the URL should begin with the word post followed by a /. So far so good.
    # <int:pk> – this part is trickier. It means that Django expects an integer value and will transfer it to a view as a variable called pk.
    # /  then we need a / again before finishing the URL.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]