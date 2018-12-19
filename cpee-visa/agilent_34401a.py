"""
.. module:: agilent_34401a
    :platform: Windows
    :synopsis: Agilent 34401A basic VISA library for python
        utilizng the super Instrument VISA template.

.. moduleauthor:: Dominic Gaiero <dgaiero@calpoly.edu>
"""
import exceptions

from instrument import Instrument


class Agilent34401A(Instrument):
    """
    Agilent (HP) 34401A Multimeter VISA interface

    This interface provides basic functionality for the
    Agilent 34401A multimeter.
    """

    def current_measurement(self, measurement_type: str) -> float:
        """
        Measures either AC or DC current.

        :param measurement_type: AC or DC measurement
        :type measurement_type: str
        :rtype: float
        :raises: MalformedParamterException
        """
        measurement_type = measurement_type.upper()
        if (measurement_type == "AC") or (measurement_type == "DC"):
            return self.instrument.query(
                f"MEASure:CURRent:{measurement_type}? DEF,DEF")
        raise exceptions.MalformedParamterException(measurement_type,
                                                    ["AC", "DC"])

    def voltage_measurement(self, measurement_type: str) -> float:
        """
        Measures either AC or DC voltage.

        :param measurement_type: AC or DC measurement
        :type measurement_type: str
        :rtype: float
        :raises: MalformedParamterException
        """
        measurement_type = measurement_type.upper()
        if (measurement_type == "AC") or (measurement_type == "DC"):
            return self.instrument.query(
                f"MEASure:VOLTage:{measurement_type}? DEF,DEF")
        raise exceptions.MalformedParamterException(measurement_type,
                                                    ["AC", "DC"])

    def resistance_measurement(self, measurement_type: str) -> float:
        """
        Measures either two or four wire resistance.

        :param measurement_type: TWO or FOUR wire measurement
        :type measurement_type: str
        :rtype: float
        :raises: MalformedParamterException
        """
        if measurement_type == "TWO":
            return self.instrument.query(
                f"MEASure:RESistance? DEF,DEF")
        elif measurement_type == "FOUR":
            return self.instrument.query(
                f"MEASure:FRESistance? DEF,DEF")
        else:
            raise exceptions.MalformedParamterException(
                measurement_type, ["TWO", "FOUR"])

    def frequency_measurement(self) -> float:
        """
        Measures frequency.

        :rtype: float
        :raises: MalformedParamterException
        """
        return self.instrument.query("MEASure:FREQuency? DEF,DEF")

    def period_measurement(self) -> float:
        """
        Measures the period of a signal.

        :rtype: float
        :raises: MalformedParamterException
        """
        return self.instrument.query("MEASure:PERiod? DEF,DEF")

    def continuity_measurement(self) -> float:
        """
        Measures contunity of a wire.

        :rtype: float
        :raises: MalformedParamterException
        """
        return self.instrument.query("MMEASure:CONTinuity?")

    def diode_measurement(self) -> float:
        """
        Preset and make a diode measurement.

        :rtype: float
        :raises: MalformedParamterException
        """
        return self.instrument.query("MEASure:DIODe?")

    def beep(self):
        """
        Beeps instrument

        Sends beep command to instrument.
        """
        self.instrument.write("SYSTem:BEEPer")
