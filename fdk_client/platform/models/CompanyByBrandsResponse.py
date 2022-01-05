"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BrandCompanyInfo import BrandCompanyInfo

from .Page import Page


class CompanyByBrandsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(BrandCompanyInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

