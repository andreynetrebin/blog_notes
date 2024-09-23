from django import forms
from .models import Post, Category


class PostCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """
    class Meta:

        model = Post
        fields = ('title', 'category', 'body', 'image', 'status')


    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
        self.fields['body'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['body'].required = False


class CategoryCreateForm(forms.ModelForm):
    """
    Форма добавления категории на сайте
    """
    class Meta:

        model = Category
        fields = ('title', 'parent')


    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })




class PostUpdateForm(PostCreateForm):
    """
    Форма обновления статьи на сайте
    """
    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields + ('publish',)

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

        # self.fields['publish'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['body'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['body'].required = False