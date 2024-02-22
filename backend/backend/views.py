from django.http import HttpResponse

# Views

def status(request):
    # Return HTTP response
    if request.method == "GET":
        return HttpResponse("working",status=200)
    else:
        return HttpResponse(status=502)

# Retrieve list of foods and categories

# Submit request information
    
# Builds response
    
# Builds recommendations
    

    
