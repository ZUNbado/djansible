from django.contrib import admin
from .models import Host, HostGroup, HostVariable
from apps.variables.models import SimpleVariableValue, GroupVariableValue, GroupVariableItemValue
from django.contrib.contenttypes import generic


class SimpleVariableValueInline(generic.GenericTabularInline):
    model = SimpleVariableValue
    readonly_fields = [ 'variable' ]
    fields = [ 'variable', 'value' ]
    ct_field = 'host_type'
    ct_fk_field = 'host_id'
    extra = 0
    max_num = 0


class GroupVariableItemValueInline(generic.GenericTabularInline):
    model = GroupVariableItemValue
    readonly_fields = [ 'group', 'variable' ]
    fields = [ 'group', 'variable', 'value' ]
    ct_field = 'host_type'
    ct_fk_field = 'host_id'
    extra = 0
    max_num = 0
    related_lookup_fields = {
            'generic': [['host_type', 'host_id'], ['var_type', 'var_id']],
            }

class HostVariableInline(generic.GenericTabularInline):
    model = HostVariable
    ct_field = 'host_type'
    ct_fk_field = 'host_id'
    extra = 0

    related_lookup_fields = {
            'generic': [['host_type', 'host_id'], ['var_type', 'var_id']],
            }

class HostAdmin(admin.ModelAdmin):
    inlines = [ HostVariableInline, SimpleVariableValueInline, GroupVariableItemValueInline ]



class HostGroupAdmin(admin.ModelAdmin):
    inlines = [ HostVariableInline, SimpleVariableValueInline, GroupVariableItemValueInline ]

admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
