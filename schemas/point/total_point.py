from marshmallow import Schema, EXCLUDE, fields
from lib import ObjectIdField

class TotalPointSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    user_address = fields.Str(required=True)


