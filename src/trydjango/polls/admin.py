from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']   # Adds a filter sidebar
    search_fields = ['question_text']  # Adds search box


admin.site.register(Question, QuestionAdmin)
