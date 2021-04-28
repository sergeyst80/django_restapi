from django.shortcuts import render
from rest_framework import generics
from poll.serializers import *
from poll.models import Poll
import datetime

# Create your views here.
class CreatePollView(generics.CreateAPIView):
    serializer_class=CreatePollSerializer


class ListActivePollsView(generics.ListAPIView):
    serializer_class=ListActivePollsSerializer
    queryset = Poll.objects.all().filter(end_date__gte=datetime.datetime.now())
    print(queryset.query)