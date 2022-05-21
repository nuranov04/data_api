from django.db import models

import uuid


class Form(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название формы'
    )
    description = models.TextField(
        verbose_name='описание формы'
    )
    form_uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
    )
    create_at = models.DateField(
        auto_now_add=True
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = 'форма'
        verbose_name_plural = 'формы'

    def __str__(self):
        return f"{self.id}--{self.title}"
