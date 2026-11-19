from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {"name":'Mehrad',"surname":"Sodagari","age":21,"skills":["Python","JavaScript","HTML","CSS"]}
    return render(request,"website/index.html",context)