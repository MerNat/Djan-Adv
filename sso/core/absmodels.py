from django.db import models


class DateTimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    
    class Meta:
        abstract = True