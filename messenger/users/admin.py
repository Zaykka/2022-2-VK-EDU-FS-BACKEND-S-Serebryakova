from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('username',)
    row_id_fields = ('username',)
    list_editable = ('bio',)
    search_fields = ('username', 'first_name', 'last_name')


admin.site.register(User)

