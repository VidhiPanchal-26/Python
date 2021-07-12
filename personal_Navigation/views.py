#this is my file
from django.http import HttpResponse

def personalNav(request):
    head = "<h1>My Personal Website Navigator </h1>"
    link1 = "<a href='https://www.youtube.com/'>YouTube</a>"
    link2 = "<a href='https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p'>Django Tutorials</a>"
    link3 = "<a href='https://www.instagram.com/'>Instagram</a>"
    link4 = "<a href='https://web.whatsapp.com/'>WhatsApp</a>"
    
    return HttpResponse(head+ "<br/>"+link1+"</br>"+link2+"</br>"+link3+"</br>"+link4)