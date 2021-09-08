from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Home)


class Inlines(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name']

    inlines = [Inlines]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['answer_text', 'is_correct', 'question_text', 'question']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [ 'question_text', 'category', 'points', 'created', 'updated', 'id',]

    inlines = [AnswerInline]


@admin.register(Attemper)
class AttemperAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['user', 'score', 'completed']
