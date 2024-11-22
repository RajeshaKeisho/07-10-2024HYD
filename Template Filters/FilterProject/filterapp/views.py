from django.shortcuts import render

# Create your views here.
def filter_view(request):
    return render(request, 'template.html', {"name":"World!", "number":5})