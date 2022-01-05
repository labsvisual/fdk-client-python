"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .GlobalValidation import GlobalValidation


class TemplateValidationData(BaseSchema):
    # Catalog swagger.json

    
    template_validation = fields.Dict(required=False)
    
    global_validation = fields.Nested(GlobalValidation, required=False)
    

