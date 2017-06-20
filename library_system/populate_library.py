import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'library.settings')
					  
import django
django.setup()
from library.models import Item, User

def populate():

	Users = [
	{"name": "John Smith",
	 "fine": 0},
	{"name": "jane Smith",
	 "fine": 0},
	{"name": "Alexis Duprey",
	 "fine": 0},
	{"name": "Casey Astacio",
	 "fine": 0}
	 
	 
	items = {"title": "Star Wars",
			 "fine": 0},
			{"name": "Casey Astacio",
			 "fine": 0},
			{"name": "Casey Astacio",
			 "fine": 0},
			{"name": "Casey Astacio",
			 "fine": 0},
		    {"name": "Casey Astacio",
			 "fine": 0},
	
	
	
	for cat, cat_data in cats.items():
		print(cat_data['views'])
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		for p in cat_data["pages"]:
			add_page(c, p["title"], p["url"], p["views"])
			
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))
			
def add_page(cat, title, url, views):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p
	
def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c
	
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()