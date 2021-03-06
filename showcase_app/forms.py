from django import forms
from showcase_app.models import UserProfile
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['message'].label = "Message:"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['bio' ]
