import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog

# Create your views here.

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = owner.dog_set.all()
            total_dog = []
            for dog in dogs:
                total_dog.append(
                    {
                    "dog's name" : dog.name,
                    "dog's age" : dog.age
                    }
                )
            results.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age,
                    "dog(s)" : total_dog
                }
        )
        return JsonResponse({'resutls':results}, status=200)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog = Dog.objects.create(
            owner = Owner.objects.get(name=data['owner']),
            name = data['name'],
            age = data['age']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results  = []
        for dog in dogs:
            results.append(
                {
                    "owner" : dog.owner.name,
                    "name" : dog.name,
                    "age" : dog.age
                }
        )
        return JsonResponse({'resutls':results}, status=200)