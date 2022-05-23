"""Python code/sdk/application/ApplicationConfig.py."""

from typing import Dict

from ..common.constants import APPLICATION_MIN_TOKEN_LENGTH, DEFAULT_DOMAIN
from ..common.exceptions import FDKInvalidCredentialError
from .models.LocationValidator import LocationValidator


class ApplicationConfig:
    def __init__(self, _conf: Dict, _opts: Dict = None, cookies: Dict = None):
        """Defines application id, token and validates it."""
        self.applicationID = _conf.get("applicationID", "")
        self.applicationToken = _conf.get("applicationToken", "")
        self.opts = _opts or {}
        self.domain = _conf.get("domain", DEFAULT_DOMAIN)
        self.cookies = cookies or {}
        self.extraHeaders = []
        self.locationDetails = _conf.get("locationDetails")
        self.validate()

    def validate(self):
        """Validates applicationID and applicationToken."""
        if not self.applicationID:
            raise FDKInvalidCredentialError("No Application ID Present")

        if not self.applicationToken:
            raise FDKInvalidCredentialError("No Application Token Present")

        if len(self.applicationToken) < APPLICATION_MIN_TOKEN_LENGTH:
            raise FDKInvalidCredentialError("Invalid Application Token")

        if self.locationDetails:
            schema = LocationValidator.validateLocationObj()
            schema.dump(schema.load(self.locationDetails))
