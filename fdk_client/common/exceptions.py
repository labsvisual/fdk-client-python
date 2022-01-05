"""Python code/sdk/common/exceptions.py."""


class FDKInvalidCredentialError(Exception):
    """Invalid credential exception."""
    def __init__(self, message="Invalid Credentials"):
        """Initialize function __init__."""
        super(FDKInvalidCredentialError, self).__init__(message)


class RequiredParametersError(Exception):
    """Invalid credential exception."""
    def __init__(self, message="Required Parameters not present"):
        """Initialize function __init__."""
        super(RequiredParametersError, self).__init__(message)
        
        
class FDKOAuthCodeError(Exception):
    """FDK OAuth Exception."""
    def __init__(self, message=""):
        """Initialize function __init__."""
        super(FDKOAuthCodeError, self).__init__(message)
