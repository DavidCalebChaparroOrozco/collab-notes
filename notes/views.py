from django.https import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> My Notes App </h1> <p> Your space to think, write and share your ideas. </p> ")