from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core import serializers


from django.contrib.contenttypes.models import ContentType

from .models import Host, HostGroup
from apps.variables.models import SimpleVariableValue, GroupVariableValue, GroupVariableItemValue

import json

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
