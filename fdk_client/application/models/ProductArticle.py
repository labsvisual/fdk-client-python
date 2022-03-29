"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticlePriceInfo import ArticlePriceInfo



from .BaseInfo import BaseInfo



from .BaseInfo import BaseInfo






class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Str(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    size = fields.Str(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    

