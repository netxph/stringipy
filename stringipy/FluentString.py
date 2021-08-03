import re

class FluentString:

    def __init__(self, data):
        self.data = data

    def prefix(self, prefix):
        return FluentString(f"{prefix}{self.data}")

    def suffix(self, suffix):
        return FluentString(f"{self.data}{suffix}")

    def snake_case(self):
        name = self.data

        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub('__([A-Z])', r'_\1', name)
        name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)

        return FluentString(name.lower())

    def print(self):
        print(self.data)