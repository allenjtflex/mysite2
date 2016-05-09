from django import forms

from .models import Document


class DocumentForm( forms.ModelForm ):
    class Meta:
        model = Document
        fields = [
            'apply_date' ,
            'category' ,
            'apply_department' ,
            'apply_user' ,
            'ext_number' ,
            'request_level' ,
            'request_descript'
        ]
