from django import forms
from .models import Question, Choise

class QuestionForm(forms.Form):
    question_id = forms.IntegerField()

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data

class ChoiseModelForm(forms.ModelForm):
    class Meta:
        model = Choise
        fields = ['question', 'choise_text']