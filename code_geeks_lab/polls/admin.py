from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'Code Geeks Lab'
admin.site.site_title  = 'Code Geeks Lab Admin'
admin.site.index_title = 'Welcome to Code Geeks Lab Admin'

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QuestionAdmin)