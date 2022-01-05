"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PhoneSchema import PhoneSchema

from .EmailSchema import EmailSchema


class ContactSchema(BaseSchema):
    # Content swagger.json

    
    phone = fields.Nested(PhoneSchema, required=False)
    
    email = fields.Nested(EmailSchema, required=False)
    

