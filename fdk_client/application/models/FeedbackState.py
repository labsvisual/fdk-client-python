"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class FeedbackState(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    media = fields.Str(required=False)
    
    qna = fields.Boolean(required=False)
    
    rating = fields.Boolean(required=False)
    
    review = fields.Boolean(required=False)
    

