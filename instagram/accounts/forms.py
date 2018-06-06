from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#create forms here
class RegistrationForm(UserCreationForm):     #create registration form to inherit from usercreationform
    email = forms.EmailField(required=True)   #make email required

    #define the form fields
    class Meta:
        model = User    #define model to inherit fields from
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

        #define method to save form data
        def save(self, commit = True):
            user = super(RegistrationForm,self).save(commit=False)   #hold off saving this data to the database until we validate
            user = first_name = self.cleaned_data['first_name']      #save cleaned_data
            user = last_name = self.cleaned_data['last_name']
            user = email = self.cleaned_data['email']

            if commit():
                user.save()

            return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )