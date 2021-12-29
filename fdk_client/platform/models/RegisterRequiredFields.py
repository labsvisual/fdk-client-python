"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RegisterRequiredFieldsEmail import RegisterRequiredFieldsEmail

from .RegisterRequiredFieldsMobile import RegisterRequiredFieldsMobile


class RegisterRequiredFields(BaseSchema):
    # User swagger.json

    
    email = fields.Nested(RegisterRequiredFieldsEmail, required=False)
    
    mobile = fields.Nested(RegisterRequiredFieldsMobile, required=False)
    

