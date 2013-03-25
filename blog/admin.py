from django.contrib import admin

from blog.models import NomadPost


class NomadPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'summary')
    fields = ('bloguser', 'status', 'title', 'slug', 'category', 'summary', 'content')

admin.site.register(NomadPost, NomadPostAdmin)


