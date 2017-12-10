from django.conf.urls import url
from bms import views

urlpatterns = [

    url(r'^indexAuthor/', views.indexAutor),
    url(r'^addAuthor/', views.addAuthor),
    url(r'^indexPublish/', views.indexPublish),
    url(r'^addPublish/', views.addPublish),
    url(r'^indexBook/', views.indexBook),
    url(r'^addBook/', views.addBook),
    url(r'^delBook/', views.delBook),
    url(r'^delPublish/', views.delPublish),
    url(r'^delAuthor/', views.delAuthor),
    url(r'^editPublish/', views.editPublish),
    url(r'^editBook/', views.editBook),
    url(r'^editAuthor/', views.editAuthor),
]
