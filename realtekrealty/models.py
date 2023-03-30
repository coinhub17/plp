from django.db import models


tp=[
    ('RENT','rent'),
    ('BUY','buy'),
]

class register(models.Model):
    firstname=models.CharField(max_length=100, blank=False, null=False)
    lastname=models.CharField(max_length=100, blank=False, null=False)
    username=models.CharField(max_length=100, blank=False, null=False)
    email=models.EmailField(max_length=100, blank=False, null=False)
    password=models.CharField(max_length=100, blank=False, null=False)
    password2=models.CharField(max_length=100, blank=False, null=False)
    
    
    class Meta:
        db_table = 'register'
        managed = True
    
    def __str__(self):
        return self.username
    
class Uploads(models.Model):
    hse=models.ImageField(upload_to='Images/')
    vhse=models.FileField(upload_to='Videos/')
    htp=models.CharField(max_length=10,choices=tp, blank=False, null=False)
    loc=models.CharField(max_length=100, blank=False, null=False)
    price=models.IntegerField()
    desc=models.CharField(max_length=100, blank=False, null=False)
    web=models.CharField(max_length=100, blank=False, null=False)
    phone=models.IntegerField()
    
    class Meta:
        db_table = 'upload'
        managed = True
    
    def __str__(self):
        return self.desc
    
class home(models.Model):
    img=models.ImageField()
    locate=models.CharField(max_length=100, blank=False, null=False)
    descr=models.CharField(max_length=100, blank=False, null=False)
    price=models.IntegerField()
    call=models.IntegerField()
    
    class Meta:
        db_table = 'loads'
        managed = True
    
    def __str__(self):
        return self.descr
    
    

# Create your models here.
