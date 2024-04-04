from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('first_name', 'last_name',)

class CustomstaffForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('is_staff',)