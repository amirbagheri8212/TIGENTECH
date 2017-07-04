from django.db import models
from ckeditor.fields import RichTextField
def dp(list):
    list1 = ()
    for i in list:
        list1 += ((i, i,),)
        return list1
class Country(models.Model):
    Name = models.CharField(max_length=5000)
    Continents = ("Asia", "North America", "South America", "Australia", "Europe", "Africa",)
    Continents = dp(Continents)
    continent = models.CharField(max_length=1000, choices=Continents)
    def __str__(self):
        return self.Name
class Person(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    is_Dead = models.BooleanField()
    BC_Date = models.BooleanField(default=False)

    date_of_birth = models.DateField(help_text="if You Check the BC Date field please enter the BC year")
    PictureFile = models.ImageField()
    Bio = RichTextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Quote(models.Model):
    Text = RichTextField()
    From = models.ForeignKey(Person, models.CASCADE)
    def __str__(self):
        return self.From.name+" ^&*&^ "+str(self.pk)

