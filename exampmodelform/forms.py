from django.forms import ModelForm
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


# Create the form class.
class ArticleForm(ModelForm):
     class Meta:
         model = Post
         fields = '__all__'


class CrispyPostForm(ArticleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('description', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit','Submit'))