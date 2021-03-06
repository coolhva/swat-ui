"""add SAML settings

Revision ID: 9789ddd4112b
Revises: 
Create Date: 2021-08-15 15:26:45.711588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9789ddd4112b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    saml_table = op.create_table('samlsettings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strict', sa.Boolean(), nullable=True),
    sa.Column('debug', sa.Boolean(), nullable=True),
    sa.Column('sp_entityId', sa.Text(), nullable=True),
    sa.Column('sp_assertionConsumerService_url', sa.Text(), nullable=True),
    sa.Column('sp_assertionConsumerService_binding', sa.Text(), nullable=True),
    sa.Column('sp_singleLogoutService_url', sa.Text(), nullable=True),
    sa.Column('sp_singleLogoutService_binding', sa.Text(), nullable=True),
    sa.Column('sp_NameIDFormat', sa.Text(), nullable=True),
    sa.Column('sp_x509cert', sa.Text(), nullable=True),
    sa.Column('sp_privateKey', sa.Text(), nullable=True),
    sa.Column('idp_entityId', sa.Text(), nullable=True),
    sa.Column('idp_singleSignOnService_url', sa.Text(), nullable=True),
    sa.Column('idp_singleSignOnService_binding', sa.Text(), nullable=True),
    sa.Column('idp_singleLogoutService_url', sa.Text(), nullable=True),
    sa.Column('idp_singleLogoutService_binding', sa.Text(), nullable=True),
    sa.Column('idp_x509cert', sa.Text(), nullable=True),
    sa.Column('idp_lowercase_urlencoding', sa.Boolean(), nullable=True),
    sa.Column('security_signatureAlgorithm', sa.Text(), nullable=True),
    sa.Column('security_digestAlgorithm', sa.Text(), nullable=True),
    sa.Column('swatui_approval_group', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    op.bulk_insert(
        saml_table,
        [
            {
                'id':1,
                'strict': True,
                'debug': True,
                'sp_entityId': 'http://flask.app/swat-ui',
                'sp_assertionConsumerService_url': 'http://localhost:8000/auth/?acs',
                'sp_assertionConsumerService_binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
                'sp_singleLogoutService_url': 'http://localhost:8000/auth/?sls',
                'sp_singleLogoutService_binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
                'sp_NameIDFormat': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
                'sp_x509cert': '',
                'sp_privateKey': '',
                'idp_entityId': 'https://sts.windows.net/724c9322-40b4-4983-8062-811993755e4e/',
                'idp_singleSignOnService_url': 'https://login.microsoftonline.com/724c9322-40b4-4983-8062-811993755e4e/saml2',
                'idp_singleSignOnService_binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
                'idp_singleLogoutService_url': 'https://login.microsoftonline.com/724c9322-40b4-4983-8062-811993755e4e/saml2',
                'idp_singleLogoutService_binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
                'idp_x509cert': 'MIIC8DCCAdigAwIBAgIQb2btNjMBe5RDwIrqyOtTdDANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMTA4MTIyMDEyMTBaFw0yNDA4MTIyMDEyMTBaMDQxMjAwBgNVBAMTKU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnRpZmljYXRlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuaKO4218ayfA6xL+K8xY3mAf5vAPXSHnpA2WO20xcD3pY9nPGZf8lZpgtcu5kZd55I1zMEZXf7+qdHC/mkE/HtXLa+BeYMk7Smgld0FuyLb3r1KsXrgHSkS+xojtDeraTduJjIrBuZiB8eLHkblkR7+zfoGgouOD9vYE43CxA+YgOlbs0aJXXRQqvUNTNC3vsim9FMF1/o3TNXK3aznfh2CfsybZ8pfRUk7diqWWI2ZwRHpQ5cRo4RPmTDTSf68vilX+LfEuu06Tqaa0Xm/jGp8J9KF1nPIfAHfc31ns2Dwu0HP6kNhR7EL/WD4b7W+9eoHGUI67Axfe+r8in7qESQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAo8CDqb+dmlQrDhvEj+ni5nX1vZisPqYIoG2LOHYXsPBduEfn1n6DaD6SYRcJ1pG7Jk9WxG/WV6Il6owPvDVO/JXSRkTJ6Nm0usJCgqON0+W2zRLyqM6N4whGM8rv87PfcFQbj/0O0uCNnRENNMT1UrlzGTXLwg6kvBT/zG0M+8w/yRvszO6cZU/hDzSYR09/uorqxXwoeAU8H8+0hqCt+P7YUFiYXUKK64WlWLUzZWYuEaqZzXwPP4DYHCg0HGiKWy+9lwHI9H0euKtwMbAC3v0BGVJ5UO837t8GsCq/i4YcAHYAMxUKJrClqQvx4bG9fnUlsAbw9pxyyzwLz7Rsn',
                'idp_lowercase_urlencoding': True,
                'security_signatureAlgorithm': 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
                'security_digestAlgorithm': 'http://www.w3.org/2001/04/xmlenc#sha256',
                'swatui_approval_group': '4ecafcf3-54f6-487c-a6e7-997d60e5b55c'
            }
        ]
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('samlsettings')
    # ### end Alembic commands ###
