from django.contrib import admin
from .models import  qasession, question, answer, comment

# Register your models here.

admin.site.register(qasession)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(comment)
