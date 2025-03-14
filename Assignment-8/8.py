class StringManipulator:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s[::-1])

manipulator = StringManipulator()
manipulator.get_string()
manipulator.print_string()
