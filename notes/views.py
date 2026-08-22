from django.https import HttpResponse
from notes.models import Note

# Create your views here.
def home(request):
    notes = Note.objects.count()
    return HttpResponse(
        "<h1>Collab Notes</h1> <p>Your ideas, in order.</p>"
        f"<p>Saved notes: {notes}</p>"
        "<footer>Collab Notes 226</footer>"
        "<p> DEBUG MODE ON </p>"
    )
