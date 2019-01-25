from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
	class Meta:
		model=Answer
		fields=['ans',]
		widgets={
			'ans':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})

		}