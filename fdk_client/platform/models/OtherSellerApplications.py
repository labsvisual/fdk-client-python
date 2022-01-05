"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OtherSellerApplication import OtherSellerApplication

from .Page import Page


class OtherSellerApplications(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(OtherSellerApplication, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

