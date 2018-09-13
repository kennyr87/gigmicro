from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired, Length, URL

class uploadJournal(FlaskForm):
    """
    Form to upload journals
    """
    journal_name    = StringField('journal_name', validators=[
        InputRequired("Journal's name is required"),
        Length(min=1, max=127, message='Field must be less than 127 characters')
    ])
    journal_url     = StringField('journal_url', validators=[
        URL(require_tld=True, message='Must be a valid URL')
        Length(max=255, message='Field must be less than 255 characters')
    ])
    issn_print      = StringField('issn_print')
    issn_online     = StringField('issn_online')

class uploadForm(FlaskForm):
    """
    Form to upload articles
    """
    article_name    = StringField()
    publish_date    = DateField()

    # need to be able to input multiple authors
    first_name      = StringField()
    middle_initial  = StringField()
    last_name       = StringField()

    article_url     = StringField()
