from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Pavimento(models.Model):
    nome = models.CharField(
        max_length=50, unique=True, verbose_name="Nome do Pavimento"
    )

    class Meta:
        verbose_name = "Pavimento"
        verbose_name_plural = "Pavimentos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Orientacao(models.Model):
    nome = models.CharField(
        max_length=50, unique=True, verbose_name="Orientação Cardinal"
    )

    class Meta:
        verbose_name = "Orientação"
        verbose_name_plural = "Orientações"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Sala(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da Sala")
    sigla = models.CharField(
        max_length=10, unique=True, verbose_name="Sigla Identificadora"
    )
    pavimento = models.ForeignKey(
        Pavimento,
        on_delete=models.CASCADE,
        related_name="salas_pavimento",
        verbose_name="Pavimento Associado",
    )
    orientacao = models.ForeignKey(
        Orientacao,
        on_delete=models.CASCADE,
        related_name="salas_orientacao",
        verbose_name="Orientação Geográfica",
    )

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ["pavimento__nome", "nome"]
        indexes = [
            models.Index(fields=["sigla"]),
        ]

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class SensorFisico(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Sensor")
    sigla = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Código do Sensor",
        help_text="Código único de identificação do sensor",
    )
    descricao = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descrição Técnica",
        help_text="Especificações técnicas e características físicas",
    )
    tensao_min = models.FloatField(
        verbose_name="Tensão Mínima (V)",
        help_text="Valor mínimo de tensão elétrica em volts",
    )
    tensao_max = models.FloatField(
        verbose_name="Tensão Máxima (V)",
        help_text="Valor máximo de tensão elétrica em volts",
    )

    class Meta:
        verbose_name = "Sensor Físico"
        verbose_name_plural = "Sensores Físicos"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class TipoSensor(models.Model):
    UNIDADE_CHOICES = [
        ("°C", "Celsius"),
        ("%", "Porcentagem"),
        ("V", "Volts"),
        ("lux", "Iluminância"),
    ]

    descricao = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Tipo de Medição",
        help_text="Tipo de grandeza física medida",
    )
    limite_inferior_permitido = models.FloatField(
        verbose_name="Limite Inferior", help_text="Valor mínimo aceitável para medição"
    )
    limite_superior_permitido = models.FloatField(
        verbose_name="Limite Superior", help_text="Valor máximo aceitável para medição"
    )
    unidade = models.CharField(
        max_length=10, choices=UNIDADE_CHOICES, verbose_name="Unidade de Medida"
    )

    class Meta:
        verbose_name = "Tipo de Sensor"
        verbose_name_plural = "Tipos de Sensores"
        ordering = ["descricao"]

    def __str__(self):
        return f"{self.descricao} ({self.unidade})"


class SensorLogico(models.Model):
    sensor_fisico = models.ForeignKey(
        SensorFisico,
        on_delete=models.CASCADE,
        related_name="sensores_logicos",
        verbose_name="Hardware Associado",
    )
    tipo_sensor = models.ForeignKey(
        TipoSensor,
        on_delete=models.CASCADE,
        related_name="sensores_tipo",
        verbose_name="Configuração de Medição",
    )
    descricao = models.CharField(
        max_length=50,
        verbose_name="Identificação do Sensor",
        help_text="Nome lógico/nomeação do sensor no sistema",
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, verbose_name="Última Atualização"
    )

    class Meta:
        verbose_name = "Sensor Lógico"
        verbose_name_plural = "Sensores Lógicos"
        ordering = ["sensor_fisico__nome", "descricao"]
        unique_together = ["sensor_fisico", "descricao"]

    def __str__(self):
        return f"{self.descricao} ({self.sensor_fisico.sigla})"


class Parametro(models.Model):
    sensor_logico = models.ForeignKey(
        SensorLogico,
        on_delete=models.CASCADE,
        related_name="parametros",
        verbose_name="Sensor Associado",
    )
    nome = models.CharField(
        max_length=50,
        verbose_name="Parâmetro Monitorado",
        help_text="Nome do parâmetro de configuração",
    )
    valor = models.FloatField(
        verbose_name="Valor Configurado",
        help_text="Valor de referência para o parâmetro",
    )

    class Meta:
        verbose_name = "Parâmetro de Operação"
        verbose_name_plural = "Parâmetros de Operação"
        ordering = ["sensor_logico", "nome"]
        unique_together = ["sensor_logico", "nome"]

    def __str__(self):
        return f"{self.nome}: {self.valor} ({self.sensor_logico})"


class Leitura(models.Model):
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name="leituras",
        verbose_name="Local de Medição",
    )
    data_hora = models.DateTimeField(
        verbose_name="Data e Hora da Medição", db_index=True
    )

    class Meta:
        verbose_name = "Leitura Ambiental"
        verbose_name_plural = "Leituras Ambientais"
        ordering = ["-data_hora"]
        indexes = [
            models.Index(fields=["data_hora"]),
        ]

    def __str__(self):
        return f"Leitura em {self.sala.sigla} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"


class LeituraSensor(models.Model):
    sensor_logico = models.ForeignKey(
        SensorLogico,
        on_delete=models.CASCADE,
        related_name="leituras_sensor",
        verbose_name="Sensor",
    )
    leitura = models.ForeignKey(
        Leitura,
        on_delete=models.CASCADE,
        related_name="leituras_sensores",
        verbose_name="Leitura Associada",
    )
    valor = models.FloatField(
        verbose_name="Valor Medido",
        validators=[MinValueValidator(-1000), MaxValueValidator(1000)],
    )

    class Meta:
        verbose_name = "Leitura de Sensor"
        verbose_name_plural = "Leituras de Sensores"
        ordering = ["leitura__data_hora"]
        unique_together = ["sensor_logico", "leitura"]

    def __str__(self):
        return f"{self.sensor_logico}: {self.valor}{self.sensor_logico.tipo_sensor.unidade}"
