class Print:
    """Show in depth explanation of your rules."""

    def __init__(self, value: str):
        self.value = value

    def __call__(self):
        print(self.value)
