from django.db import models
# Create your models here.
from django.utils.text import slugify
'''
Django model field:
    -html widget
    -validation
    -db size   
'''

JOB_TYPE= (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

def image_upload(instance,filename):
    imagename , extention =filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)



class Job(models.Model): #table
    title= models.CharField(max_length=100)  #column
    #location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=image_upload)
    #http://127.0.0.1:8000/Job/(web-developer)
    #go to html file and edit (id -->slug) in line 126 and 140
    slug=models.SlugField(null=True,blank=True)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='apply_job')
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    website=models.URLField()
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name