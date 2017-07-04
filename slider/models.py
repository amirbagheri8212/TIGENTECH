from django.db import models
class sliderimg(models.Model):
    name = models.CharField(max_length=800)
    image = models.FileField(upload_to="slider")
    def __str__(self):
        return self.name+" =  {OO}  =  "+self.image.url