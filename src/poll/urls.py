from django.urls import path
from . import views


app_name = 'poll'

urlpatterns = [
    path('admin/list/', views.ListPollsView.as_view()),
    path('admin/create/', views.CreatePollView.as_view()),
    path('admin/detail/<int:pk>/', views.DetailPollView.as_view()),
    path('admin/question/list/<int:pk>/', views.ListQuestionsView.as_view()),
    path('admin/question/create/', views.CreateQuestionView.as_view()),
    path('admin/question/detail/<int:pk>/', views.DetailQuestionView.as_view()),
    path('user/list/', views.ListActivePollsView.as_view()),
    path('user/question/list/<int:pk>/', views.ListPollQuestionsView.as_view()),
    path('user/start/', views.CreateUserPollView.as_view()),
    path('user/answer/', views.CreateUserAnswerView.as_view()),
    path('user/history/<int:user>/', views.HistoryUserPollsView.as_view()),
]
