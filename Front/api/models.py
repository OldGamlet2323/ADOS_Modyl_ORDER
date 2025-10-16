from django.db import models

class DutyOfficer(models.Model):
    position = models.CharField(max_length=100, verbose_name="Посада")
    rank = models.CharField(max_length=100, verbose_name="Звання")
    full_name = models.CharField(max_length=255, verbose_name="П.І.Б.")
    weapon_number = models.CharField(max_length=50, blank=True, verbose_name="Номер зброї")

    def __str__(self):
        return self.full_name

class DutyPark(models.Model):
    position = models.CharField(max_length=100, verbose_name="Посада")
    rank = models.CharField(max_length=100, verbose_name="Звання")
    full_name = models.CharField(max_length=255, verbose_name="П.І.Б.")

    def __str__(self):
        return self.full_name
class DutyDinigRoom(models.Model):
    position = models.CharField(max_length=100, verbose_name="Посада")
    rank = models.CharField(max_length=100, verbose_name="Звання")
    full_name = models.CharField(max_length=255, verbose_name="П.І.Б.")

    def __str__(self):
        return self.full_name
