"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PayloadSmsTemplateStructure import PayloadSmsTemplateStructure

from .PayloadSmsProviderStructure import PayloadSmsProviderStructure


class PayloadSmsStructure(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(PayloadSmsTemplateStructure, required=False)
    
    provider = fields.Nested(PayloadSmsProviderStructure, required=False)
    

