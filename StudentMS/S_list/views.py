from django.shortcuts import render

# Create your views here.
def S_list(request):
    return render(request, 'S-list.html')