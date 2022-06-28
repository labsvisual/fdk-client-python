"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetPincodeZonesResponse(BaseSchema):
    # Logistic swagger.json

    
    zones = fields.List(fields.Raw(required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    

