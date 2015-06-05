from django.db import models


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
