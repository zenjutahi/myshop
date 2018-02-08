from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile Number'}))
	payment_code = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Payment Code'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'mobile_no',
					'payment_code', 'city']