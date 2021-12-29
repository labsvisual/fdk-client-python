"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyBrandInfo import CompanyBrandInfo


class BrandsByCompanyResponse(BaseSchema):
    # Configuration swagger.json

    
    brands = fields.Nested(CompanyBrandInfo, required=False)
    

