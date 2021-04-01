from django.db import models


class Feedback(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mail_id=models.EmailField()
    country=models.CharField(max_length=30)
    feedback=models.TextField()
