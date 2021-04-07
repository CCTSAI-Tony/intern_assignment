"""
Logic gate simulation
"""
from logic_gates.AND import ANDGate
from logic_gates.OR import ORGate
from logic_gates.XOR import XORGate
from logic_gates.NOT import NOTGate
from logic_gates.INPUT import INPUTGate
from logic_gates.OUTPUT import OUTPUTGate

"""
Idea: Use OOD manner to solve this logic gate problem. 
Create different gate class and each gate class has its own logic output.
Each gate instance can link their input gate object(s), and based on its input values,
it cal calculate it's own output value.
Use list structure to do the linking process.
"""


class Solution:
    def __init__(self, file):
        """
        Parse the input file's information.
        :param file: str
        """
        if not file:
            raise ValueError("Please give a valid path.")
        # Do the logic and grab the information here.
        with open(file, 'r') as f:
            lines = (f.readlines())
        number_of_gates = int(lines[0].strip("\n"))
        #  Create a list to store all the gates.
        self.gates = [INPUTGate()] * (number_of_gates + 1)
        #  Create a list to store the input reference for each gate.
        self.reference = [(-1, -1)] * (number_of_gates + 1)
        for line in lines[1:]:
            line = line.strip("\n").replace(":", "").split()
            i = int(line[0])
            type_of_gate = line[1].upper()
            input_ref = (int(line[2]), int(line[3]))
            # Create different gate instance based on the label.
            if type_of_gate == "I":
                gate = INPUTGate()
            elif type_of_gate == "N":
                gate = NOTGate()
            elif type_of_gate == "A":
                gate = ANDGate()
            elif type_of_gate == "O":
                gate = ORGate()
            elif type_of_gate == "X":
                gate = XORGate()
            else:
                gate = OUTPUTGate()
            # When overriding situation happens,
            # warning the user that the input_file's information is incorrect.
            if self.reference[i] != (-1, -1):
                raise ValueError("Duplicate index happens, "
                                 "gate_index need to be unique")
            self.gates[i] = gate
            self.reference[i] = input_ref

    def simple_circuit(self):
        # Link the input objects for each gate.
        self.gate_map_reference()
        output_gate = None
        for gate in self.gates[1:]:
            if type(gate) == OUTPUTGate:
                output_gate = gate
                # Cause there is only one output gate, then break the loop.
                break
        print(output_gate.output())

    def gate_map_reference(self):
        for i in range(1, len(self.gates)):
            gate = self.gates[i]
            ref_1, ref_2 = self.reference[i]
            # Make sure input value is valid.
            if type(gate) == INPUTGate:
                value = input("Please input a value to the INPUT Gate. ")
                while not value.isdigit() or value not in ["0", "1"]:
                    value = input("Value is invalid, please try again. ")
                gate.set_input1(int(value))
            elif type(gate) in [ANDGate, ORGate, XORGate]:
                # Make sure input reference is valid.
                if ref_1 == 0 or ref_2 == 0:
                    raise ValueError(
                        "Invalid input reference of gate {}".format(i))
                gate.set_input1(self.gates[ref_1])
                gate.set_input2(self.gates[ref_2])

            elif type(gate) in [NOTGate, OUTPUTGate]:
                # Make sure input reference is valid.
                if ref_1 == 0 and ref_2 == 0:
                    raise ValueError(
                        "Invalid input reference of gate {}".format(i))
                ref = ref_1 or ref_2
                gate.set_input1(self.gates[ref])


if __name__ == '__main__':
    #  Please paste your input_file.txt here.
    input_file = "./input.txt"
    Solution(input_file).simple_circuit()
