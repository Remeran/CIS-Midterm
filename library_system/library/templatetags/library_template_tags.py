from django import template
from library.models import Item

register = template.Library()

@register.inclusion_tag('library/browse.html')
def get_category_list(item=None):
	return {'item': Item.objects.all(),
			'act_item': item}