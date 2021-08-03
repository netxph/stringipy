from stringipy.FluentString import FluentString

class FluentStringList:

    def __init__(self, data):
        self.data = data

    def prefix(self, prefix):
        return FluentStringList([FluentString(item).prefix(prefix).data for item in self.data])
        
    def suffix(self, suffix):
        return FluentStringList([FluentString(item).suffix(suffix).data for item in self.data])

    def snake_case(self):
        return FluentStringList([FluentString(item).snake_case().data for item in self.data])
    
    def join(self, separator):
        print(dir(FluentString))
        return FluentString(separator.join(self.data))