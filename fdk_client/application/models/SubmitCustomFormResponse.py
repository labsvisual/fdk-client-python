"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Ticket import Ticket


class SubmitCustomFormResponse(BaseSchema):
    # Lead swagger.json

    
    message = fields.Str(required=False)
    
    ticket = fields.Nested(Ticket, required=False)
    

