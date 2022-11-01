from django.contrib import admin
from chats.models import Chat, Message


class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'author')
    list_filter = ('author',)
    row_id_fields = ('author',)
    list_editable = ('kind',)
    search_fields = ('name', 'author')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sent_from', 'message', 'created_at')
    list_filter = ('chat', 'sent_from',)
    row_id_fields = ('sent_from',)
    search_fields = ('chat', 'sent_from',)


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)