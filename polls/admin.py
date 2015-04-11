from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [('Text', {'fields':['question_text']}), 
		('Date information', {'fields':['pub_date'], 'classes':['collapse']}),]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# Register your models here.
