import re

from django.core.validators import RegexValidator
from django.db import models

from mask_project.utilities import validate_phone_number

alphanum_pattern = re.compile(
    r'^[A-Za-z0-9\(\)\/\-@_&#:,\.\?!\s\']*$'
)
alphanumeric = RegexValidator(
    alphanum_pattern,
    'Only letters, numbers, spaces and '
    '&#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;'
    '&#58;&#44;&#46;&#33;&#63; are allowed here.'
)


class DonationRequestModel(models.Model):
    """Define database fields the form will be stored in."""
    requesting_organization_name = models.CharField(
        max_length=100,
        validators=[alphanumeric],
        verbose_name="Requesting Organization Name",
        help_text="What organization is in need of masks?"
    )
    drop_off_address = models.CharField(
        max_length=100,
        validators=[alphanumeric],
        verbose_name="Drop off location street address",
        help_text="Street address donated masks should be delivered to."
    )
    drop_off_city = models.CharField(
        max_length=25,
        validators=[alphanumeric],
        verbose_name="Drop off location city",
        help_text="City to delivered to, help people with GPS devices find you."
    )
    drop_off_zip_code = models.CharField(
        max_length=10,
        validators=[alphanumeric],
        help_text="Drop off location zip code"
    )
    drop_off_instructions = models.TextField(
        max_length=1000,
        verbose_name="Drop off instructions",
        help_text="Where should a person leave donated masks when they get to the drop off location?"
    )
    drop_off_times = models.TextField(
        max_length=1000,
        validators=[alphanumeric],
        verbose_name="Drop off times",
        help_text="What days / times are people able to drop off masks?"
    )
    shaped_masks = models.BooleanField(default=False)
    rectangular_masks = models.BooleanField(default=False)
    custom_pattern_url = models.URLField(
        verbose_name="URL to custom pattern for needed for donation",
        null=True,
        blank=True
    )
    scrub_caps = models.BooleanField(default=False)
    quantity_needed = models.CharField(
        max_length=30,
        validators=[alphanumeric],
        verbose_name="Quantity of item requested needed",
        help_text="How many are really needed?"
    )
    contact_first_name = models.CharField(
        max_length=30,
        verbose_name="Contact first name",
        validators=[alphanumeric]
    )
    contact_last_name = models.CharField(
        max_length=30,
        verbose_name="Contact last name",
        validators=[alphanumeric]
    )
    contact_email = models.EmailField(
        verbose_name="Contact email",
        max_length=255
    )
    contact_phone_number = models.CharField(
        verbose_name="Contact phone number",
        max_length=10,
        blank=True,
        null=True,
        validators=[validate_phone_number]
    )
    time_submitted = models.DateTimeField(auto_now_add=True)
    responded_to = models.BooleanField(
        default=False,
        help_text="For optional internal use"
    )

    class Meta:
        db_table = 'donation_requests'
        verbose_name_plural = 'Donation Requests'
        ordering = ['time_submitted', 'responded_to']

    def __str__(self):

        return self.time_submitted.strftime('%Y-%m-%d %I:%M %p')
