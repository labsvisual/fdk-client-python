"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .FeedbackResponseItem import FeedbackResponseItem










class TicketFeedback(BaseSchema):
    # Lead swagger.json

    
    _id = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    response = fields.List(fields.Nested(FeedbackResponseItem, required=False), required=False)
    
    category = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    

