from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
   peoples =[
       {'name' : 'Tushar Patekar', 'age':23},
       {'name' : 'JK', 'age':22},
       {'name' : 'suyog', 'age':15}
   ]
   text = """
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto ab aliquam vel. Odit accusamus sint fuga quidem aliquid ad. Laboriosam blanditiis, distinctio omnis similique eveniet ipsa doloremque quis voluptas voluptates.

    """
   vegetables = ['tomato', 'potato', 'baigan', 'ayye']
   return render(request, "home/index.html", context={'peoples':peoples, 'vegetables' : vegetables})


def about_page(request):
    return render(request, "home/about.html")
def contact_page(request):
    return render(request, "home/contact.html")

def success_page(request):
    return HttpResponse("<h1> this  sucess page</h1>")