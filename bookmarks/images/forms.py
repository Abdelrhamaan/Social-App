from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms
from .models import Image
import requests

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'url']
        widgets = {
            'url': forms.HiddenInput
        }
        
    """ method to check extension of image from url """
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['png', 'jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not  \
                                        match valid image extensions.')
            
        return url 
        
        
        
        
    def save(self, force_insert=False,
                    force_update=True,
                    commit=True):
        
        image = super().save(commit=False)
        url = self.cleaned_data['url']
        extension = url.rsplit('.', 1)[1].lower()
        name = slugify(image.title)
        image_name = f'{name}.{extension}'
        response = requests.get(url)
        # sava = false ---> To Prevent saving img in db
        #  content file ---> to save img in media dir 
        image.image.save(image_name, 
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image 