import datetime
from .forms import ReportFilterForm
from django.db.models import (
    Count,
    Q,
    F,
    Max,
    Avg,
    ExpressionWrapper,
    FloatField,
    DateTimeField,
)
from django.db.models.functions import Trunc, Cast, Extract
from django.db import connection
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import (
    Pavimento,
    Orientacao,
    TipoSensor,
    SensorLogico,
    Sala,
    Parametro,
    SensorFisico,
    LeituraSensor,
    Leitura,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException


class SalaListView(ListView):
    model = Sala
    template_name = "twodos/sala_list.html"
    context_object_name = "salas"
    ordering = ["nome"]  # Ordenação mais intuitiva
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().select_related("pavimento", "orientacao")


class SalaDetailView(DetailView):
    model = Sala
    template_name = "twodos/sala_detail.html"
    context_object_name = "sala"

    def get_queryset(self):
        return super().get_queryset().select_related("pavimento", "orientacao")


class SalaCreateView(CreateView):
    model = Sala
    fields = ["nome", "sigla", "pavimento", "orientacao"]
    template_name = "twodos/sala_form.html"
    success_url = reverse_lazy("sala_list")


class SalaUpdateView(UpdateView):
    model = Sala
    fields = ["nome", "sigla", "pavimento", "orientacao"]
    template_name = "twodos/sala_form.html"
    success_url = reverse_lazy("sala_list")


class SalaDeleteView(DeleteView):
    model = Sala
    template_name = "twodos/sala_confirm_delete.html"
    success_url = reverse_lazy("sala_list")


class HomeView(TemplateView):
    template_name = "twodos/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Recupera todos os sensores físicos do banco de dados
        context["sensores_fisicos"] = SensorFisico.objects.all()
        return context


class PavimentoListView(ListView):
    model = Pavimento
    template_name = "twodos/pavimento_list.html"
    context_object_name = "pavimentos"
    ordering = ["-id"]
    paginate_by = 10


class PavimentoDetailView(DetailView):
    model = Pavimento
    template_name = "twodos/pavimento_detail.html"
    context_object_name = "pavimento"


class PavimentoCreateView(CreateView):
    model = Pavimento
    fields = ["nome"]
    template_name = "twodos/pavimento_form.html"
    success_url = reverse_lazy("pavimento_list")


class PavimentoUpdateView(UpdateView):
    model = Pavimento
    fields = ["nome"]
    template_name = "twodos/pavimento_form.html"
    success_url = reverse_lazy("pavimento_list")


class PavimentoDeleteView(DeleteView):
    model = Pavimento
    template_name = "twodos/pavimento_confirm_delete.html"
    success_url = reverse_lazy("pavimento_list")


class OrientacaoListView(ListView):
    model = Orientacao
    template_name = "twodos/orientacao_list.html"
    context_object_name = "orientacoes"
    ordering = ["-id"]
    paginate_by = 10


class OrientacaoDetailView(DetailView):
    model = Orientacao
    template_name = "twodos/orientacao_detail.html"
    context_object_name = "orientacao"


class OrientacaoCreateView(CreateView):
    model = Orientacao
    fields = ["nome"]
    template_name = "twodos/orientacao_form.html"
    success_url = reverse_lazy("orientacao_list")


class OrientacaoUpdateView(UpdateView):
    model = Orientacao
    fields = ["nome"]
    template_name = "twodos/orientacao_form.html"
    success_url = reverse_lazy("orientacao_list")


class OrientacaoDeleteView(DeleteView):
    model = Orientacao
    template_name = "twodos/orientacao_confirm_delete.html"
    success_url = reverse_lazy("orientacao_list")


class TipoSensorListView(ListView):
    model = TipoSensor
    template_name = "twodos/tipo_sensor_list.html"
    context_object_name = "tipos"
    ordering = ["-id"]
    paginate_by = 10


class TipoSensorDetailView(DetailView):
    model = TipoSensor
    template_name = "twodos/tipo_sensor_detail.html"
    context_object_name = "tipo"


class TipoSensorCreateView(CreateView):
    model = TipoSensor
    fields = [
        "descricao",
        "limite_inferior_permitido",
        "limite_superior_permitido",
        "unidade",
    ]
    template_name = "twodos/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")


class TipoSensorUpdateView(UpdateView):
    model = TipoSensor
    fields = [
        "descricao",
        "limite_inferior_permitido",
        "limite_superior_permitido",
        "unidade",
    ]
    template_name = "twodos/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")


class TipoSensorDeleteView(DeleteView):
    model = TipoSensor
    template_name = "twodos/tipo_sensor_confirm_delete.html"
    success_url = reverse_lazy("tipo_sensor_list")


