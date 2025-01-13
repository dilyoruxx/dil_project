from django.db import models

# Create your models here.

class Book(models.Model):
    autor = models.CharField(max_length=50) 
    year = models.PositiveIntegerField
    pages = models.PositiveIntegerField
    name = models.CharField(max_length=25)

#     def __str__(self):
#         return self.name

class About(models.Model):
    image = models.ImageField(
        upload_to="about_images/",
        verbose_name="фотография",
        null=True, blank=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name='загаловок'
    )
    description = models.TextField(
        verbose_name='описание'
    )

    def __str__(self):
        return f'{self.id}- {self.title}'
    
    class Meta:
        verbose_name='обо мне'
        verbose_name_plural='о нас'

"""
test = About()
print(test)
print(test.title)
print(test.discriptions)
"""    
    
"""
cursor.execute(
CREATE TABLE IF NOT EXISTS about(
title VARCHAR (200)
description TEXT
)
)
"""