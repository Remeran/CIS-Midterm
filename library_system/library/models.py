from django.db import models
from datetime import timedelta
from django.template.defaultfilters import slugify



class User(models.Model):
	name = models.CharField(max_length=128)
	fine = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name



class Item(models.Model):
	CAT_CHOICES = (
		('None', 'None'),
		('Generalities', (
				('Data Processing', 'Data Processing'),
				('Computer Science', 'Computer Science'),
				('Subject bibliographies and indexes', 'Subject bibliographies and indexes'),
				('Library and information sciences', 'Library and information sciences'),
				('General encyclopedias', 'General encyclopedias'),
				('News media, journalism, publishing', 'News media, journalism, publishing'),
				('Australian journalism and news media', 'Australian journalism and news media'),
			)
		),
		('Philosophy and Psychology', (
				('Specific philosophical schools of thought', 'Specific philosophical schools of thought'),
				('Psychology', 'Psychology'),
				('Differential and developmental psychology', 'Differential and developmental psychology'),
				('Applied psychology', 'Applied psychology'),
				('Logic', 'Logic'),
				('Ethics', 'Ethics (moral philosophy)'),
				('Ancient, medieval and oriental philosophy', 'Ancient, medieval and oriental philosophy'),
				('Modern Western philosophy', 'Modern Western philosophy'),
			)
		),
		('Religion', (
				('Natural theology', 'Natural theology'),
				('The Bible', 'The Bible'),
				('Christian denominations and sects', 'Christian denominations and sects'),
				('Other and comparative religions', 'Other and comparative religions'),
			)
		),
		('Social Sciences', (
				('Sociology and anthropology', 'Sociology and anthropology'),
				('Social groups', 'Social groups'),
				('General statistics', 'General statistics'),
				('Political science', 'Political science'),
			)
		),
		('Languages', (
				('Linguistics', 'Linguistics'),
				('English language', 'English language'),
				('French language', 'French language'),
				('Other languages', 'Other languages'),
			)
		),
		('Science', (
				('Mathematics', 'Mathematics'),
				('Astronomy and allied sciences', 'Astronomy and allied sciences'),
				('Physics', 'Physics'),
				('Chemistry and allied sciences', 'Chemistry and allied sciences'),
			)
		),
		('Technology (Applied Sciences)', (
				('Medical Sciences', 'Medical Sciences'),
				('Nursing', 'Nursing'),
				('Engineering and allied operations', 'Engineering and allied operations'),
				('Accounting', 'Accounting'),
				('Management', 'Management'),
			)
		),
		('Geography and History', (
				('Geography and travel', 'Geography and travel'),
				('Regional geography', 'Regional geography'),
				('Biography', 'Biography'),
				('Ancient history', 'Ancient history'),
				('European history', 'European history'),
				('Asian history', 'Asian history'),
				('United States history', 'United States history'),
			)
		),
		('Arts and Recreation', (
				('History of art', 'History of art'),
				('Architecture', 'Architecture'),
				('Sculpture and ceramics', 'Sculpture and ceramics'),
				('Painting', 'Painting'),
				('Artists', 'Artists'),
				('Music', 'Music'),
			)
		),
		('Literature', (
				('American literature', 'American literature'),
				('English literature', 'English literature'),
				('Canadian literature', 'Canadian literature'),
				('Australian literature', 'Australian literature'),
				('French literature', 'French literature'),
				('Spanish literature', 'Spanish literature'),
			)
		),
	)
	
	TYPE_CHOICES = (
		('none', 'None'),
		('dvd', 'DVD'),
		('bluray', 'Blu-ray'),
		('book', 'Book'),
		('magazine', 'Magazine'),
		('newspaper', 'Newspaper'),
		('reference book', 'Reference Book'),
		
	)

	title = models.CharField(max_length=128)
	category = models.CharField(
		max_length=100,
		choices=CAT_CHOICES,
		default='None'
	)
	type = models.CharField(
		max_length=50,
		choices=TYPE_CHOICES,
		default='None'
	)
	checked_out = models.BooleanField(default=False)
	assigned_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
	time_passed = models.DurationField(default=timedelta())
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Item, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
