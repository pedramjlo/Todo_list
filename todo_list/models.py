from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    class ColourChoice(models.TextChoices):
        RED = 'red', 'Red'
        BLUE = 'blue', 'Blue'
        GREEN = 'green', 'Green'
        BLACK = 'black', 'Black'
        PURPLE = 'purple', 'Purple'
        YELLOW = 'yellow', 'Yellow'
        WHITE = 'white', 'White'

    name = models.CharField(max_length=50, null=False, blank=True)
    colour = models.CharField(max_length=8, choices=ColourChoice, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name



class Task(models.Model):
    is_pinned = models.BooleanField(default=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



