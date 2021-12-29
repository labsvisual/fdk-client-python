"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CustomForm import CustomForm

from .Page import Page


class CustomFormList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(CustomForm, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

