from django import forms
from biebfeed.models import TwitterTarget

class FriendForm(forms.ModelForm):

    class Meta:
        model = TwitterTarget
        fields = ('user', 'target_username',)