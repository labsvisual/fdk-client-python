"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TemplateRequest import TemplateRequest


class TemplateRequestList(BaseSchema):
    # Feedback swagger.json

    
    template_list = fields.List(fields.Nested(TemplateRequest, required=False), required=False)
    

