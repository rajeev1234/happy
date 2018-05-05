from django import forms
from djng.forms import NgFormBaseMixin

from .models import Newsletter




class JoinForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ["email"]