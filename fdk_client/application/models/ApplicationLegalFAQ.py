"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ApplicationLegalFAQ(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    

