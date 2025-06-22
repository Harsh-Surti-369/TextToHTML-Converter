from django.db import models
# from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Editor(models.Model):
    body = CKEditor5Field(blank=True, null=True)
