from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    second_name = forms.CharField(label='Second name', max_length=100)

class NameAndFile(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #second_name = forms.CharField(label='Second name', max_length=100)
    products_file = forms.FileField()
    tickets_file = forms.FileField()
