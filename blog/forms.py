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
        self.fields['body'].widget.attrs.update({'class': 'django_ckeditor_6'})  
        self.fields["body"].required = False  



# class OldEnquiryForm(forms.ModelForm):
#     def __init__(self,*args, user=None, **kwargs):
#         super(oldenquiryForm, self).__init__(*args, **kwargs)
#         if user is not None:
#             self.fields['created_by'].queryset = emp.objects.filter(branch=user.admin.branch_name)

#     class Meta:
#         model=enquiry
#         fields=['product','type','created_at']
#         widgets={
#             'created_at':forms.DateInput(attrs={'type':'date'}),
#         }



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
        # if user is not None:
        #     self.fields['parent'].queryset = Category.objects.filter(author=user)

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