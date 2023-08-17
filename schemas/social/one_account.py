from marshmallow import Schema, RAISE, fields, EXCLUDE, validate

from lib import ObjectIdField, DatetimeField
from lib.enums.social import SocialNames


class OneAccountLinkedSocialFormData(Schema):
    class Meta:
        unknown = RAISE
    
    social_name = fields.String(required=True, validate=validate.OneOf([
        SocialNames.TWITTER,
        SocialNames.DISCORD,
        SocialNames.FACEBOOK,
        SocialNames.GMAIL
    ]))
    social_account = fields.String(required=True)
    # address = fields.String(required=True)


