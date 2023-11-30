from django.shortcuts import render
from .models import Repices
from django.views.generic import DetailView


def index(request):
	recipes = Repices.objects.order_by('date')
	return render(request, 'recipes/index.html', {'recipes' : recipes})

class RecipeDetails(DetailView):
	model = Repices
	template_name = 'recipes/details.html'
	context_object_name = 'recipe'