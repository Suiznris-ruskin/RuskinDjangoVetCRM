from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages
from .models import Visit
from .models import Pet
from .models import Pet_Parent
import requests
from django.http import JsonResponse

# Create your views here.
def home(request):
    visits = Visit.objects.all()

    #check to see if logging in
    if request.method =='POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        #Authenticate
        user = authenticate(request, username=uname, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"There was an error loging in..")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':visits})

def visit_home(request):
    visits = Visit.objects.all()
    if request.user.is_authenticated:
        return render(request,'visit_home.html', {'records':visits})
    else:
        messages.success(request, "You must be logged in to see that..."  )
        return redirect('home')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out..."  )
    return redirect('home')


def customer_visit(request,pk):
    if request.user.is_authenticated:
        # look up record
        customer_visit = Visit.objects.get(id=pk)
        return render(request,'visit.html', {'customer_visit':customer_visit})
    else:
        messages.success(request, "You must be logged in to see that..."  )
        return redirect('home')
    

def integration(request):
    if request.user.is_authenticated:
        # look up record
        return render(request,'integration.html')
    else:
        messages.success(request, "You must be logged in to see that..."  )
        return redirect('home')
    
def calendar(request):
    if request.user.is_authenticated:
        # look up record
        return render(request,'calendar.html')
    else:
        messages.success(request, "You must be logged in to see that..."  )
        return redirect('home')
    
def pets(request):
    if request.user.is_authenticated:
        pets = Pet.objects.all()
        return render(request,'pets.html', {'records':pets})
    else:
        messages.success(request, "You must be logged in to see that..."  )
        return redirect('home')
    
    
def pet_parents(request):
    if request.user.is_authenticated:
        pet_parents = Pet_Parent.objects.all()
        return render(request,'pet_parents.html', {'records':pet_parents})
    else:
        messages.success(request, "You must be logged in to see that..."  )
        return redirect('home')
    


#def api_call(request):
 #   api_url = 'https://7cefabkfrj.execute-api.us-west-2.amazonaws.com/Prod/classify_digit/'
 #   raw_data = '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'
 #   response = requests.post(api_url, data=raw_data)
 #   result = response.json()
  ##  return render_template('result.html', result=result)
 #   return render(requests,'integration.html', {
 #           "result": result,
 #       }) 

def api_call(request):
    # Extract the data from the request
    data = request.POST.get('raw_data')
   # data = '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';  
    # Use the data in the API call
    url = 'https://7cefabkfrj.execute-api.us-west-2.amazonaws.com/Prod/classify_digit/'  # Replace with your API endpoint
  #  url = 'https://gk4fv03hyl.execute-api.us-east-2.amazonaws.com/test/dragons'

    response = requests.post(url,json=data)

    if response.status_code == 200:
        data = response.json()
        return render(request,'integration.html',{'response':data})
    else:
        return JsonResponse(response.json(), status=500)