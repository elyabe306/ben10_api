from django.db import models

class Alien(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    homeworld = models.CharField(max_length=100)
    abilities = models.TextField()  # Armazenará uma lista de habilidades em formato JSON
    image = models.ImageField(upload_to='alien_images')