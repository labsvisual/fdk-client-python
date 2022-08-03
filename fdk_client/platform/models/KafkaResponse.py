"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class KafkaResponse(BaseSchema):
    # Inventory swagger.json

    
    offset = fields.Int(required=False)
    
    partition = fields.Int(required=False)
    

