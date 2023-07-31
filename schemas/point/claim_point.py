from marshmallow import Schema, EXCLUDE, fields
from lib import ObjectIdField


class ClaimPointSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    user_address = fields.String(required=True)

