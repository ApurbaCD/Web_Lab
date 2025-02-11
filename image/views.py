from django.shortcuts import render

# Create your views here.
from .form import ImageForm
from .models import Image


def index (request):

    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"index.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"index.html",{"img":img,"form":form})