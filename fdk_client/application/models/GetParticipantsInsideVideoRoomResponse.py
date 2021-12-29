"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Participant import Participant


class GetParticipantsInsideVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    participants = fields.List(fields.Nested(Participant, required=False), required=False)
    

