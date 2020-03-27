from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import Animal


class ListAnimalsView(View):
    """
    List all animals in the database.
    """
    def get(self, request):
        animals = Animal.objects.all()
        return render(request, 'netbox_animal_sounds/animal_list.html', {
            'animals': animals,
        })


class AnimalView(View):
    """
    Display a single animal, identified by name in the URL.
    """
    def get(self, request, name):
        animal = get_object_or_404(Animal.objects.filter(name=name))
        return render(request, 'netbox_animal_sounds/animal.html', {
            'animal': animal,
        })


class RandomAnimalView(View):
    """
    Display a randomly-selected animal.
    """
    def get(self, request):
        animal = Animal.objects.order_by('?').first()
        return render(request, 'netbox_animal_sounds/animal.html', {
            'animal': animal,
        })

