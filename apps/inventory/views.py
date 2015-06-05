from django.views.generic import RedirectView, TemplateView
from django.http import HttpResponse
from .models import Host, HostGroup, HostSimpleVarValue, HostGroupVarValue, HostGroupVarItemValue, HostGroupSimpleVarValue, HostGroupGroupVarValue, HostGroupGroupVarItemValue

import json

class HostRedirView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        (host, created) = Host.objects.get_or_create(name=kwargs['host_name'])
        url = '/admin/inventory/host/%s' % host.pk
        return url


class InventoryView(TemplateView):
    def get(self, request, **kwargs):
        inventory = dict()
        for hg in HostGroup.objects.all():
            # hosts in hostgroup
            hg_hosts = Host.objects.filter(hostgroup=hg)
            hosts = [host.name for host in hg_hosts]

            # hostgroup vars
            hostgroup_vars = dict()
            for hggvv in HostGroupGroupVarValue.objects.filter(hostgroup=hg):
                groupvar = dict()
                for hggviv in HostGroupGroupVarItemValue.objects.filter(group=hggvv):
                    if hggviv.value:
                        groupvar[hggviv.item.name] = hggviv.value
                if hggvv.var.name in hostgroup_vars:
                    if type(hostgroup_vars[hggvv.var.name]) != list:
                        hostgroup_vars[hggvv.var.name] = [ hostgroup_vars[hggvv.var.name] ]
                    hostgroup_vars[hggvv.var.name].append(groupvar)
                else:
                    hostgroup_vars[hggvv.var.name] = groupvar

            for hgsvv in HostGroupSimpleVarValue.objects.filter(hostgroup=hg):
                if hgsvv.var.name in hostgroup_vars:
                    if type(hostgroup_vars[hgsvv.var.name]) != list:
                        hostgroup_vars[hgsvv.var.name] = [ hostgroup_vars[hgsvv.var.name] ]
                    hostgroup_vars[hgsvv.var.name].append(hgsvv.value)
                else:
                    hostgroup_vars[hgsvv.var.name] = hgsvv.value

            inventory[hg.name] = { 'hosts' : hosts, 'vars' : hostgroup_vars }

        if 'all' not in inventory:
            inventory['all'] = { 'hosts' : list() }

        meta = {}
        for host in Host.objects.all():
            host_meta = dict()
            for hgvv in HostGroupVarValue.objects.filter(host=host):
                groupvar = dict()
                for hgviv in HostGroupVarItemValue.objects.filter(group=hgvv):
                    if hgviv.value:
                        groupvar[hgviv.item.name]  = hgviv.value
                if hgvv.var.name in host_meta:
                    if type(host_meta[hviv.var.name]) != list:
                        host_meta[hviv.var.name] = [ host_meta[hviv.var.name] ]
                    host_meta[hviv.var.name].append(groupvar)
                else:
                    host_meta[hviv.var.name] = groupvar
            for hsvv in HostSimpleVarValue.objects.filter(host=host):
                if hsvv.var.name in host_meta:
                    if type(host_meta[hsvv.var.name]) != list:
                        host_meta[hsvv.var.name] = [ host_meta[hsvv.var.name] ]
                    host_meta[hsvv.var.name].append(hsvv.value)
                else:
                    host_meta[hsvv.var.name] = hsvv.value
            if len(host_meta) > 0:
                meta[host.name] = host_meta
            if host.name not in inventory['all']['hosts']:
                inventory['all']['hosts'].append(host.name)

        inventory['_meta'] = { 'hostvars' : meta }
        return HttpResponse(json.dumps(inventory, indent=2), content_type='application/json', status=200)
        
