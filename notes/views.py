from django.https import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Collab Notes </h1> <p> Your space to think</p> <footer> Collab Notes 226 </footer> ")