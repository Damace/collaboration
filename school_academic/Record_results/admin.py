# systemUsers/admin.py
from django.contrib import admin
from django import forms
from .models import EnterResults, Stream

class EnterResultsForm(forms.ModelForm):
    class Meta:
        model = EnterResults
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'class_name' in self.data:
            try:
                class_id = int(self.data.get('class_name'))
                self.fields['stream'].queryset = Stream.objects.filter(class_name_id=class_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['stream'].queryset = self.instance.class_name.stream_set.all()

class EnterResultsAdmin(admin.ModelAdmin):
    form = EnterResultsForm
    list_display = ('academic_year', 'term', 'subject', 'exam_category', 'class_name', 'stream')
    search_fields = ('academic_year__name', 'term__name', 'subject__code', 'exam_category__name', 'class_name__name', 'stream__name')
    list_filter = ('academic_year', 'term', 'subject', 'exam_category', 'class_name', 'stream')

admin.site.register(EnterResults, EnterResultsAdmin)
