from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Restaurant, Food
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm


class ListRestaurant(ListView):
    template_name = 'restaurant/restaurant_list.html'
    model = Restaurant

    def get_queryset(self):
        return Restaurant.objects.filter(grade__gte=4).order_by('-grade')[:10]


def best_food(request,slug):
    list_food = Food.objects.filter(grade__gte=3, slug=slug).order_by('grade')[:10]
    return render(request, 'restaurant/best_food_list.html', context={'foods': list_food})
    

def restaurant_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    foods = restaurant.food_set.all()
    restaurant = get_object_or_404(Restaurant,slug=slug)
    comments = restaurant.comments.all()
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.restaurant = restaurant
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name='restaurant/restaurant_detail.html', context={'foods':foods, 
                                                                                        'comments':comments,
                                                                                        'new_comment':new_comment, 
                                                                                        'comment_form':comment_form})


def search_restaurant(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', default = "")
        restaurants = Restaurant.objects.filter(name__icontains=searched)
        return render(request, 'restaurant/search.html', context={'searched':searched, 'restaurants':restaurants})

    else:
        return render(request, 'restaurant/search.html', {})




