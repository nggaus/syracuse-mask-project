import re

import bleach
from django.core.exceptions import ValidationError

alphanum_pattern = re.compile(
    r'^[A-Za-z0-9\(\)\/\-@_&#:,\.\?!\s\']*$'
)
email_pattern = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)


def bleachinput(user_input):

    if user_input is not None and user_input != '':
        user_input = bleach.clean(
            user_input,
            tags=[],
            attributes={},
            styles=[],
            strip=True,
            strip_comments=True)

    return user_input


def clean_number(given_value):
    return_value = None

    if given_value:
        given_value = str(given_value)
        given_value = given_value.strip("' ")
        numbers_only = [x for x in given_value if x.isdigit()]
        return_value = ''.join(numbers_only)

    return return_value


def clean_phone_number(value):
    return_number = None

    if value:

        if value != 0 and value != '0':
            value = clean_number(value)

            if value and len(value) >= 10:
                return_number = str(value[:10])

    return return_number


def clean_zip(zipcode):
    """Return a valid US zip or None."""
    return_zip = None

    if zipcode:
        zipcode = zipcode.strip("' ")

        # First get only the alphanumeric characters out of the current value
        alphanums = alphanum_pattern.sub('', zipcode)
        zlen = len(alphanums)

        if zlen == 5:

            # potential US zipcode
            all_nums = clean_number(alphanums)

            if all_nums and len(all_nums) == 5 and all_nums != '00000':
                return_zip = all_nums

        elif zlen == 9:

            # potential US zipcode plus four
            all_nums = clean_number(alphanums)

            if all_nums and len(all_nums) == 9 and all_nums != '000000000':
                return_zip = '%s-%s' % (all_nums[0:5], all_nums[5:9])

    return return_zip


def validate_phone_number(value):
    """Returns string containing 10 digit phone number or raises a validation error."""
    return_number = clean_phone_number(value)

    if not return_number:
        raise ValidationError('Please enter a valid phone number with area code.')

    return return_number


def validate_zip(zipcode):
    """Return US or Canadian postal code properly formatted or raise a validation error."""
    return_zip = clean_zip(zipcode)

    if not return_zip:
        raise ValidationError('Enter a valid US or Canadian zip or postal code.')

    return return_zip
