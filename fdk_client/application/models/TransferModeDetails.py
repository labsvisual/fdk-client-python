"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TransferItemsDetails import TransferItemsDetails




class TransferModeDetails(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(TransferItemsDetails, required=False), required=False)
    
    display_name = fields.Str(required=False)
    

