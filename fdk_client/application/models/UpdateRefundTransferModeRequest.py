"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UpdateRefundTransferModeRequest(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    

