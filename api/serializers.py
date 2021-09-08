from rest_framework import serializers
from main.models import Home, Question, Attemper, Category, Answer


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'get_quest']



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'question_text', 'category', 'points']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'question', 'is_correct']


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attemper
        fields = '__all__'

