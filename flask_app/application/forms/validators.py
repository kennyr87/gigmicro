# -*- coding: utf-8 -*-
"""
    flask_app.application.forms.validators
    ~~~~~
    custom validators module
"""
from wtforms.validators import ValidationError, StopValidation

def check_length(length):
    """
    Validates length of fixed length field

    :param int length: Length of the field
    :return Callable that raises validation error
    """
    length      = int(length)
    message     = 'Field must be %d characters long.' % (length)

    def _length(form, field):
        l = field.data and ( len(field.data) or 0 )
        if l != length:
            raise ValidationError(message)

    return _length

class MutualInputs(object):
    """
    Validates mutually dependent inputs.

    If input is empty, removes prior errors from the field
    and validates :attr:`.field_name`.

    Args:
        field_name (str): Name of other field to validate.
        message (str, optional): Error message to raise in case of a validation error.

    """

    def __init__(self, field_name, message=None):
        self.field_name = field_name
        if message is None:
            m = field.gettext("Either {field_0} or {field_1} is required.")
            message = m.format(field_0=field.name, field_1=self.field_name)
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.field_name]
        except KeyError:
            raise ValidationError(
                field.gettext("Invalid field name '%s'.") % (self.field_name)
            )

        # strip white space
        string_check = lambda s: s.strip()

        if (
            not field.raw_data
            or isinstance(field.raw_data[0], str)
            and not string_check(field.raw_data[0])
        ):  
            try:
                other.validate(form)
            except other.errors:
                raise ValidationError(self.message)
            field.errors[:] = []
            raise StopValidation()