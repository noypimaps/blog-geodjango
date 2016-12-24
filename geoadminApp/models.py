from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
import uuid


class Features(models.Model):
    """The Features model will hold the geometry and the feature attributes.
    """
    feat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    geometry = models.GeometryField()
    attributes = JSONField()
    layer = models.ForeignKey('Layers', on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.feat_id

    class Meta:
        verbose_name_plural = "Features"

class Layers(models.Model):
    """The Layers model holds the metdata of a layer.
    """
    layername = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=30)

    def __unicode__(self):
        return self.layername

    class Meta:
        verbose_name_plural = "Layers"

