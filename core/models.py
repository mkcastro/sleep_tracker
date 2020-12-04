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


