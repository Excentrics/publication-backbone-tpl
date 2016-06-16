# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FluentPagesConfig(AppConfig):
    name = 'fluent_pages'
    verbose_name = _('Fluent pages')


class FormDesignerConfig(AppConfig):
    name = 'form_designer'
    verbose_name = _('Form designer')


class ConstanceConfig(AppConfig):
    name = 'constance'
    verbose_name = _('Addition settings')


