from django import forms
from django.forms import ModelForm
from .models import Feedback
    
   

class FeedbackForm(forms.Form) :
    email=forms.EmailField(label="Enter Your Email",max_length=100,required=True)
    name=forms.CharField(label="Enter Your Name", max_length=200, required=True)
    feedback=forms.CharField(label="Your Feedback", widget=forms.Textarea , max_length=100, required=True)


    

class FeedbackForm(ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'