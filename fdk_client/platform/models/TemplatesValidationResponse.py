"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TemplateValidationData import TemplateValidationData

from .TemplateDetails import TemplateDetails


class TemplatesValidationResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(TemplateValidationData, required=False)
    
    template_details = fields.Nested(TemplateDetails, required=False)
    

