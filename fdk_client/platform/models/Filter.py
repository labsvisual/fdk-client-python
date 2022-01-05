"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Priority import Priority

from .TicketCategory import TicketCategory

from .Status import Status




class Filter(BaseSchema):
    # Lead swagger.json

    
    priorities = fields.List(fields.Nested(Priority, required=False), required=False)
    
    categories = fields.List(fields.Nested(TicketCategory, required=False), required=False)
    
    statuses = fields.List(fields.Nested(Status, required=False), required=False)
    
    assignees = fields.List(fields.Dict(required=False), required=False)
    

