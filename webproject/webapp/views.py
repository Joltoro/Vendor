from django.shortcuts import render

# Create your views here.
def home(context):
    x= "Fence"
    return render(context,'home.html',{'Key':x})
