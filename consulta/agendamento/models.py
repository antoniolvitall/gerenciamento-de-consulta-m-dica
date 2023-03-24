from django.db import models


class Profissional(models.Model):
    matricula = models.CharField(max_length=5)
    nome = models.CharField(max_length=50)
    nomesocial = models.CharField(max_length=50)
    cns = models.CharField(max_length=15)
    CARGO = (
        ('M', 'Médico'),
        ('E', 'Enfermeiro'),
    )

    def __str__(self):
        return self.nomesocial

class Consulta(models.Model):
    data_consulta = models.DateField()
    Profissional
