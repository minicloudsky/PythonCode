from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # fields 用于指定表单的字段，这些指定的字段在模板中
        # 会被渲染成表单控件（即一些 <input> 等表单控件）
        model = User
        fields = ("username","email")