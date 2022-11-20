from django import forms

class Tamu(forms.Form):
    nim = forms.CharField(max_length=10)
    nama = forms.CharField(max_length=50)
    kegiatan = forms.CharField(
        widget= forms.Textarea
    )
