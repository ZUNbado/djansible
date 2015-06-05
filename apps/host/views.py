from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core import serializers


from django.contrib.contenttypes.models import ContentType

from .models import Host, HostGroup
from apps.variables.models import SimpleVariableValue, GroupVariableValue, GroupVariableItemValue

import json

def getvars_from_object(obj):
    obj_type = ContentType.objects.get_for_model(obj)
    variables = {}
    for sv in SimpleVariableValue.objects.filter(host_id = obj.pk, host_type = obj_type):
        if sv.variable.name in variables:
            if type(variables[sv.variable.name]) != list:
                variables[sv.variable.name] = [ variables[sv.variable.name] ]
            variables[sv.variable.name].append(sv.value)
        else:
            variables[sv.variable.name] = sv.value
    for gv in GroupVariableValue.objects.filter(host_id = obj.pk, host_type = obj_type):
        groupvar = {}
        for gvv in GroupVariableItemValue.objects.filter(group = gv):
            if gvv.value:
                groupvar[gvv.variable.name] = gvv.value

        if gv.variable.name in variables:
            if type(variables[gv.variable.name]) != list:
                variables[gv.variable.name] = [ variables[gv.variable.name] ]
            variables[gv.variable.name].append(groupvar)
        else:
            variables[gv.variable.name] = groupvar

    return variables


class InventoryView(TemplateView):
    def get(self, request, **kwargs):
        inventory = {}
        for hg in HostGroup.objects.all():
            # hosts for group
            hg_hosts = Host.objects.filter(hostgroup=hg)
            hosts = [host.name for host in hg_hosts]
            inventory[hg.name] = { 'hosts' : hosts, 'vars' : getvars_from_object(hg) }

        if 'all' not in inventory:
            inventory['all'] = { 'hosts' : list() }

        meta = {}
        for host in Host.objects.all():
            meta[host.name] = getvars_from_object(host)
            if host.name not in inventory['all']['hosts']:
                inventory['all']['hosts'].append(host.name)
        inventory['_meta'] = { 'hostvars' : meta }

        return HttpResponse(json.dumps(inventory, indent=2), content_type='application/json', status=200)

class HostCheckView(TemplateView):
    def get(self, request, host_name, **kwargs):
        (host, created) = Host.objects.get_or_create(name=host_name)
        return HttpResponse(json.dumps({'name': host.name, 'created' : created }), content_type='application/json', status=200)


class HostView(TemplateView):
    def get(self, request, host_id=None, **kwargs):
        if host_id:
            hosts = Host.objects.filter(pk=host_id)
        else:
            hosts = Host.objects.all()

        return_hosts = []
        for host in hosts:
            simplevars = []
            for sv in SimpleVariableValue.objects.filter(host_type = ContentType.objects.get_for_model(host), host_id = host.pk):
                simplevars.append({ sv.variable.name : sv.value })

            grouppedvars = []
            for gv in GroupVariableValue.objects.filter(host_type = ContentType.objects.get_for_model(host), host_id = host.pk):
                groupvars = {}
                for gvv in GroupVariableItemValue.objects.filter(group = gv):
                    groupvars[gvv.variable.name] = gvv.value

                if len(groupvars) > 0:
                    grouppedvars.append({ gv.variable.name : groupvars})

            return_hosts.append({
                    'host' : host.name,
                    'vars' : simplevars + grouppedvars,
                    })

        return HttpResponse(return_hosts, content_type='application/json', status=200)
