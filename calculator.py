import math

class Calculator:
    def __init__(self):
        self.current_input = ""
        self.result = None
        self.display_text = ""

    def handle_input(self, input_value):
        if input_value == "=":
            try:
                self.result = str(eval(self.current_input))
                self.display_text = self.result
                self.current_input = self.result
            except Exception as e:
                self.current_input = "Error"
        elif input_value == "C":
            self.current_input = ""
            self.result = None
            self.display_text = ""
        elif input_value == "√":
            try:
                # Find the last number in the current input
                index = len(self.current_input)
                while index > 0 and self.current_input[index - 1].isdigit() or self.current_input[index - 1] == ".":
                    index -= 1

                # Extract the last number
                last_number = self.current_input[index:]

                # Calculate the square root of the last number
                if last_number:
                    number = float(last_number)
                    sqrt_result = math.sqrt(number)
                    self.current_input = self.current_input[:index] + str(sqrt_result)
                    self.display_text += " √ " + str(sqrt_result)
            except Exception as e:
                self.current_input = "Error"
        elif input_value == "^2":
            try:
                # Find the last number in the current input
                index = len(self.current_input)
                while index > 0 and self.current_input[index - 1].isdigit() or self.current_input[index - 1] == ".":
                    index -= 1

                # Extract the last number
                last_number = self.current_input[index:]

                # Calculate the square of the last number
                if last_number:
                    number = float(last_number)
                    squared_result = number ** 2
                    self.current_input = self.current_input[:index] + str(squared_result)
                    self.display_text += "^2"
            except Exception as e:
                self.current_input = "Error"
        elif input_value == "(":
            self.current_input += input_value
            self.display_text += input_value
        elif input_value == ")":
            self.current_input += input_value
            self.display_text += input_value
        else:
            self.current_input += input_value
            self.display_text += input_value

    def get_display_text(self):
        return self.display_text