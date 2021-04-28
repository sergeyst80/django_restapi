from rest_framework import fields, serializers
from .models import *

# class CreatePollSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Poll
#         fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'text', 'question_type', 'answer_variants')


class PollsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPoll
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class HistoryAnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='text', read_only=True)
    
    class Meta:
        model = Answer
        fields = ('question', 'answer')


class HistorySerializer(serializers.ModelSerializer):
    answers = HistoryAnswerSerializer(source='poll_answers', many=True)
    poll = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = UserPoll
        fields = ('pk', 'poll', 'answers')



# class HistorySerializer(serializers.Serializer):
#     pk = serializers.IntegerField(label='pk', read_only=True)
#     poll =  serializers.SlugRelatedField(slug_field='name', read_only=True)
#     answers = serializer.PrimaryKeyRelatedField(queryset=Answer.objects.all().filter(user_poll=))
#     # questions = serializers.RelatedField().IntegerField(label='question', read_only=True)
#     # answers = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
#     # class Meta:
#     #     model = UserPoll
#     #     fields = '__all__'
