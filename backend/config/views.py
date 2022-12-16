from django.shortcuts import render


# * Default view for application
def index(request):
    return render(request, 'index.html')