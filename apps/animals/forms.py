from django import forms


from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'edad', 'descripcion', 'imagen']
        # fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        # labels = {
        #     'nombre': 'Nombre del animal',
        # }