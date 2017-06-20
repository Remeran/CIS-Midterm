from django.shortcuts import render
from library.models import Item, User
from library.forms import UserForm
from library.forms import ItemForm
from library.forms import SearchForm
from library.forms import CheckForm


# Create your views here.
from django.http import HttpResponse

def index(request):	
	return render(request, 'library/index.html')
	
def browse(request):

	item_list = Item.objects.all()
	context_dict = {'items': item_list}
	
	return render(request, 'library/browse.html', context_dict)
	
def checked_out(request):	

	checked_list = Item.objects.all().filter(checked_out=True)
	context_dict = {'items': checked_list}
	
	return render(request, 'library/checked_out.html', context_dict)
	
def add_user(request):
	form = UserForm()
	
	if request.method == 'POST':
		form = UserForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'library/add_user.html', {'form': form})
	
def add_item(request):
	form = ItemForm()
	
	if request.method == 'POST':
		form = ItemForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'library/add_item.html', {'form': form})
	
def search(request):
	form = SearchForm()
	
	if request.method == 'POST':
		form = SearchForm(request.POST)
		
		if form.is_valid():
			search = form.cleaned_data['search']
			cat = form.cleaned_data['category']
			if cat == 'None':
				cat_items = Item.objects.all()
				print(cat)
			else:
				cat_items = Item.objects.filter(category__icontains = cat)
				print(cat)
			search_list = cat_items.filter(title__icontains = search)
			context_dict = {'items': search_list}
			return render(request, 'library/search_results.html', context_dict)
		else:
			print(form.errors)
	return render(request, 'library/search.html', {'form': form} )
	
def show_item(request, item_name_slug):
	item = Item.objects.get(slug=item_name_slug)
	return render(request, 'library/item.html', {'item': item})
	
def check_out(request, item_name_slug):
	item = Item.objects.get(slug=item_name_slug)
	form = CheckForm()
	
	if request.method == 'POST':
		form = CheckForm(request.POST, instance=item)
		
		if form.is_valid():
			form.save()
			return index(request)
		else:
			print(form.errors)
	context_dict = {'form': form, 'item': item}
	return render(request, 'library/check_out.html', context_dict)
	
def check_in(request, item_name_slug):
	item = Item.objects.get(slug=item_name_slug)
	form = CheckForm()
	
	if request.method == 'POST':
		form = CheckForm(request.POST, instance=item)
		
		if form.is_valid():
			item = form.save(commit=False)
			item.checked_out = False
			item.save()
			return index(request)
		else:
			print(form.errors)
	context_dict = {'form': form, 'item': item}
	return render(request, 'library/check_in.html', context_dict)

