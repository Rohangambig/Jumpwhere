class StringReverser:
    def reverse_words(self, s):
        return " ".join(s.split()[::-1])

reverser = StringReverser()
s = "hello .py"
print(reverser.reverse_words(s))
