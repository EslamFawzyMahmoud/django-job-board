from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Job
from .form import ApplyForm ,Jobform
# Create your views here.
def Job_List(request):
    Job_List=Job.objects.all()
    paginator = Paginator(Job_List, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'Job':page_obj} #template name
    return render(request,'Job/Job_List.html',context)


def Job_Detail(request,slug):
    Job_Detail=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=Job_Detail
            myform.save()
    else:
        form=ApplyForm()

    context={'jobs':Job_Detail,'form':form}
    return render(request,'Job/Job_Detail.html',context)

def add_job(request):

    if request.method=='POST':
        form=Jobform(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=Jobform()

    return render(request,'Job/add_job.html',{'form':form})