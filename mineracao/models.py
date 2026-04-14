from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cnpj} - {self.razao_social}"
    
class Patente(models.Model):
    numero_registro = models.CharField(max_length=255, unique=True)
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='patentes')

    def __str__(self):
        return f"{self.numero_registro} - {self.titulo}"