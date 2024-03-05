import random

from django.http import HttpResponse

from .models import Food

random.seed()

# Views

def get_nutrients(request):
    # Return HTTP response
    if request.method == "GET":
        result = []
        for item in Food.objects.all():
             result.append({"description": item.description, "fdc_id": item.fdc_id})
        return HttpResponse(result,status=200)
    else:
        return HttpResponse(status=502)

# Retrieve list of foods and categories

# Submit request information
    
# Builds response
    
# Builds recommendations
    

# Retrieve random food item.
def get_random_item(request):
        rand = str(random.randint(167512,175304))
        query = Food.objects.get(fdc_id=rand)
        return HttpResponse(query.description,status=200)
