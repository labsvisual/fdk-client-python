"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PayloadEmailTemplateStructure import PayloadEmailTemplateStructure

from .PayloadEmailProviderStructure import PayloadEmailProviderStructure


class PayloadEmailStructure(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(PayloadEmailTemplateStructure, required=False)
    
    provider = fields.Nested(PayloadEmailProviderStructure, required=False)
    

