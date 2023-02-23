from django.db import models

# Create your models here.
class Table1(models.Model):
    title=models.CharField(max_length=200)
    pic=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.title
class Table2(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    desc=models.TextField()

    def __str__(self):
        return self.name