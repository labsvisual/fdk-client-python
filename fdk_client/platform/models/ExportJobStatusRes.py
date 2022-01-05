"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ExportJobStatusRes(BaseSchema):
    # Analytics swagger.json

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
    download_url = fields.Str(required=False)
    

