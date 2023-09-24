from django.db import models

class Upload(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.caption

class DemoTable(models.Model):
    # string, number, date, time, 
    # email, url, file, image, boolean, 
    # choice, large text

    gender_choices = (("M","Male",),
                      ("F","Female"),
                      ("NS","Not Specified"))
    
    name = models.CharField(max_length=30 )
    age = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True) 
    time = models.TimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    url = models.URLField(max_length=200)
    file = models.FileField(upload_to='files/')
    avatar = models.ImageField(upload_to='avatars/')
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=2, choices=gender_choices)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    given_to = models.CharField(max_length=50)
    priorty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# create a model for storing information about Places
