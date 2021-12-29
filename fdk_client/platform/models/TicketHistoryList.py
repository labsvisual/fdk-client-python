"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TicketHistory import TicketHistory

from .Page import Page


class TicketHistoryList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(TicketHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

