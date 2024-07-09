from hotels_app.models import *
from django import forms

class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            if isinstance(field.field, forms.BooleanField):
                field.field.widget.attrs["class"] = "form-check-input"
            else:
                field.field.widget.attrs['class'] = 'form-control w-25'

    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['user',]
        widgets = {
            "start": forms.DateInput(attrs={"type": "date", "class": "form-control w-25"}),
            "end": forms.DateInput(attrs={"type": "date", "class": "form-control w-25"})
        }



class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            if isinstance(field.field, forms.BooleanField):
                field.field.widget.attrs["class"] = "form-check-input"
            else:
                field.field.widget.attrs['class'] = 'form-control w-25'

    class Meta:
        model = Room
        fields = '__all__'