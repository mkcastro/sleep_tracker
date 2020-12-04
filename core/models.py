from django.db import models

# Create your models here.
class Sleep(models.Model):



    class Meta:
        verbose_name = _("Sleep")
        verbose_name_plural = _("Sleeps")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Sleep_detail", kwargs={"pk": self.pk})


class Coffee(models.Model):



    class Meta:
        verbose_name = _("Coffee")
        verbose_name_plural = _("Coffees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Coffee_detail", kwargs={"pk": self.pk})

class Bed(models.Model):



    class Meta:
        verbose_name = _("Bed")
        verbose_name_plural = _("Beds")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bed_detail", kwargs={"pk": self.pk})

class Usana(models.Model):



    class Meta:
        verbose_name = _("Usana")
        verbose_name_plural = _("Usanas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Usana_detail", kwargs={"pk": self.pk})
