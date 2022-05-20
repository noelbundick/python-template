""" Sample module """


class Hello:
    """Sample class"""

    myName = "computer"

    def greet(self, word="world"):
        """Greet the caller"""
        return f"Hello, {word} from {self.myName}!"

    def echo(self, word):
        """Echo the caller"""
        return f"{word} from {self.myName}"
