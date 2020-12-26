from django.shortcuts import render
from .models import Job
# Create your views here.
def Job_List(request):
    Job_List=Job.objects.all()
    context={'jobs':Job_List} #template name
    return render(request,'Job/Job_List.html',context)


def Job_Detail(request,id):
    Job_Detail=Job.objects.get(id=id)
    context={'jobs':Job_Detail}
    return render(request,'Job/Job_Detail.html',context)

