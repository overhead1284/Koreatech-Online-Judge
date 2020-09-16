from django.contrib import admin
from django import forms
from .models import Problem, Testcase, Submit, Article, Comment
#from ckeditor.widgets import CKEditorWidget


class TestcaseAdmin(admin.StackedInline):
    model = Testcase


class ProblemAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [TestcaseAdmin]

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    #content = forms.CharField(widget=CKEditorWidget())

class TestcaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Testcase, TestcaseAdmin)
admin.site.register(Submit)
admin.site.register(Comment)
