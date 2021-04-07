"""
OR gate
"""
from logic_gates.GATE import Gate


class ORGate(Gate):
    """
    OR logic gate.
    """

    def __init__(self, input1=None, input2=None):
        super().__init__(input1, input2)
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
        return self._input1.output() | self._input2.output()

    def set_input1(self, obj):
        """Setter of input1"""
        self._input1 = obj

    def set_input2(self, obj):
        """Setter of input2"""
        self._input2 = obj
