from django import forms


class StudentForm(forms.Form):
    firstname = forms.CharField(min_length=3, max_length=20, label='First Name', required=True)
    lastname = forms.CharField(min_length=3, max_length=20, label='Last Name', required=True)