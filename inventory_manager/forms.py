
from django import forms
from django.utils.translation import gettext_lazy as _
from inventory_manager.models import SupportTicket
from inventory_manager.views import Book, Author


class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        help_texts = {
            'first_name': _('Required'),
            'last_name': _('Required'),
        }


class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    

class ContactForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = '__all__'

        help_texts = {
            'email': _('Required'),
            'topic': _('Required'),
            'message': _('Required')
        }