class SensorLogicoListView(ListView):
    model = SensorLogico
    template_name = "twodos/sensor_logico_list.html"
    context_object_name = "sensores_logicos"
    ordering = ["-id"]
    paginate_by = 10


class SensorLogicoDetailView(DetailView):
    model = SensorLogico
    template_name = "twodos/sensor_logico_detail.html"
    context_object_name = "sensor_logico"


class SensorLogicoCreateView(CreateView):
    model = SensorLogico
    fields = ["sensor_fisico", "tipo_sensor", "descricao"]
    template_name = "twodos/sensor_logico_form.html"
    success_url = reverse_lazy("sensor_logico_list")


class SensorLogicoUpdateView(UpdateView):
    model = SensorLogico
    fields = ["sensor_fisico", "tipo_sensor", "descricao"]
    template_name = "twodos/sensor_logico_form.html"
    success_url = reverse_lazy("sensor_logico_list")


class SensorLogicoDeleteView(DeleteView):
    model = SensorLogico
    template_name = "twodos/sensor_logico_confirm_delete.html"
    success_url = reverse_lazy("sensor_logico_list")


class ParametroListView(ListView):
    model = Parametro
    template_name = "twodos/parametro_list.html"
    context_object_name = "parametros"
    ordering = ["-id"]
    paginate_by = 10


class ParametroDetailView(DetailView):
    model = Parametro
    template_name = "twodos/parametro_detail.html"
    context_object_name = "parametro"


class ParametroCreateView(CreateView):
    model = Parametro
    fields = ["sensor_logico", "nome", "valor"]
    template_name = "twodos/parametro_form.html"
    success_url = reverse_lazy("parametro_list")


class ParametroUpdateView(UpdateView):
    model = Parametro
    fields = ["sensor_logico", "nome", "valor"]
    template_name = "twodos/parametro_form.html"
    success_url = reverse_lazy("parametro_list")


class ParametroDeleteView(DeleteView):
    model = Parametro
    template_name = "twodos/parametro_confirm_delete.html"
    success_url = reverse_lazy("parametro_list")


class SensorFisicoListView(ListView):
    model = SensorFisico
    template_name = "twodos/sensor_fisico_list.html"
    context_object_name = "sensores_fisicos"
    ordering = ["-id"]
    paginate_by = 10


class SensorFisicoDetailView(DetailView):
    model = SensorFisico
    template_name = "twodos/sensor_fisico_detail.html"
    context_object_name = "sensor_fisico"


class SensorFisicoCreateView(CreateView):
    model = SensorFisico
    fields = ["nome", "sigla", "descricao", "tensao_min", "tensao_max"]
    template_name = "twodos/sensor_fisico_form.html"
    success_url = reverse_lazy("sensor_fisico_list")


class SensorFisicoUpdateView(UpdateView):
    model = SensorFisico
    fields = ["nome", "sigla", "descricao", "tensao_min", "tensao_max"]
    template_name = "twodos/sensor_fisico_form.html"
    success_url = reverse_lazy("sensor_fisico_list")


class SensorFisicoDeleteView(DeleteView):
    model = SensorFisico
    template_name = "twodos/sensor_fisico_confirm_delete.html"
    success_url = reverse_lazy("sensor_fisico_list")


class DashboardView(TemplateView):
    template_name = "twodos/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        end_time = timezone.now()
        start_time = end_time - datetime.timedelta(hours=24)

        # Dados para os gráficos
        temperature_readings = (
            LeituraSensor.objects.filter(
                sensor_logico__tipo_sensor__descricao__iexact="temperatura",
                leitura__data_hora__range=(start_time, end_time),
            )
            .select_related("leitura", "sensor_logico__tipo_sensor")
            .order_by("leitura__data_hora")
        )

        humidity_readings = (
            LeituraSensor.objects.filter(
                sensor_logico__tipo_sensor__descricao__iexact="umidade",
                leitura__data_hora__range=(start_time, end_time),
            )
            .select_related("leitura", "sensor_logico__tipo_sensor")
            .order_by("leitura__data_hora")
        )

        # Preparando dados para os gráficos
        context.update(
            {
                "temp_labels": [
                    reading.leitura.data_hora.strftime("%H:%M")
                    for reading in temperature_readings
                ],
                "temp_values": [
                    float(reading.valor) for reading in temperature_readings
                ],
                "hum_labels": [
                    reading.leitura.data_hora.strftime("%H:%M")
                    for reading in humidity_readings
                ],
                "hum_values": [float(reading.valor) for reading in humidity_readings],
            }
        )

        # Dados do status das salas
        salas = Sala.objects.prefetch_related(
            "leituras__leituras_sensores__sensor_logico__tipo_sensor"
        ).all()

        salas_status = []
        for sala in salas:
            ultima_leitura = sala.leituras.order_by("-data_hora").first()

            temperatura = umidade = None
            if ultima_leitura:
                temperatura = ultima_leitura.leituras_sensores.filter(
                    sensor_logico__tipo_sensor__descricao__iexact="Temperatura"
                ).first()

                umidade = ultima_leitura.leituras_sensores.filter(
                    sensor_logico__tipo_sensor__descricao__iexact="Umidade"
                ).first()

            salas_status.append(
                {
                    "sala": sala,
                    "ultima_leitura": (
                        ultima_leitura.data_hora if ultima_leitura else "N/A"
                    ),
                    "temperatura": temperatura.valor if temperatura else "N/A",
                    "umidade": umidade.valor if umidade else "N/A",
                }
            )

        context["salas_status"] = salas_status
        return context


