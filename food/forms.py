from django import forms
from .models import Food


class AddFood(forms.ModelForm):
    class Meta:
        model = Food
        fields = (
            'name', 'calories', 'serving_size_g', 'fat_total_g', 'protein_g', 'carbohydrates_total_g', 'created_at')
        exclude = ('user',)


class EditFood(forms.ModelForm):
    name = forms.CharField(disabled=True)

    def __init__(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        super(EditFood, self).__init__(*args, **kwargs)
        self.fields['name'].disabled = True

        if data:
            for index in range(len(data)):
                self.fields['name'].widget.attrs['value'] = data[index]['name']
                self.fields['serving_size_g'].widget.attrs['value'] = data[index]['serving_size_g']

    class Meta:
        model = Food
        fields = ('name', 'serving_size_g')

    def default_values(data):
        for values in data:
            name = forms.CharField(default=values['name'], disabled=True)
            serving_size_g = forms.CharField(default=values['serving_size_g'], disabled=True)
