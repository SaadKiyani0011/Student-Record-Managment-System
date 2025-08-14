from django.shortcuts import render

# Create your views here.
def S_add(request):
    return render(request, 'S-add.html')