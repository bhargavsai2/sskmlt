from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from authentication.models import PPVProfile

# If you don't do this you cannot use Bootstrap CSS


# class LoginForm(AuthenticationForm):
#         username = forms.CharField(label="Username", max_length=30,
#                                    widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
#         password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


# class CustomUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kargs)
#         self.fields['password2'].label = "Confirm password:"
#         # set the classes for the fields
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = User
#         exclude = ['user_mobile']
#         fields = ("type_employee_type",
#                   "email",
#                   "first_name",
#                   "last_name",
#                   )



# class CustomPasswordRequestForm(forms.Form):
#     Email = forms.CharField(label="Email", max_length=100,
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email','required': 'True'}))


# class CustomPasswordResetForm(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','required': 'True'}))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'confirm_password','required': 'True'}))


class CustomUserChangeForm(forms.Form):
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = PPVProfile
        fields = '__all__'
        exclude = ['is_superuser','is_staff','lockout_account','audit_name','audit_dttm','user_type','password']

    def clean_username(self):
        print("test!!")
        #data = self.cleaned_data['username']
        data = 'testusername'
        return data


# class ProfileForm(forms.ModelForm):

#     error_css_class = 'error'

#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)

#         # set the classes for the fields
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

#         self.fields['user_phone'].label = "Your phone number:"
#         self.fields['user_mobile'].label = "Your mobile number:"
#         self.fields['user_department'].label = "Your department:"
#         self.fields['user_title'].label = "Your title:"
#         # self.fields['user_manager_name'].label = "Your Manager Name"

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user', 'is_validated', 'token_authorized', 'manager_authorized', 'role',
#                    'sudo_rnis', 'ssh_rnis', 'token_requested', 'sudossh_authorized', 'sudossh_processed',
#                    'sudossh_time', 'sudo_ssh_requested', 'ldap_account_location','last_escalation_request_time','ssh_rnis_requested','sudo_rnis_requested']

#         widgets = {
#                 'password': forms.PasswordInput(),
#                 'employee_status': forms.RadioSelect(),
 
#         }

#     # def validate(self):
#     #     # import pdb;pdb.set_trace()

#     def clean_username(self):
#         print("test!!")
#         # data = self.cleaned_data['username']
#         data = 'testusername'
#         return data
