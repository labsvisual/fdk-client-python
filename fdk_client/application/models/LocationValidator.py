"""Class Validators."""

from marshmallow import fields
from ..models.BaseSchema import BaseSchema


class LocationNestedSchema(BaseSchema):
    longitude = fields.Str(required=False)
    latitude = fields.Str(required=False)


class LocationValidator:

    class validateLocationObj(BaseSchema):
        pincode = fields.Str(required=True)
        country = fields.Str(required=True)
        city = fields.Str(required=False)
        location = fields.Nested(LocationNestedSchema, required=False)
