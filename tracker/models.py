from django.db import models
from django.contrib.auth.models import User


class PressureRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pressure_records')
    systolic = models.IntegerField()        # верхнее давление
    diastolic = models.IntegerField()       # нижнее давление
    pulse = models.IntegerField()           # пульс
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']        

    def __str__(self):
        return f"{self.user.username} — {self.systolic}/{self.diastolic} ({self.created_at:%Y-%m-%d %H:%M})"