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
    max_num = 0

class HostGroupAdmin(NestedModelAdmin):
    inlines = [ HostGroupSimpleVarValueInline, HostGroupGroupVarValueInline, ]

# Host Section
class HostGroupVarItemValueInline(NestedTabularInline):
    model = HostGroupVarItemValue
    extra = 0
    max_num = 0
    can_delete = False

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(HostGroupVarItemValueInline, self).get_formset(request, obj, **kwargs)
        if obj:
            formset.form.base_fields['item'].widget.widget.attrs = { 'readonly' : 'True', 'disabled' : 'True' }
        return formset
    
class HostGroupVarValueInline(NestedTabularInline):
    model = HostGroupVarValue
    inlines = [HostGroupVarItemValueInline, ]
    extra = 0
    can_change = False

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(HostGroupVarValueInline, self).get_formset(request, obj, **kwargs)
        print formset.form.base_fields
        #if obj:
        #    formset.form.base_fields['var'].widget.widget.attrs = { 'readonly' : 'True', 'disabled' : 'True' }
        return formset
   
class HostSimpleVarValueInline(NestedTabularInline):
    model = HostSimpleVarValue

class HostAdmin(NestedModelAdmin):
    inlines = [ HostSimpleVarValueInline, HostGroupVarValueInline, ]
    pass


admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
