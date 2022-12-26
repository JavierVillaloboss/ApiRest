from django import forms
from Autosapp.models import Autos,Repuesto,Tienda

class Registroform(forms.ModelForm):
    class Meta:
        model = Autos
        fields = '__all__'

class RegistroR(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'

class RegistroT(forms.ModelForm):
    def clean_correo(self):
        inputCorreo = self.cleaned_data['correo']
        if inputCorreo.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return inputCorreo
    class Meta:
        model = Tienda
        fields = '__all__'


