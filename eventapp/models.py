from django.db import models


class welcome_page(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    date=models.DateField()
    description=models.CharField(max_length=100)
    count=models.CharField(max_length=3,default='0')
    
    def __str__(self):
        return self.name




