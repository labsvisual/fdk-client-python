"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class TicketFeedbackPayload(BaseSchema):
    # Lead swagger.json

    
    form_response = fields.Dict(required=False)
    

