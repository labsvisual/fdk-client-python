"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class TicketAsset(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in TicketAssetTypeEnum.__members__.values()]))
    

