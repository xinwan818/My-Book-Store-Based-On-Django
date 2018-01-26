from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required = False)
    message = forms.CharField(widget = forms.Textarea)
    
    def limit(self):
        massage = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough !")
        return message
