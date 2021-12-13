from django.db import models


class Pet(models.Model):
    """The model of the pet."""

    class PetClassChoices(models.TextChoices):
        DOG = "dog"
        CAT = "cat"

    name = models.CharField(
        max_length=128,
        verbose_name="Имя питомца",
    )
    age = models.IntegerField(verbose_name="Возраст")
    type = models.CharField(
        max_length=3,
        choices=PetClassChoices.choices,
        verbose_name="Вид питомца",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания записи", auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    """Model for pet photos."""

    photo = models.ImageField(
        verbose_name="Фото питомца",
        upload_to="photo/",
        blank=True,
        null=True,
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="photos")

    class Meta:
        verbose_name = "Фотография питомца"
        verbose_name_plural = "Фотографии питомца"
