"""
Exceptions class holds exceptions that are called throughout instruments.
"""

class MalformedParamterException(Exception):
    """
    This exception is raised when a paramter is incorrect.
    """
    def __init__(self, parameter: str, expected_parameter: str) -> None:
        """
        :param parameter: parameter given to instrument
        :type parameter: str
        :param expected_parameter: Parameter that instrument expected
        :type expected_parameter: str
        """
        msg = f"Recieved parameter: {parameter}. Expected parameters: {expected_parameter}"
        super(MalformedParamterException, self).__init__(msg)

class InstrumentError(Exception):
    """
    This exception is raised when an instrument has an error.
    """
