"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PhoneProperties import PhoneProperties


class PhoneSchema(BaseSchema):
    # Content swagger.json

    
    active = fields.Boolean(required=False)
    
    phone = fields.List(fields.Nested(PhoneProperties, required=False), required=False)
    

