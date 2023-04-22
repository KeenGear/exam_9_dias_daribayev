from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a text...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('This field is required.')
        elif not hasattr(image, 'read'):
            raise forms.ValidationError('Invalid file format. Only image files are allowed.')
        elif image.size > 4 * 1024 * 1024:
            raise forms.ValidationError('Image file size should not exceed 4 MB.')
        elif not image.content_type.startswith('image/'):
            raise forms.ValidationError('Invalid file format. Only image files are allowed.')
        return image
