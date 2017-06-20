from django import forms
from datetime import timedelta
from library.models import User, Item

class UserForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
	                       help_text="Please Enter the user's name.")
	fine = forms.IntegerField(widget= forms.HiddenInput(), initial=0)
	
	class Meta:
		model = User
		fields = ('name'),
		
class ItemForm(forms.ModelForm):
	title = forms.CharField(max_length=128,
				            help_text="Please enter the item's title.")
	category = forms.ChoiceField(choices=Item.CAT_CHOICES, 
								 help_text="Please choose the category.")
	type = forms.ChoiceField(choices=Item.TYPE_CHOICES, 
								 help_text="Please choose the type.")
	checked_out = forms.BooleanField(widget= forms.HiddenInput(),required = False, initial = False)
	assigned_user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
	time_passed = forms.DurationField(widget= forms.HiddenInput(), initial=timedelta())
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Item
		fields = ('title', 'category', 'type', 'assigned_user')
		
class SearchForm(forms.ModelForm):
	category = forms.ChoiceField(choices=Item.CAT_CHOICES, 
								 help_text="Please choose the category.")
	search = forms.CharField(required=False, max_length=128,
							 help_text="Search (leave blank to browse by category):")
	
	class Meta:
		model = Item
		fields = ('search','category',)
		
class CheckForm(forms.ModelForm):
	checked_out = forms.BooleanField(widget= forms.HiddenInput(), initial = True)
	assigned_user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, help_text="Who are you?:")
	
	class Meta:
		model = Item
		fields = ('checked_out','assigned_user',)