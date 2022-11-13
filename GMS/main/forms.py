# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . import models

# Enquiry
class EnquiryForm(forms.ModelForm):
	class Meta:
		model=models.Enquiry
		fields=('full_name','email','detail')

# Registration
class SignUp(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')

#Profile
class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')

# Trainer Login
class TrainerLoginForm(forms.ModelForm):
	class Meta:
		model=models.Trainer
		fields=('username','pwd')

# Trainer Profile
class TrainerProfileForm(forms.ModelForm):
	class Meta:
		model=models.Trainer
		fields=('full_name','mobile','address','detail','img')

# Trainer Change Password
class TrainerChangePassword(forms.Form):
	new_password=forms.CharField(max_length=50,required=True)

# Report For Trainer
class ReportForTrainerForm(forms.ModelForm):
	class Meta:
		model=models.TrainerSubscriberReport
		fields=('report_for_trainer','report_msg')

# Report For User
class ReportForUserForm(forms.ModelForm):
	class Meta:
		model=models.TrainerSubscriberReport
		fields=('report_for_user','report_msg','report_from_trainer')
		widgets = {'report_from_trainer': forms.HiddenInput()}

# Report For Trainer 2nd
class ReportForTrainerForm(forms.ModelForm):
	class Meta:
		model=models.TrainerSubscriberReport
		fields=('report_for_trainer','report_msg','report_from_user')
		widgets = {'report_from_user': forms.HiddenInput()}