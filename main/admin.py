from django.contrib import admin

# Register your models here.
from main.models import Books, Disciplines, UserDiscipline


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'discipline', 'nomer', 'link')
    list_filter = ('author', 'discipline')
    search_fields = ('author', 'name', 'nomer')


class DisciplinesAdmin(admin.ModelAdmin):
    list_filter = ('name', 'id')
    search_fields = ('name', 'id')


class UserDisciplineAdmin(admin.ModelAdmin):
    list_display = ('user', 'discip')
    list_filter = ('user', 'discip')
    search_fields = ('user', 'discip')


admin.site.register(Books, BookAdmin)
admin.site.register(Disciplines, DisciplinesAdmin)
admin.site.register(UserDiscipline, UserDisciplineAdmin)
