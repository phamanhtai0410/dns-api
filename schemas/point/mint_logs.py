from marshmallow import Schema, EXCLUDE, fields
from lib import ObjectIdField

class MintLogsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True
    user_address = fields.String(required=True)
    ref_address = fields.String(required=True)
    letter = fields.Int(required=True)
    domain_name = fields.String(required=True)    