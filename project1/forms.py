
from django import forms

class Addproject(forms.Form):
    Title = forms.CharField(max_length=100, required=True, label='project title')
    Details = forms.CharField(max_length=1000,required=True,label='Details')
    Totaltarget = forms.IntegerField()
    Totaldonations = forms.IntegerField()
    StartDate = forms.DateField()
    EndDate = forms.DateField()
    # Owner = forms.CharField(max_length=50, required=True, label="owner")
    Rate = forms.FloatField()
    # category = forms.CharField(max_length=50)