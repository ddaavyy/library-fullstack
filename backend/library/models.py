from django.db import models

# Create your models here.
class LivrosModel(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=40)
    data_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome