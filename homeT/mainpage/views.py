from django.shortcuts import render
from routinepage.models import Routine

# Create your views here.
def main(request):
    hotRoutine = Routine.objects.all().order_by('-id')[:5]


    return render(request, 'main.html',{
        'hotRoutine' : hotRoutine,
    })