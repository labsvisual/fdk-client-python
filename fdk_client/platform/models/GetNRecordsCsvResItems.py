"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class GetNRecordsCsvResItems(BaseSchema):
    # Communication swagger.json

    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    firstname = fields.Str(required=False)
    
    lastname = fields.Str(required=False)
    
    orderid = fields.Str(required=False)
    

