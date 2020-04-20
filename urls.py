# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.urls import path

urlpatterns = [
    url(r'^masks/', include('mask_project.urls', namespace='mask_project')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
