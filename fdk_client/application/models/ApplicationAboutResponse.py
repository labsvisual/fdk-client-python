"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ApplicationInfo import ApplicationInfo

from .CompanyInfo import CompanyInfo

from .OwnerInfo import OwnerInfo


class ApplicationAboutResponse(BaseSchema):
    # Configuration swagger.json

    
    application_info = fields.Nested(ApplicationInfo, required=False)
    
    company_info = fields.Nested(CompanyInfo, required=False)
    
    owner_info = fields.Nested(OwnerInfo, required=False)
    

