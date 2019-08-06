from django import forms
from .models import internshipPost

class internshipPostForm(forms.ModelForm):
    class Meta:
        model = internshipPost
        fields=['company_name','description']
