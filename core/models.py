from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Sleep(models.Model):
    coffee = models.ForeignKey(
        "core.Coffee",
        verbose_name=_("coffee"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    bed = models.ForeignKey(
        "core.Bed",
        verbose_name=_("bed"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    usana = models.ForeignKey(
        "core.Usana",
        verbose_name=_("usana"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Sleep")
        verbose_name_plural = _("Sleeps")

    def __str__(self):
        return f"You slept for {8} hours"

    def get_absolute_url(self):
        return reverse("Sleep_detail", kwargs={"pk": self.pk})


class Coffee(models.Model):
    name = models.TextField(_("name"), default="Folgers")

    class Meta:
        verbose_name = _("Coffee")
        verbose_name_plural = _("Coffees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Coffee_detail", kwargs={"pk": self.pk})


class Bed(models.Model):
    name = models.TextField(_("bed"), default="Uratex")

    class Meta:
        verbose_name = _("Bed")
        verbose_name_plural = _("Beds")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bed_detail", kwargs={"pk": self.pk})


class Usana(models.Model):
    name = models.TextField(_("usana"), default="Cellsentials")

    class Meta:
        verbose_name = _("Usana")
        verbose_name_plural = _("Usanas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Usana_detail", kwargs={"pk": self.pk})
