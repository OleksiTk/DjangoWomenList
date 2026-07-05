from django import template
from women.models import Category
import women.views as views



register = template.Library()





@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=None):
    
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}