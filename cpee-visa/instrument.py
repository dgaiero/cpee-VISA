"""
Instrument class to define common functionalities for all instruments.
"""
import visa

class Instrument:
    """
    Base class to define common functionality for VISA instruments.
    """

    def __init__(self, address: str) -> None:
        """
        Initalizes class

        :param address: Address of instrument
        :type address: str
        """
        self.address = address
        __resources = visa.ResourceManager()
        self.instrument = __resources.open_resource(self.address)
        self.instrument.encoding = "latin-1"

    def __repr__(self) -> str:
        return self.instrument.query('*IDN?')

    def __str__(self) -> str:
        return self.instrument.query('*IDN?')

    def identity(self) -> str:
        """
        Returns identity string

        :rtype: str
        """
        return self.instrument.query("*IDN?")

    def operation_complete(self):
        """
        Return "1" to the output buffer after the command is executed.
        Use the `*OPC?` command to guarantee that commands previously
        \\sent to the instrument have completed.
        """
        return self.instrument.query("*OPC?")

    def event_status_register(self) -> str:
        """
        Query the Standard event register

        :rtype: str
        """
        return self.instrument.query("*ESR?")

    def reset(self):
        """
        Reset the instrument to its **power-on** state.
        """
        self.instrument.write("*RST")

    def wait(self):
        """
        Instruct the instrument to wait for all pending operations to complete before
        \\executing any additional commands over the interface.
        """
        self.instrument.write("*WAI")

    def trigger(self) -> str:
        """
        Generate a trigger to the trigger subsystem that has selected a bus (software)
        \\trigger as its source `(TRIG:SOUR BUS)`.
        """
        self.instrument.write("*TRG")

    def clear(self) -> str:
        """
        Clear all event registers and Status Byte register.
        """
        self.instrument.write("*CLS")

    def test(self) -> str:
        """
        Perform a complete self-test of the instrument.
        """
        return self.instrument.write("*TST?")

    def custom_query(self, query: str) -> str:
        """
        Run a query for a custom message and return message.

        :param query: Query to run
        :type query: str
        :rtype: str
        """
        return self.instrument.query(query)

    def custom_write(self, write: str) -> str:
        """
        Run a write for a custom message.

        :param write: Write to run
        :type write: str
        """
        return self.instrument.write(write)

    def custom_command(self, function_name: str, *args, **kwargs) -> str:
        """
        Call a function in pyvisa.

        :param function_name: Function to call
        :param args: Arguments of function
        :param kwargs: Kewrod Arguments of function
        """
        # TODO: Call pyvisa cross reference
        function = getattr(self.instrument, function_name)
        return function(*args, **kwargs)

    def close_connection(self):
        """
        Closes connection to instrument
        """
        self.instrument.close()
