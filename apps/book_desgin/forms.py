from django import forms
from .models import DesignBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = DesignBooking
        fields = '__all__'