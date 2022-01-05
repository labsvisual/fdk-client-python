"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class AppLogisticsConfig(BaseSchema):
    # Configuration swagger.json

    
    logistics_by_seller = fields.Boolean(required=False)
    
    serviceability_check = fields.Boolean(required=False)
    
    same_day_delivery = fields.Boolean(required=False)
    
    dp_assignment = fields.Boolean(required=False)
    

