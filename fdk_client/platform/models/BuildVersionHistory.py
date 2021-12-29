"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BuildVersion import BuildVersion




class BuildVersionHistory(BaseSchema):
    # Configuration swagger.json

    
    versions = fields.Nested(BuildVersion, required=False)
    
    latest_available_version_name = fields.Str(required=False)
    

