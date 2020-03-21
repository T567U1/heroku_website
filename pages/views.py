from django.shortcuts import render

# Create your views here.
def get_theman(request, *args, **kwargs):
    contex = {
        'boi': "It's me"
    }
    return render(request, 'home.html', contex)
