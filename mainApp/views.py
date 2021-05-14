from django.shortcuts import render
from .models import Teammate
# Create your views here.
def main(request):
    teammates = Teammate.objects.all()
    return render (request, 'main.html', {'teammates':teammates})