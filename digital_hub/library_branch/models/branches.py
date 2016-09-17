from __future__ import unicode_literals
from django.utils.six.moves.builtins import str
from django.utils.six import with_metaclass
from django.db import models
from django.utils.translation import ugettext_lazy as _
# -*- coding: utf-8 -*-


class Branch(models.Model):
    class Meta(object):
        verbose_name = _('branch')
        verbose_name_plural = _('branches')
        app_label = 'library_branch'

    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)
