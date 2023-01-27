from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        def save(self, commit=True):
            user = super(ContactForm, self).save(commit=False)

            if commit:
                user.save()
            return user
