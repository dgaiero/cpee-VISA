"""
Exceptions class holds exceptions that are called throughout instruments.
"""

class MalformedParamterException(Exception):
    """
    This exception is raised when a paramter is incorrect.
    """
    def __init__(self, parameter: str, expected_parameter: str) -> None:
        msg = f"Recieved parameter: {parameter}. Expected parameters: {expected_parameter}"
        super(MalformedParamterException, self).__init__(msg)

class InstrumentError(Exception):
    """
    This exception is raised when an instrument has an error.
    """
