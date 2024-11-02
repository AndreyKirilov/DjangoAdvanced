from django.contrib.auth.views import LogoutView
from django.urls import path
from TaskApp.todo_app.views import (dashboard, HomePage, book_view, login_user_view, logout_view,
                                    TaskView, CreateTaskView, TaskUpdateView, DeleteTaskView, BookListView, BookCreateView,
                                    create_user_view, UserDetailsView)

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('dashboard/', dashboard, name='dash'),
    path('register/', create_user_view, name='user-create'),
    path('login/', login_user_view, name='user-login'),
    path('logout/', logout_view, name='user-logout'),
    path('book_app/', book_view, name='book_app'),
    path('tasks-list/', TaskView.as_view(), name='tasks-list'),
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
    path('books-list/', BookListView.as_view(), name='books-list'),
    path('add-book/', BookCreateView.as_view(), name='create-book'),
    path('profile-details/<int:pk>/', UserDetailsView.as_view(), name='profile-details'),
]


#form_view