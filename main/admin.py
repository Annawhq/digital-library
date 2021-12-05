from django.contrib import admin

# Register your models here.
from main.models import Books, Disciplines, UserDiscipline

admin.site.register(Books)
admin.site.register(Disciplines)
admin.site.register(UserDiscipline)
