"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AbuseReport import AbuseReport

from .Page import Page


class ReportAbuseGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(AbuseReport, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

