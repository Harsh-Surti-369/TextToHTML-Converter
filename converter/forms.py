from django.forms import ModelForm, CharField
from django_ckeditor_5.widgets import CKEditor5Widget
# local
from .models import Editor


class EditorForm(ModelForm):
    body = CKEditor5Widget(config_name='default')
    class Meta:
        model = Editor
        fields = '__all__'
