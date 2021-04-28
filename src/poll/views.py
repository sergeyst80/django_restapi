from django.shortcuts import render
from rest_framework import generics, permissions
from poll.serializers import *
from poll.models import *
import datetime


# Create your views here.
class ListPollsView(generics.ListAPIView):
    serializer_class=PollSerializer
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class CreatePollView(generics.CreateAPIView):
    serializer_class=PollSerializer
    permission_classes = (permissions.IsAdminUser,)


class DetailPollView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PollSerializer
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class ListQuestionsView(generics.ListAPIView):
    serializer_class=QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Question.objects.all()

        if pk:
            queryset = queryset.filter(poll=pk)
        
        return queryset


class CreateQuestionView(generics.CreateAPIView):
    serializer_class=QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)


class DetailQuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class ListActivePollsView(generics.ListAPIView):
    serializer_class=PollSerializer
    queryset = Poll.objects.all().filter(end_date__gte=datetime.datetime.now())


class ListPollQuestionsView(generics.ListAPIView):
    serializer_class=UserQuestionSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        poll = Poll.objects.all().filter(pk=pk).first()
        queryset = poll.poll_questions.all()
        return queryset


class CreateUserPollView(generics.CreateAPIView):
    serializer_class = PollsHistorySerializer


class CreateUserAnswerView(generics.CreateAPIView):
    serializer_class = AnswerSerializer


class HistoryUserPollsView(generics.ListAPIView):
    serializer_class = HistorySerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('user')
        queryset = UserPoll.objects.all().filter(user_id=user_id)
        return queryset
