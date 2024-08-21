from django.db import models

class Cadastro(models.Model):
  username = models.CharField(max_length=50)
  password = models.IntegerField()
  confirm_password = models.IntegerField()

  def __str__(self):
    return self.username
  


