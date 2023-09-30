from django.db import models

class Upload(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.caption

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
class PhotographerProfile(models.Model):
    gender_choices = ((0, "FEMALE"), (1, "MALE"), (2, "OTHER"))
    photographer = models.OneToOneField(Photographer, on_delete=models.CASCADE, related_name='profile')
    city = models.CharField(max_length=50)
    gender = models.IntegerField(choices=gender_choices)

    def __str__(self):
        return f"{self.photographer.name}"
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='players')
    def __str__(self):
        return self.name