"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AttributeMasterMandatoryDetails import AttributeMasterMandatoryDetails




class AttributeMasterMeta(BaseSchema):
    # Catalog swagger.json

    
    mandatory_details = fields.Nested(AttributeMasterMandatoryDetails, required=False)
    
    enriched = fields.Boolean(required=False)
    

