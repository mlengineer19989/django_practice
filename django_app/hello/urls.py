from django.urls import path
from . import views
from .views import FriendList, FriendDetail

urlpatterns = [
    path(r"", views.index, name="index"), 
    path(r"create", views.create, name="create"), 
    path(r"edit/<int:num>", views.edit, name="edit"),
    path(r"delete/<int:num>", views.delete, name="delete"), 
    path(r"list", FriendList.as_view()), 
    path(r"detail/<int:pk>", FriendDetail.as_view()), 
    path(r"find", views.find, name="find"), 
    #path("next", views.next, name="next"),
    #path("form", views.form, name="form"),
]