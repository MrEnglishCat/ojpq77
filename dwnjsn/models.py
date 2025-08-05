from django.db import models
from mimesis import Datetime


class JSNUploadModel(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=Datetime(locale="ru").datetime().strftime('%Y-%m-%d_%H:%M'))