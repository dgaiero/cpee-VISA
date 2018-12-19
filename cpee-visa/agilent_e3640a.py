"""
.. module:: agilent_e3640a
    :platform: Windows
    :synopsis: Agilent E3640A basic VISA library for python
        utilizng the super Instrument VISA template.

.. moduleauthor:: Dominic Gaiero <dgaiero@calpoly.edu>
"""
import exceptions
from typing import List

from instrument import Instrument


class Agilent364XA(Instrument):
    """
    Agilent Single Output Power Supply VISA interface

    This class provides basic functionality for the Agilent E3640A power supply.

    .. note::
        It may work with any Agilent 364XA power supplies,
        however only the above has been mentioned.
    """

    def set_voltage(self, level: float):
        """
        Sets voltage of power supply. This will set the voltage to any level
        regardless of the output level set.

        :param level: Requested Voltage Level
        :type level: float
        :raises: MalformedParamterException
        """
        if (level > 20) or (level < 0):
            raise exceptions.MalformedParamterException(level,
                "between 0 - 20 V")
        self.instrument.write(f"VOLTage {level}")

    def get_voltage_actual(self) -> float:
        """
        Gets actual voltage output

        :rtype: float
        """
        return self.instrument.query("MEASure:VOLTage?")

    def get_voltage_set(self) -> float:
        """
        Gets set voltage output

        :rtype: float
        """
        return self.instrument.query("VOLTage?")

    def set_current(self, level: float):
        """
        Sets current of power supply.

        :param level: Requested Current Level
        :type level: float
        :raises: MalformedParamterException
        """
        if (level > 3) or (level < 0):
            raise exceptions.MalformedParamterException(level,
                    "between 0 - 3 A")
        self.instrument.write(f"CURRent {level}")

    def set_output(self, voltage: float, current: float):
        """
        Set output current and voltage

        :param voltage: Output Voltage (between 0 - 20 V)
        :type voltage: float
        :param current: Output Current (between 0 - 3 A)
        :type current: float
        :raises: MalformedParamterException
        """
        if (((current > 3) or (current < 0)) and
                ((voltage > 20) or (voltage < 0))):
            raise exceptions.MalformedParamterException(
                f"{voltage} V, {current} A", "between 0 - 3 A/0 - 20 V")
        self.instrument.write(f"APPLy {voltage}, {current}")

    def get_output_set(self) -> List[float]:
        """
        Gets output current and voltage

        :rtpye: list[float]
        """
        output = self.instrument.query("APPLy?")
        return [float(i) for i in output.split(',')]

    def get_current_actual(self) -> float:
        """
        Gets actual current output

        :rtype: float
        """
        return self.instrument.query("MEASure:CURRent?")

    def get_current_set(self) -> float:
        """
        Gets set current output

        :rtype: float
        """
        return self.instrument.query("CURRent?")

    def set_voltage_range(self, voltage_range: str):
        """
        Sets voltage range to high or low

        :param voltage_range: HIGH (20V) or LOW (8V)
        :type voltage_range: str
        :raises: MalformedParameterException
        """
        voltage_range = voltage_range.upper()
        if voltage_range == "HIGH":
            self.instrument.write("VOLTage:RANGe P20V")
        elif voltage_range == "LOW":
            self.instrument.write("VOLTage:RANGe P8V")
        else:
            raise exceptions.MalformedParamterException(voltage_range,
                                                        ["HIGH", "LOW"])

    def get_voltage_range(self) -> str:
        """
        Gets the current voltage range of HIGH or LOW.

        Runs command `VOLTage:RANGe?`

        :rtype: str
        """
        return self.instrument.query("VOLTage:RANGe?")

    def get_output_state(self) -> str:
        """
        Gets voltage and current output

        :rtype: str
        """
        return self.instrument.query("OUTPut?")

    def set_output_state(self, state: str):
        """
        Turns supply output on or off

        :param state: ON or OFF status of power supply
        :type state: str
        :raises: MalformedParameterException
        """
        state = state.upper()
        if state != "OFF" or state != "ON":
            raise exceptions.MalformedParamterException(state, ["ON", "OFF"])
        self.instrument.write(f"OUTput {state}")

    def beep(self):
        """
        Beeps instrument

        Sends beep command to instrument.
        """
        self.instrument.write("SYSTem:BEEPer")

    def get_erors(self) -> list:
        """
        Gets errors from machine.

        A record of up to 20 errors is stored in the power supply’s error queue.
        \\Errors are retrieved in first-in-first-out (FIFO) order.
        \\The first error returned is the first error that was stored.

        :rtype: list
        """
        # TODO: Convert to List
        errors = self.instrument.query("SYSTem:ERRor?")
        return errors
