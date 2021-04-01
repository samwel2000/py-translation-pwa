from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    template_name = 'blog/home.html'
    context = {}
    return render(request, template_name, context)

def item(request):
    data = _('i am data fellas')
    template_name = 'blog/home.html'
    context = {
        'data':data
    }
    return render(request, template_name, context)