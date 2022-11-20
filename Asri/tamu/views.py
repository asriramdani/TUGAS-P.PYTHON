from django.shortcuts import render

# Create your views here.
from . forms import Tamu

from . models import Guest
def index(request):
    buku_Tamu = Tamu()

    context = {
        'BukuTamu' :buku_Tamu,}


    if request.method == "POST":
        Guest.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
            kegiatan = request.POST.get('kegiatan'),
        )

    return render(request, 'tamu/index.html', context)