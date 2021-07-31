from django.db import models
from django.shortcuts import reverse

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    established = models.DateField(blank=True)
    grade = models.IntegerField()
    city = models.CharField(max_length=500)
    address = models.TextField()
    image_restaurant = models.ImageField(blank=True, upload_to='restaurant')
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['-grade']

    def __str__(self):
        return '{} start at {} with grade {} in {}'.format(self.name, self.established, self.grade, self.city)

    def get_absolute_url(self):
        return reverse('rest_name:detail_restaurant', args=[self.slug])

        
class Food(models.Model):
    SALAD = 'SA'
    BEVERAGES = 'BE'
    DESSERT = 'DE'
    MAIN_COURSE = 'MC'
    PISH_GHAZA = 'PG'

    FOOD_TYPE = [
        (SALAD, 'salad'),
        (BEVERAGES, 'beverages'),
        (DESSERT, 'desert'),
        (MAIN_COURSE, 'main course'),
        (PISH_GHAZA, 'pish_ghaza'),
    ]

    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grade = models.IntegerField(blank=True)
    image_food = models.ImageField(blank=True, upload_to='food')
    description = models.TextField(blank=True, null=True)
    food_type = models.CharField(max_length=2, choices=FOOD_TYPE)
    price = models.FloatField(null=True)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['-grade']

    def __str__(self):
        return '{}-{}-{} in {}'.format(self.name, self.grade, self.food_type, self.restaurant)


class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "comment by {} on {} {} ".format(self.name, self.food, self.restaurant)