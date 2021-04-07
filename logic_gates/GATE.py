"""
GATE
"""


class Gate:
    """
    Logic gate.
    """
    def __init__(self, input1=None, input2=None):
        """

        :param input1: gate object
        :param input2: gate object
        """
        self._input1 = input1
        self._input2 = input2

    def output(self) -> int:
        """
        Output the gate value.
        """
        pass

    def set_input1(self, obj):
        """Setter of input1"""
        self._input1 = obj

    def set_input2(self, obj):
        """Setter of input2"""
        self._input2 = obj
