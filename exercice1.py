class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self, string):
        self.message = string

    def print_string(self):
        print(self.message)


test = StringFoo("message")
test.print_string()


