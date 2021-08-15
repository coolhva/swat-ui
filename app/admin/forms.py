from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms import (PasswordField, SubmitField, HiddenField,
                     BooleanField, StringField, TextAreaField)
from wtforms.validators import DataRequired


class AdminLoginForm(FlaskForm):
    admintoken = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class SAMLSettingsForm(FlaskForm):
    id = HiddenField()
    strict = BooleanField('Strict')
    debug = BooleanField('Debug')
    sp_entityId = StringField('EntityID', validators=[DataRequired()])
    sp_assertionConsumerService_url = StringField(
        'Assertion ConsumerService URL', validators=[DataRequired()])
    sp_assertionConsumerService_binding = StringField(
        'Assertion Consumer Service Binding', validators=[DataRequired()])
    sp_singleLogoutService_url = StringField(
        'Single Logout Service URL', validators=[DataRequired()])
    sp_singleLogoutService_binding = StringField(
        'Single Logout Service Binding', validators=[DataRequired()])
    sp_NameIDFormat = StringField('NameIDFormat', validators=[DataRequired()])
    sp_x509cert = TextAreaField('SP x509 Certificate')
    sp_privateKey = TextAreaField('SP Private Key')
    idp_entityId = StringField('IDP EntityID', validators=[DataRequired()])
    idp_singleSignOnService_url = StringField(
        'IDP Single SignOn Service URL', validators=[DataRequired()])
    idp_singleSignOnService_binding = StringField(
        'IDP Single SignOn Service Binding', validators=[DataRequired()])
    idp_singleLogoutService_url = StringField(
        'IDP Single Logout Service URL', validators=[DataRequired()])
    idp_singleLogoutService_binding = StringField(
        'IDP Single Logout Service Binding', validators=[DataRequired()])
    idp_x509cert = TextAreaField(
        'IDP x509 Certificate', validators=[DataRequired()])
    idp_lowercase_urlencoding = BooleanField('Lowercase URL Encoding')
    security_signatureAlgorithm = StringField(
        'Signature Algorithm', validators=[DataRequired()])
    security_digestAlgorithm = StringField(
        'Digest Algorthm', validators=[DataRequired()])
    swatui_approval_group = StringField(
        'SWAT UI Approval group', validators=[DataRequired()])
    submit = SubmitField('Update settings')
