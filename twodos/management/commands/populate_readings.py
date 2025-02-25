import random
import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from twodos.models import Leitura, LeituraSensor, SensorLogico, Sala


class Command(BaseCommand):
    help = "Popula o banco de dados com leituras simuladas para os últimos 30 dias."

    def handle(self, *args, **options):
        # Recupera sensores lógicos para Temperatura e Umidade
        sensors_temperature = SensorLogico.objects.filter(
            tipo_sensor__descricao__iexact="Temperatura"
        )
        sensors_humidity = SensorLogico.objects.filter(
            tipo_sensor__descricao__iexact="Umidade"
        )

        if not sensors_temperature.exists() or not sensors_humidity.exists():
            self.stdout.write(
                self.style.ERROR(
                    "Não há sensores configurados para Temperatura ou Umidade."
                )
            )
            return

        salas = Sala.objects.all()
        if not salas.exists():
            self.stdout.write(self.style.ERROR("Nenhuma sala cadastrada."))
            return

        now = timezone.now()
        start_time = now - datetime.timedelta(days=30)  # Alterado para 30 dias
        time_cursor = start_time

        while time_cursor <= now:
            for sala in salas:
                # Cria um registro de leitura para a sala
                leitura = Leitura.objects.create(sala=sala, data_hora=time_cursor)

                # Seleciona aleatoriamente um sensor de cada tipo
                sensor_temp = random.choice(list(sensors_temperature))
                sensor_hum = random.choice(list(sensors_humidity))

                # Gera valores aleatórios
                valor_temp = round(random.uniform(10.0, 50.0), 2)
                valor_hum = round(random.uniform(20.0, 80.0), 2)

                # Cria os registros de leitura
                LeituraSensor.objects.create(
                    sensor_logico=sensor_temp, leitura=leitura, valor=valor_temp
                )
                LeituraSensor.objects.create(
                    sensor_logico=sensor_hum, leitura=leitura, valor=valor_hum
                )

            time_cursor += datetime.timedelta(hours=2)

        self.stdout.write(
            self.style.SUCCESS(
                "Banco de dados populado com leituras simuladas para os últimos 30 dias."
            )
        )
