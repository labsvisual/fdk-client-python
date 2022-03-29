"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Application import Application


class ApplicationResponse(BaseSchema):
    # Common swagger.json

    
    application = fields.Nested(Application, required=False)
    

