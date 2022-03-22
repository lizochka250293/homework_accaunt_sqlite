from django.contrib import admin
from .models import Accaunt
# Register your models here.

class AccauntAdmin(admin.ModelAdmin):
    list_display = ['login', 'status', 'created_at']
    list_editable = ['status']
    ordering = ["login"]
    list_per_page = 10
    search_fields = ['login']

admin.site.register(Accaunt, AccauntAdmin)


# Register your models here.
