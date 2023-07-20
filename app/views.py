from django.shortcuts import render
from .models import ContactForm

# Create your views here.
def index(request):
    obj=ContactForm.objects.all()
    context={
        "obj":obj, 
    }
    return render(request, "index.html", context)


def saveContact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        code = request.POST.get('country_code')
        ph = request.POST.get('phone_number')
        data = ContactForm(name=name, ph1=code, ph2=ph)
        data.save()
    return index(request)