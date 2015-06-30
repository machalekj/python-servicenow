class ServiceNowError(Exception):
    """General error for servicenow module."""
    pass

class InvalidCredentials(ServiceNowError):
    """Invalid credentials error. Raised when HTTP status code 401 is received."""
    pass


__all__ = ['Connection', 'ServiceNow', 'ServiceNowError', 'InvalidCredentials']
