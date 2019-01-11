"""
    application.forms
    ~~~~~
    forms 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired, Length, URL, ValidationError

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

class JournalForm(FlaskForm):
    """
    Form to upload journals
    """
    journal_name    = StringField('Journal Name', validators=[
        InputRequired("Journal's name is required"),
        Length(max=127, message='Field must be less than 127 characters')
    ])
    journal_url     = StringField('URL', validators=[
        URL(require_tld=True, message='Must be a valid URL'),
        Length(max=255, message='Field must be less than 255 characters')
    ])
    issn_print      = StringField('ISSN Print', validators=[
        check_length(8)
    ])
    issn_online     = StringField('ISSN Online', validators=[
        check_length(8)
    ])

class ArticleForm(FlaskForm):
    """
    Form to upload articles
    """
    article_name    = StringField('Article Name', validators=[
        InputRequired("Article's name is required."),
        Length(max=127, message='Field must be less than 127 characters')
    ])
    # input date in mm/dd/yyyy format
    publish_date    = DateField('Publication Date', validators=[
        InputRequired("Publication date is required.")
    ])

    article_url     = StringField('URL', validators=[
        InputRequired("Article's URL is required."),
        Length(max=255, message='Field must be less than 255 characters.'),
        URL('Must be a valid URL.')
    ])

class AuthorForm(FlaskForm):
    """
    Form to upload authors.
    """
    # need to be able to input multiple authors
    first_name      = StringField('First Name', validators=[
        Length(max=31, message='Field must be less than 31 characters.')
    ])
    middle_initial  = StringField('M', validators=[
        check_length(1)
    ])
    last_name       = StringField('Last Name', validators=[
        InputRequired("Author's last name is required."),
        Length(max=31, message='Field must be less than 31 characters.')
    ])
