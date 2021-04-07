"""
INPUT gate
"""
from logic_gates.GATE import Gate


class INPUTGate(Gate):
    """
    INPUT logic gate.
    """
    def __init__(self, input1=None, input2=None):
        super().__init__(input1, input2)
        """
        
        :param input1: int
        :param input2: int
        """
        self._input1 = input1
        self._input2 = input2

    def output(self):
        """
        Output the gate value, time complexity O(1).
        :return: int
        """
        return self._input1

    def set_input1(self, value):
        self._input1 = value

    def set_input2(self, value):
        pass
