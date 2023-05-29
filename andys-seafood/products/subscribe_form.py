from django.forms import ModelForm
from products.models import Subscription
from django import forms


class SubscribeForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name",
                                                         'style': 'width: 300px;',
                                                         'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter your email",
                                                                   'style': 'width: 300px;',
                                                                   'class': 'form-control'}))
    class Meta:
        model = Subscription
        fields = "__all__"
