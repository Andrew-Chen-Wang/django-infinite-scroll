from django.db import models


class English(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=9001)
