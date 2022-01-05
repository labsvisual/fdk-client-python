"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AbandonCartsDetail import AbandonCartsDetail



from .Page import Page


class AbandonCartsList(BaseSchema):
    # Analytics swagger.json

    
    items = fields.List(fields.Nested(AbandonCartsDetail, required=False), required=False)
    
    cart_total = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    

