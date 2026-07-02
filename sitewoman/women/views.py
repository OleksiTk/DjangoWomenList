from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')



def cats(request, cat_slug):
    return HttpResponse(f'cats, World! (Slug: {cat_slug})')