class CustomReportView(TemplateView):
    template_name = "twodos/custom_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ReportFilterForm(self.request.GET or None)
        context["form"] = form
        results = None

        if form.is_valid():
            qs = LeituraSensor.objects.select_related(
                "leitura__sala", "sensor_logico__tipo_sensor"
            )
            # ... filtros mantidos
            results = qs.order_by("-leitura__data_hora")

        context["results"] = results
        return context


class CriticalSensorsReportView(TemplateView):
    template_name = "twodos/critical_sensors_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        critical_data = (
            LeituraSensor.objects.annotate(
                lower_limit=F("sensor_logico__tipo_sensor__limite_inferior_permitido"),
                upper_limit=F("sensor_logico__tipo_sensor__limite_superior_permitido"),
            )
            .filter(Q(valor__lt=F("lower_limit")) | Q(valor__gt=F("upper_limit")))
            .values("sensor_logico")
            .annotate(
                critical_count=Count("id"), last_reading=Max("leitura__data_hora")
            )
            .order_by("-critical_count")
        )

        sensor_ids = [item["sensor_logico"] for item in critical_data]
        sensors = SensorLogico.objects.filter(id__in=sensor_ids).select_related(
            "tipo_sensor"
        )

        sensor_data = []
        for sensor in sensors:
            data = next(
                item for item in critical_data if item["sensor_logico"] == sensor.id
            )
            sensor_data.append(
                {
                    "sensor": sensor,
                    "critical_count": data["critical_count"],
                    "last_reading": data["last_reading"],
                }
            )

        context["sensor_data"] = sorted(
            sensor_data, key=lambda x: x["critical_count"], reverse=True
        )
        return context


class AggregatedReportView(TemplateView):
    template_name = "twodos/aggregated_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interval = int(self.request.GET.get("interval", 60))  # Intervalo em minutos

        # Cálculo do intervalo personalizado
        aggregated_data = LeituraSensor.objects.annotate(
            total_minutes=Extract("leitura__data_hora", "epoch") / 60,
            time_bucket=Cast(
                (F("total_minutes") / interval).astype("integer") * interval,
                output_field=DateTimeField(),
            )
            .values("time_bucket", "sensor_logico__tipo_sensor__descricao")
            .annotate(average_value=Avg("valor"))
            .order_by("time_bucket"),
        )

        # Formatação dos dados
        context["aggregated_data"] = [
            (
                item["time_bucket"].strftime("%d/%m/%Y %H:%M"),
                item["sensor_logico__tipo_sensor__descricao"],
                round(float(item["average_value"]), 2),
            )
            for item in aggregated_data
        ]

        context["interval"] = interval
        return context


class AggregatedReportView(TemplateView):
    template_name = "twodos/aggregated_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SensorDataAPIView(APIView):
    def get(self, request):
        sensor1 = request.GET.get("sensor1")
        sensor2 = request.GET.get("sensor2")

        data = {
            "sensor1": self.get_sensor_data(sensor1),
            "sensor2": self.get_sensor_data(sensor2),
        }
        return Response(data)

    def get_sensor_data(self, sensor_id):
        return list(
            LeituraSensor.objects.filter(sensor_logico=sensor_id).values(
                "leitura__data_hora", "valor"
            )
        )


class SensorDataAPIView(APIView):
    def get(self, request):
        try:
            sensor1 = request.GET.get("sensor1")
            sensor2 = request.GET.get("sensor2")

            if not sensor1 or not sensor2:
                raise APIException("Parâmetros sensor1 e sensor2 são obrigatórios")

            data = {
                "sensor1": self.get_sensor_data(sensor1),
                "sensor2": self.get_sensor_data(sensor2),
            }
            return Response(data)

        except Exception as e:
            return Response({"error": str(e)}, status=400)

    def get_sensor_data(self, sensor_id):
        return list(
            LeituraSensor.objects.filter(sensor_logico=sensor_id)
            .values("leitura__data_hora", "valor")
            .order_by("leitura__data_hora")
        )
