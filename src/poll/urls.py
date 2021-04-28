from django.urls import path
from . import views


app_name = 'poll'

urlpatterns = [
    path('create-poll/', views.CreatePollView.as_view()),
    path('list-active-polls/', views.ListActivePollsView.as_view()),
]
