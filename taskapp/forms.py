from django import forms

from .models import ToDoList

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = [
            'user',
            'name',
            'priority'
        ]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        print(name)
        if len(name) > 250:
            raise forms.ValidationError('Content Is too long, Max char is 10')
        return name

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        name = data.get('name', None)
        if name == "":
            name = None
        if name is None:
            raise forms.ValidationError('Name is required.')
        return super().clean(*args, **kwargs)



