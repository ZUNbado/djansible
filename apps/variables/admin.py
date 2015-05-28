from django.contrib import admin
from .models import VariableType, GroupVariableItems, GroupVariable, SimpleVariable, SimpleVariableValue


class GroupVariableItemsInline(admin.TabularInline):
    model = GroupVariableItems
    extra = 1

class GroupVariableAdmin(admin.ModelAdmin):
    inlines = [ GroupVariableItemsInline, ]

admin.site.register(VariableType)
admin.site.register(GroupVariable, GroupVariableAdmin)
admin.site.register(SimpleVariable)
admin.site.register(SimpleVariableValue)
