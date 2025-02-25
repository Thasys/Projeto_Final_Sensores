# twodos/forms.py
from django import forms
from twodos.models import Sala, TipoSensor


class ReportFilterForm(forms.Form):
    start_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        label="Data Inicial",
    )
    end_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        label="Data Final",
    )
    sala = forms.ModelChoiceField(
        queryset=Sala.objects.all(), required=False, label="Sala"
    )
    tipo_sensor = forms.ModelChoiceField(
        queryset=TipoSensor.objects.all(), required=False, label="Tipo de Sensor"
    )
