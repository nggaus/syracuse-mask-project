# -*- coding: utf-8 -*-
import aldryn_addons.urls
from aldryn_django.utils import i18n_patterns

urlpatterns = [
] + aldryn_addons.urls.patterns() + i18n_patterns(
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
