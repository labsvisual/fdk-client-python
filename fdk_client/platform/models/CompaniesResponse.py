"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppInventoryCompanies import AppInventoryCompanies

from .Page import Page


class CompaniesResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.Nested(AppInventoryCompanies, required=False)
    
    page = fields.Nested(Page, required=False)
    

