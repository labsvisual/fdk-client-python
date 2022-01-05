"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class RewardsValidator:
    
    class getPointsOnProduct(BaseSchema):
        
        pass 
    
    class getOfferByName(BaseSchema):
        
        name = fields.Str(required=False)
         
    
    class getOrderDiscount(BaseSchema):
        
        pass 
    
    class getUserPoints(BaseSchema):
        
        pass 
    
    class getUserPointsHistory(BaseSchema):
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getUserReferralDetails(BaseSchema):
        
        pass 
    
    class redeemReferralCode(BaseSchema):
        
        pass 
    