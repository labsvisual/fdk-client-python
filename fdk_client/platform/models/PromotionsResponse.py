"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .PromotionListItem import PromotionListItem


class PromotionsResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(PromotionListItem, required=False)
    

