from django import forms

class UpdateUserForm(forms.Form):
    GENDER_CHOICES = [('Male', 'Female', 'Company')]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    username = forms.CharField(label='Username', max_length=50)
    email_address = forms.CharField(label='Email Address', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    phone_number = forms.CharField(label='Phone Number', max_length=30)

class UpdatePasswordForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput())
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput())

class UpdateProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField()
