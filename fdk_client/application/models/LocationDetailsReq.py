"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .TatReqProductArticles import TatReqProductArticles




class LocationDetailsReq(BaseSchema):
    # Logistic swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatReqProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    

