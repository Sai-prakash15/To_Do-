from django.contrib import admin
from .models import ToDoList, ListItem
from .forms import ToDoListForm
# Register your models here.


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'priority','created_timestamp','modified_timestamp']
    form = ToDoListForm
    # class Meta:
    #     model = ToDoList
class ListItemAdmin(admin.ModelAdmin):
    list_display = ['to_do_list', '__str__', 'priority','created_timestamp','modified_timestamp']

admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(ListItem, ListItemAdmin)