from django.contrib import admin
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['login', 'status', 'created_at']
    list_editable = ['status']
    ordering = ["login"]
    list_per_page = 10
    search_fields = ['login']

admin.site.register(Account, AccountAdmin)


# Register your models here.
