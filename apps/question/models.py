from django.db import models

from apps.form.models import Form

QUESTION_TYPE = (
    ('input', 'input'),
    ('textarea', 'textarea'),
    ('select', 'select '),
)


class Question(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name='вопрос'
    )
    is_required = models.BooleanField(
        default=False
    )
    type = models.CharField(
        choices=QUESTION_TYPE,
        max_length=20,
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='question',
        verbose_name='форма',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return f"{self.id}--{self.question}--{self.form.id}(id формы)"


class Select(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='select'
    )
    select = models.CharField(
        max_length=100,
        verbose_name='вариант'
    )
    is_false = models.BooleanField(
        default=False,
        verbose_name='верный ответ или нет?'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'вариант'
        verbose_name_plural = 'варианты'

    def __str__(self):
        return f"{self.id}--{self.select}--{self.question.question}"


class SelectAnswer(models.Model):
    select = models.ForeignKey(
        Select,
        on_delete=models.CASCADE,
        related_name='select_answers'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='question_select_answers'
    )

    def __str__(self):
        return f"{self.select.select}---{self.question.question}"


class Answer(models.Model):
    input = models.CharField(
        max_length=500,
        verbose_name='строка',
        blank=True, null=True
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answer',
        verbose_name="вопрос"
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return f"{self.id}--{self.question.question}"
