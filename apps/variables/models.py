from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class VariableType(models.Model):
    name = models.CharField(max_length=255)
    validator = models.CharField(max_length=255)

    def __unicode__(self): return u'%s' % self.name


class SimpleVariable(models.Model):
    name = models.CharField(max_length=255)
    variabletype = models.ForeignKey(VariableType)

    def __unicode__(self): return u'%s' % self.name

class GroupVariable(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self): return u'%s' % self.name

class GroupVariableItems(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(GroupVariable)
    variabletype = models.ForeignKey(VariableType)
    
    def __unicode__(self): return u'%s' % ( self.name )


class SimpleVariableValue(models.Model):
    host_type = models.ForeignKey(ContentType)
    host_id = models.PositiveIntegerField()
    host_object = GenericForeignKey('host_type', 'host_id')
    variable = models.ForeignKey(SimpleVariable)
    value = models.CharField(max_length=255, null = True, blank = True)

class GroupVariableValue(models.Model):
    host_type = models.ForeignKey(ContentType)
    host_id = models.PositiveIntegerField()
    host_object = GenericForeignKey('host_type', 'host_id')
    variable = models.ForeignKey(GroupVariable)

    def __unicode__(self): return u'%s / %s' % ( self.pk, self.variable )


class GroupVariableItemValue(models.Model):
    host_type = models.ForeignKey(ContentType)
    host_id = models.PositiveIntegerField()
    host_object = GenericForeignKey('host_type', 'host_id')
    group = models.ForeignKey(GroupVariableValue)
    variable = models.ForeignKey(GroupVariableItems)
    value = models.CharField(max_length=255, null = True, blank = True)

    def __unicode__(self): return u'%s / %s / %s' % ( self.pk, self.group, self.variable )
