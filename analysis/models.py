from django.db import models


class FileUpload(models.Model):
    content = models.FileField(upload_to="")