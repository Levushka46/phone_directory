from django import forms


class PhoneNumberForm(forms.Form):
    msisdn = forms.CharField(label="Enter MSISDN:")
