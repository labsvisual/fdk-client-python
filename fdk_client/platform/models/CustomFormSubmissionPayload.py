"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .TicketAsset import TicketAsset


class CustomFormSubmissionPayload(BaseSchema):
    # Lead swagger.json

    
    response = fields.List(fields.Dict(required=False), required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    

