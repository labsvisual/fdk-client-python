"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CompanySocialAccounts(BaseSchema):
    # CompanyProfile swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

