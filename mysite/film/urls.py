from django.urls import path,include
from . import views
from film.views import detail
urlpatterns = [
 path('',views.indexx),
 path('/list',views.indexx),
path('<int:myid>',detail),
 ]  