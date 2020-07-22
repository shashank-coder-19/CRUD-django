from django.urls import path, include
from basic_app import views

app_name='basic_app'
# here i am writing url path for list view , detail view , create view, update view , delete view
urlpatterns=[
     path('',views.SchoolLIstView.as_view(),name='list'),
     path('<int:pk>/',views.SchoolDetailView.as_view(),name="detail"),
     path('create/',views.SchoolCreateView.as_view(),name='create'),
     path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name="update"),
     path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name="delete"),


]
