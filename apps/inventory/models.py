from django.db import models
from apps.var.models import SimpleVariable, GroupVariable, GroupVariableItems


class Host(models.Model):
    name = models.CharField(max_length=255)
    hostgroups = models.ManyToManyField('HostGroup', blank = True)

    def __unicode__(self): return u'%s' % self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=255)
    hosts = models.ManyToManyField(Host, blank = True)

    def __unicode__(self): return u'%s' % self.name

class HostSimpleVarValue(models.Model):
    var = models.ForeignKey(SimpleVariable)
    host = models.ForeignKey(Host)
    value = models.CharField(max_length=255)

class HostGroupVarValue(models.Model):
    var = models.ForeignKey(GroupVariable)
    host = models.ForeignKey(Host)

class HostGroupVarItemValue(models.Model):
    group = models.ForeignKey(HostGroupVarValue)
    item = models.ForeignKey(GroupVariableItems)
    value = models.CharField(max_length=255)

class HostGroupSimpleVarValue(models.Model):
    var = models.ForeignKey(SimpleVariable)
    hostgroup = models.ForeignKey(HostGroup)
    value = models.CharField(max_length=255)

class HostGroupGroupVarValue(models.Model):
    var = models.ForeignKey(GroupVariable)
    hostgroup = models.ForeignKey(HostGroup)

class HostGroupGroupVarItemValue(models.Model):
    group = models.ForeignKey(HostGroupGroupVarValue)
    item = models.ForeignKey(GroupVariableItems)
    value = models.CharField(max_length=255)
