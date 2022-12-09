class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self, string):
        self.message = string

    def print_string(self, string):
        return self.message(string)


test = StringFoo("message")

print(test.message)
