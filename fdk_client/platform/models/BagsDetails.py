"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagFinancialBreakup import BagFinancialBreakup

from .BagCurrStatus import BagCurrStatus

from .BagItem import BagItem

from .BagArticle import BagArticle



from .BagPrices import BagPrices

from .GstDetails import GstDetails

from .BagBreakupValues import BagBreakupValues



from .BagCurrentStatus import BagCurrentStatus

from .BagStatus import BagStatus








class BagsDetails(BaseSchema):
    # Order swagger.json

    
    financial_breakup = fields.List(fields.Nested(BagFinancialBreakup, required=False), required=False)
    
    status = fields.Nested(BagCurrStatus, required=False)
    
    item = fields.Nested(BagItem, required=False)
    
    article = fields.Nested(BagArticle, required=False)
    
    id = fields.Int(required=False)
    
    prices = fields.Nested(BagPrices, required=False)
    
    gst_details = fields.Nested(GstDetails, required=False)
    
    breakup_values = fields.Nested(BagBreakupValues, required=False)
    
    update_time = fields.Int(required=False)
    
    current_status = fields.Nested(BagCurrentStatus, required=False)
    
    bag_status = fields.Nested(BagStatus, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    payment_methods = fields.Dict(required=False)
    

