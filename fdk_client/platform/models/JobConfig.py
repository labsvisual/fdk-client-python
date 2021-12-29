"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .StoreFilter import StoreFilter

from .ProcessConfig import ProcessConfig

from .StoreConfig import StoreConfig









from .CompanyConfig import CompanyConfig











from .DBConnectionProfile import DBConnectionProfile







from .CatalogMasterConfig import CatalogMasterConfig







from .Audit import Audit






class JobConfig(BaseSchema):
    # Inventory swagger.json

    
    _id = fields.Int(required=False)
    
    job_code = fields.Str(required=False)
    
    task_type = fields.Str(required=False)
    
    sync_delay = fields.Int(required=False)
    
    cron_expression = fields.Str(required=False)
    
    store_filter = fields.Nested(StoreFilter, required=False)
    
    process_config = fields.Nested(ProcessConfig, required=False)
    
    store_config = fields.List(fields.Nested(StoreConfig, required=False), required=False)
    
    properties = fields.Dict(required=False)
    
    immediate_first_run = fields.Boolean(required=False)
    
    disable = fields.Boolean(required=False)
    
    dependent_job_codes = fields.List(fields.Str(required=False), required=False)
    
    company_config = fields.List(fields.Nested(CompanyConfig, required=False), required=False)
    
    company_ids = fields.List(fields.Int(required=False), required=False)
    
    tax_identifiers = fields.List(fields.Str(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    period_threshold = fields.Int(required=False)
    
    period_threshold_type = fields.Str(required=False)
    
    db_connection_profile = fields.Nested(DBConnectionProfile, required=False)
    
    params = fields.Dict(required=False)
    
    open_tags = fields.Dict(required=False)
    
    delete_quantity_threshold = fields.Int(required=False)
    
    catalog_master_config = fields.Nested(CatalogMasterConfig, required=False)
    
    aggregator_types = fields.List(fields.Str(required=False), required=False)
    
    integration_type = fields.Str(required=False)
    
    min_price = fields.Float(required=False)
    
    audit = fields.Nested(Audit, required=False)
    
    version = fields.Int(required=False)
    
    alias = fields.Str(required=False)
    

