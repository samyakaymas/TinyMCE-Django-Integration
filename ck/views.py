from django.shortcuts import render
from .forms import RichForm
from django.forms import Form
def index(request):
	form = RichForm()
	if request.method=="POST":
		form = RichForm(request.POST)
		value = request.POST
		print(value)
	return render(request,'index.html',context={'form':form})
