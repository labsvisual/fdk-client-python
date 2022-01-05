"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Giveaway import Giveaway

from .Page import Page


class GiveawayResponse(BaseSchema):
    # Rewards swagger.json

    
    items = fields.List(fields.Nested(Giveaway, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

