from django.urls import path
from .views import (
    HomeView,
    SalaListView,
    SalaDetailView,
    SalaCreateView,
    SalaUpdateView,
    SalaDeleteView,
    PavimentoListView,
    PavimentoDetailView,
    PavimentoCreateView,
    PavimentoUpdateView,
    PavimentoDeleteView,
    OrientacaoListView,
    OrientacaoDetailView,
    OrientacaoCreateView,
    OrientacaoUpdateView,
    OrientacaoDeleteView,
    TipoSensorListView,
    TipoSensorDetailView,
    TipoSensorCreateView,
    TipoSensorUpdateView,
    TipoSensorDeleteView,
    SensorLogicoListView,
    SensorLogicoDetailView,
    SensorLogicoCreateView,
    SensorLogicoUpdateView,
    SensorLogicoDeleteView,
    ParametroListView,
    ParametroDetailView,
    ParametroCreateView,
    ParametroUpdateView,
    ParametroDeleteView,
    SensorFisicoListView,
    SensorFisicoDetailView,
    SensorFisicoCreateView,
    SensorFisicoUpdateView,
    SensorFisicoDeleteView,
    DashboardView,
    CustomReportView,
    CriticalSensorsReportView,
    AggregatedReportView,
    SensorDataAPIView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("salas/", SalaListView.as_view(), name="sala_list"),
    path("salas/<int:pk>/", SalaDetailView.as_view(), name="sala_detail"),
    path("salas/criar/", SalaCreateView.as_view(), name="sala_create"),
    path("salas/<int:pk>/editar/", SalaUpdateView.as_view(), name="sala_update"),
    path("salas/<int:pk>/deletar/", SalaDeleteView.as_view(), name="sala_delete"),
    path("pavimentos/", PavimentoListView.as_view(), name="pavimento_list"),
    path(
        "pavimentos/<int:pk>/", PavimentoDetailView.as_view(), name="pavimento_detail"
    ),
    path("pavimentos/criar/", PavimentoCreateView.as_view(), name="pavimento_create"),
    path(
        "pavimentos/<int:pk>/editar/",
        PavimentoUpdateView.as_view(),
        name="pavimento_update",
    ),
    path(
        "pavimentos/<int:pk>/deletar/",
        PavimentoDeleteView.as_view(),
        name="pavimento_delete",
    ),
    path("orientacoes/", OrientacaoListView.as_view(), name="orientacao_list"),
    path(
        "orientacoes/<int:pk>/",
        OrientacaoDetailView.as_view(),
        name="orientacao_detail",
    ),
    path(
        "orientacoes/criar/", OrientacaoCreateView.as_view(), name="orientacao_create"
    ),
    path(
        "orientacoes/<int:pk>/editar/",
        OrientacaoUpdateView.as_view(),
        name="orientacao_update",
    ),
    path(
        "orientacoes/<int:pk>/deletar/",
        OrientacaoDeleteView.as_view(),
        name="orientacao_delete",
    ),
    path("tipos-sensor/", TipoSensorListView.as_view(), name="tipo_sensor_list"),
    path(
        "tipos-sensor/<int:pk>/",
        TipoSensorDetailView.as_view(),
        name="tipo_sensor_detail",
    ),
    path(
        "tipos-sensor/criar/", TipoSensorCreateView.as_view(), name="tipo_sensor_create"
    ),
    path(
        "tipos-sensor/<int:pk>/editar/",
        TipoSensorUpdateView.as_view(),
        name="tipo_sensor_update",
    ),
    path(
        "tipos-sensor/<int:pk>/deletar/",
        TipoSensorDeleteView.as_view(),
        name="tipo_sensor_delete",
    ),
    path(
        "sensores-logicos/", SensorLogicoListView.as_view(), name="sensor_logico_list"
    ),
    path(
        "sensores-logicos/<int:pk>/",
        SensorLogicoDetailView.as_view(),
        name="sensor_logico_detail",
    ),
    path(
        "sensores-logicos/criar/",
        SensorLogicoCreateView.as_view(),
        name="sensor_logico_create",
    ),
    path(
        "sensores-logicos/<int:pk>/editar/",
        SensorLogicoUpdateView.as_view(),
        name="sensor_logico_update",
    ),
    path(
        "sensores-logicos/<int:pk>/deletar/",
        SensorLogicoDeleteView.as_view(),
        name="sensor_logico_delete",
    ),
    path("parametros/", ParametroListView.as_view(), name="parametro_list"),
    path(
        "parametros/<int:pk>/", ParametroDetailView.as_view(), name="parametro_detail"
    ),
    path("parametros/criar/", ParametroCreateView.as_view(), name="parametro_create"),
    path(
        "parametros/<int:pk>/editar/",
        ParametroUpdateView.as_view(),
        name="parametro_update",
    ),
    path(
        "parametros/<int:pk>/deletar/",
        ParametroDeleteView.as_view(),
        name="parametro_delete",
    ),
    path(
        "sensores-fisicos/", SensorFisicoListView.as_view(), name="sensor_fisico_list"
    ),
    path(
        "sensores-fisicos/<int:pk>/",
        SensorFisicoDetailView.as_view(),
        name="sensor_fisico_detail",
    ),
    path(
        "sensores-fisicos/criar/",
        SensorFisicoCreateView.as_view(),
        name="sensor_fisico_create",
    ),
    path(
        "sensores-fisicos/<int:pk>/editar/",
        SensorFisicoUpdateView.as_view(),
        name="sensor_fisico_update",
    ),
    path(
        "sensores-fisicos/<int:pk>/deletar/",
        SensorFisicoDeleteView.as_view(),
        name="sensor_fisico_delete",
    ),
    path("relatorio-customizado/", CustomReportView.as_view(), name="custom_report"),
    path(
        "relatorio-sensores-criticos/",
        CriticalSensorsReportView.as_view(),
        name="critical_sensors_report",
    ),
    path(
        "relatorio-agregado/", AggregatedReportView.as_view(), name="aggregated_report"
    ),
    path("api/sensor-data/", SensorDataAPIView.as_view(), name="sensor_data_api"),
]
