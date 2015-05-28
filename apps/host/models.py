from django.db import models
from apps.variables.models import SimpleVariable, SimpleVariableValue, GroupVariable, GroupVariableValue, GroupVariableItems, GroupVariableItemValue

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Host(models.Model):
    name = models.CharField(max_length=255)
    hostgroups = models.ManyToManyField('HostGroup', blank = True)
    variables = GenericRelation('HostVariable')

    def __unicode__(self): return u'%s' % self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=255)
    hosts = models.ManyToManyField(Host, blank = True)

    def __unicode__(self): return u'%s' % self.name


class HostVariable(models.Model):
    host_type = models.ForeignKey(ContentType, related_name='host')
    host_id = models.PositiveIntegerField()
    host_object = GenericForeignKey('host_type', 'host_id')

    var_limit = models.Q(app_label='variables', model = 'simplevariable') | models.Q(app_label='variables', model='groupvariable')
    var_type = models.ForeignKey(ContentType, related_name='variable', limit_choices_to = var_limit)
    var_id = models.PositiveIntegerField()
    var_object = GenericForeignKey('var_type', 'var_id')


    def save(self):
        model = ContentType.objects.get_for_model(self.var_object)

        if model.model == 'simplevariable':
            if not self.pk:
                SimpleVariableValue.objects.create(host_id = self.host_id, host_type = self.host_type, variable = SimpleVariable.objects.get(pk=self.var_id))
        if model.model == 'groupvariable':
            if self.pk:
                groupvariable = GroupVariableValue.objects.get(host_id = self.host_id, host_type = self.host_type, variable = GroupVariable.objects.get(pk=self.var_id) )
            else:
                groupvariable = GroupVariableValue.objects.create(host_id = self.host_id, host_type = self.host_type, variable = GroupVariable.objects.get(pk=self.var_id) )
            for var in GroupVariableItems.objects.filter(group = groupvariable.variable):
                GroupVariableItemValue.objects.get_or_create(host_id = self.host_id, host_type = self.host_type, group = groupvariable, variable = var)

        super(HostVariable, self).save()
