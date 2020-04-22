# This is a fairly standard Django settings file, with some special additions
# that allow addon applications to auto-configure themselves. If it looks
# unfamiliar, please see our documentation:
#
#   http://docs.divio.com/en/latest/reference/configuration-settings-file.html
#
# and comments below.


# INSTALLED_ADDONS is a list of self-configuring Divio Cloud addons - see the
# Addons view in your project's dashboard. See also the addons directory in
# this project, and the INSTALLED_ADDONS section in requirements.in.
from cms import constants

INSTALLED_ADDONS = [
    # Important: Items listed inside the next block are auto-generated.
    # Manual changes will be overwritten.

    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'djangocms-bootstrap4',
    'djangocms-file',
    'djangocms-googlemap',
    'djangocms-history',
    'djangocms-link',
    'djangocms-picture',
    'djangocms-snippet',
    'djangocms-style',
    'djangocms-text-ckeditor',
    'djangocms-video',
    'django-filer',
    # </INSTALLED_ADDONS>
]

# Now we will load auto-configured settings for addons. See:
#
#   http://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
#
# for information about how this works.
#
# Note that any settings you provide before the next two lines are liable to be
# overwritten, so they should be placed *after* this section.

import aldryn_addons.settings

aldryn_addons.settings.load(locals())

# Your own Django settings can be applied from here on. Key settings like
# INSTALLED_APPS, MIDDLEWARE and TEMPLATES are provided in the Aldryn Django
# addon. See:
#
#   http://docs.divio.com/en/latest/how-to/configure-settings.html
#
# for guidance on managing these settings.

# To see the settings that have been applied, use the Django diffsettings
# management command.
# See https://docs.divio.com/en/latest/how-to/configure-settings.html#list

# Michelle added below here
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALLED_APPS.extend([
    # Extend the INSTALLED_APPS setting by listing additional applications here
])
TIME_ZONE = 'America/New_York'
APPEND_SLASH = True
CMS_PERMISSION = True
CMS_TOOLBAR_ANONYMOUS_ON = False
CMS_DEFAULT_X_FRAME_OPTIONS = constants.X_FRAME_OPTIONS_SAMEORIGIN
CMS_TEMPLATES = [
    ('fullwidth.html', 'Fullwidth'),
    ('full_width_banner.html', 'Fullwidth with Jumbotron'),
    ('fullwidth-narrow-margins.html', 'Fullwidth Narrow Margins'),
    ('sidebar-left.html', 'Sidebar Left'),
    ('sidebar-right.html', 'Sidebar Right'),
    ('home.html', 'Home page template'),
]
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
FILER_CANONICAL_URL = 'sharing/'
DJANGOCMS_BOOTSTRAP4_TAG_CHOICES = ['div', 'section', 'article', 'header', 'footer', 'aside']
DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 12
DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = (
    ('container', 'Container'),
    ('container-fluid', 'Fluid container'),
)
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
    ('col', 'Column'),
)
DJANGOCMS_BOOTSTRAP4_USE_ICONS = True
DJANGOCMS_BOOTSTRAP4_CAROUSEL_TEMPLATES = (
    ('default', 'Default'),
)
DJANGOCMS_BOOTSTRAP4_TAB_TEMPLATES = (
    ('default', 'Default'),
)
DJANGOCMS_BOOTSTRAP4_SPACER_SIZES = (
    ('0', '* 0'),
    ('1', '* .25'),
    ('2', '* .5'),
    ('3', '* 1'),
    ('4', '* 1.5'),
    ('5', '* 3'),
)
DJANGOCMS_BOOTSTRAP4_CAROUSEL_ASPECT_RATIOS = (
    (16, 9),
    (4, 3),
    (19, 6),
    (1, 1),
)
DJANGOCMS_BOOTSTRAP4_COLOR_STYLE_CHOICES = (
    ('primary', 'Primary'),
    ('secondary', 'Secondary'),
    ('success', 'Success'),
    ('danger', 'Danger'),
    ('warning', 'Warning'),
    ('info', 'Info'),
    ('light', 'Light'),
    ('dark', 'Dark'),
    ('custom', 'Custom'),
)
DJANGOCMS_VIDEO_ALLOWED_EXTENSIONS = ['mp4', 'webm', 'ogv']
DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
