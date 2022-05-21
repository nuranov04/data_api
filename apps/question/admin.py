from django.contrib import admin


from apps.question.models import Question, Select, Answer, SelectAnswer


admin.site.register(Question)
admin.site.register(Select)
admin.site.register(Answer)
admin.site.register(SelectAnswer)