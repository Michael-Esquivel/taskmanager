from django.forms import ModelForm
from .models import taskM

class taskF(ModelForm):
    class Meta:
        model = taskM
        fields = ['title', 'description', 'important']