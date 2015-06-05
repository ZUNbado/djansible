from django.contrib import admin
from .models import Host, HostGroup, HostSimpleVarValue, HostGroupVarValue, HostGroupVarItemValue, HostGroupSimpleVarValue, HostGroupGroupVarValue, HostGroupGroupVarItemValue
from grappelli_nested.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

# HostGroup Section
class HostGroupGroupVarItemValueInline(NestedTabularInline):
    model = HostGroupGroupVarItemValue
    extra = 0

class HostGroupGroupVarValueInline(NestedTabularInline):
    model = HostGroupGroupVarValue
    inlines = [HostGroupGroupVarItemValueInline, ]
    extra = 0

class HostGroupSimpleVarValueInline(NestedTabularInline):
    model = HostGroupSimpleVarValue
    extra = 0

class HostGroupAdmin(NestedModelAdmin):
    inlines = [ HostGroupSimpleVarValueInline, HostGroupGroupVarValueInline, ]

# Host Section
class HostGroupVarItemValueInline(NestedTabularInline):
    model = HostGroupVarItemValue
    extra = 0

class HostGroupVarValueInline(NestedTabularInline):
    model = HostGroupVarValue
    inlines = [HostGroupVarItemValueInline, ]
    extra = 0

class HostSimpleVarValueInline(NestedTabularInline):
    model = HostSimpleVarValue

class HostAdmin(NestedModelAdmin):
    inlines = [ HostSimpleVarValueInline, HostGroupVarValueInline, ]
    pass


admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
