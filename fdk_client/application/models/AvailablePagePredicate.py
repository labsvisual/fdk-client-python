"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AvailablePageScreenPredicate import AvailablePageScreenPredicate

from .AvailablePageUserPredicate import AvailablePageUserPredicate

from .AvailablePageRoutePredicate import AvailablePageRoutePredicate


class AvailablePagePredicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    

