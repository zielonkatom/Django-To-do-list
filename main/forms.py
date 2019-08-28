from django import forms
from .models import ThingToDo

class ThingToDoForm(forms.ModelForm):
    activity_text = forms.CharField(initial="",required=True, label="Got anything to do?", max_length=500)


    class Meta:
        model = ThingToDo
        fields = ('activity_text',)
