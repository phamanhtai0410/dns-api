from marshmallow import Schema, EXCLUDE, fields
from lib import ObjectIdField

class DefaultPointsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True
        
    level1 = fields.Int(required=True)
    point1 = fields.Int(required=True)
    level2 = fields.Int(required=True)
    point2 = fields.Int(required=True)
    level3 = fields.Int(required=True)
    point3 = fields.Int(required=True)
    level4 = fields.Int(required=True)
    point4 = fields.Int(required=True)
    default = fields.Int(required=True)
