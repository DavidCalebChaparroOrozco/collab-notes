from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Collab Notes </h1> <p> Welcome to the Notes App! </p>")