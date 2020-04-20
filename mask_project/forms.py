from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import DonationRequestModel
from .utilities import bleachinput, clean_phone_number, clean_zip


class DonationRequestForm(ModelForm):

    class Meta:
        model = DonationRequestModel
        fields = [
            "requesting_organization_name",
            "drop_off_address",
            "drop_off_city",
            "drop_off_zip_code",
            "drop_off_instructions",
            "drop_off_times",
            "shaped_masks",
            "rectangular_masks",
            "custom_pattern_url",
            "scrub_caps",
            "quantity_needed",
            "contact_first_name",
            "contact_last_name",
            "contact_email",
            "contact_phone_number"
        ]

    def clean_requesting_organization_name(self):
        requesting_organization_name = bleachinput(
            self.cleaned_data.get("requesting_organization_name")
        )

        if not requesting_organization_name:
            raise ValidationError("Name of organization requesting donations is required.")

        return requesting_organization_name.title()

    def clean_drop_off_address(self):
        drop_off_address = bleachinput(self.cleaned_data.get("drop_off_address"))

        if not drop_off_address:
            raise ValidationError("Street address people can use in their "
                                  "GPS to find your drop off location is required.")

        return drop_off_address.title()

    def clean_drop_off_city(self):
        drop_off_city = bleachinput(self.cleaned_data.get("drop_off_city"))

        if not drop_off_city:
            raise ValidationError("City people can use in their GPS to find your "
                                  "drop off location is required.")

        return drop_off_city.title()

    def clean_drop_off_zip_code(self):
        drop_off_zip_code = self.cleaned_data.get("drop_off_zip_code")

        if drop_off_zip_code:
            drop_off_zip_code = clean_zip(drop_off_zip_code)
        else:
            raise ValidationError("A zip code people can use in their GPS to "
                                  "find your drop off location is required.")

        return drop_off_zip_code

    def clean_drop_off_instructions(self):
        drop_off_instructions = bleachinput(
            self.cleaned_data.get("drop_off_instructions")
        )

        if not drop_off_instructions:
            raise ValidationError("Please enter instructions so people know what "
                                  "to do and where to leave their donated items "
                                  "when they arrive.")

        return drop_off_instructions

    def clean_drop_off_times(self):
        drop_off_times = bleachinput(
            self.cleaned_data.get("drop_off_times")
        )

        if not drop_off_times:
            raise ValidationError("Please enter days and times when people can "
                                  "drop off donated items.")

        return drop_off_times

    def clean_contact_first_name(self):
        contact_first_name = bleachinput(
            self.cleaned_data.get("contact_first_name")
        )

        if not contact_first_name:
            raise ValidationError("First name of contact person within organization "
                                  "for questions on donations is required.")

        return contact_first_name.title()

    def clean_contact_last_name(self):
        contact_last_name = bleachinput(
            self.cleaned_data.get("contact_last_name")
        )

        if not contact_last_name:
            raise ValidationError("Last name of contact person within organization "
                                  "for questions on donations is required.")

        return contact_last_name.title()

    def clean_contact_email(self):
        contact_email = bleachinput(
            self.cleaned_data.get("contact_email")
        )

        if not contact_email:
            raise ValidationError("Email for contact person within organization "
                                  "for questions on donations is required.")

        return contact_email.lower()

    def clean_contact_phone_number(self):
        contact_phone_number = bleachinput(
            self.cleaned_data.get("contact_phone_number")
        )

        if contact_phone_number:
            contact_phone_number = clean_phone_number(contact_phone_number)

        return contact_phone_number
