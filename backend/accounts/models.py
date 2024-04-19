from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, max_length=255)  # Especificando max_length
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    
# Para evitar o erro de texto muito longo, fazer o seguinte:

    # No terminal, digitar: python manage.py makemigrations --empty nome_aplicativo
    # Na pasta do aplicativo, subpasta migrations, abrir o arquivo mais recente



