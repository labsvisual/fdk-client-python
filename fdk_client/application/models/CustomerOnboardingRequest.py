"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BusinessDetails import BusinessDetails

from .DeviceDetails import DeviceDetails



from .UserPersonalInfoInDetails import UserPersonalInfoInDetails



from .MarketplaceInfo import MarketplaceInfo


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    source = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    

