from app import db


class SAMLsettings(db.Model):
    __tablename__ = 'samlsettings'

    id = db.Column(db.Integer, primary_key=True)
    strict = db.Column(db.Boolean)
    debug = db.Column(db.Boolean)
    sp_entityId = db.Column(db.Text)
    sp_assertionConsumerService_url = db.Column(db.Text)
    sp_assertionConsumerService_binding = db.Column(db.Text)
    sp_singleLogoutService_url = db.Column(db.Text)
    sp_singleLogoutService_binding = db.Column(db.Text)
    sp_NameIDFormat = db.Column(db.Text)
    sp_x509cert = db.Column(db.Text)
    sp_privateKey = db.Column(db.Text)
    idp_entityId = db.Column(db.Text)
    idp_singleSignOnService_url = db.Column(db.Text)
    idp_singleSignOnService_binding = db.Column(db.Text)
    idp_singleLogoutService_url = db.Column(db.Text)
    idp_singleLogoutService_binding = db.Column(db.Text)
    idp_x509cert = db.Column(db.Text)
    idp_lowercase_urlencoding = db.Column(db.Boolean)
    security_signatureAlgorithm = db.Column(db.Text)
    security_digestAlgorithm = db.Column(db.Text)
    swatui_approval_group = db.Column(db.Text)
