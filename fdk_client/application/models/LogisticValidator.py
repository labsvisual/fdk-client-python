"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class LogisticValidator:
    
    class getTatProduct(BaseSchema):
        
        pass 
    
    class getPincodeZones(BaseSchema):
        
        pass 
    
    class getPincodeCity(BaseSchema):
        
        pincode = fields.Str(required=False)
         
    