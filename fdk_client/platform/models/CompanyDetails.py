"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CompanySocialAccounts import CompanySocialAccounts


class CompanyDetails(BaseSchema):
    # CompanyProfile swagger.json

    
    website_url = fields.Str(required=False)
    
    socials = fields.List(fields.Nested(CompanySocialAccounts, required=False), required=False)
    

