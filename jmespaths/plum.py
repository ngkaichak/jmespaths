class Plum:
    def __init__(self, expression, data) -> None:
        self.expression = expression
        self.data = data.peach() if isinstance(data, Plum)else data

    def plum(self, value):
        if isinstance(self.data, dict):
            if self.expression not in self.data:
                return
        self.data[self.expression] = value

    def peach(self):
        return self.data[self.expression]

    def __get__(self, instance):
        try:
            return self.data[self.expression].get(instance)
        except AttributeError:
            return None

    def __instancecheck__(self, instance):
        return isinstance(instance, self.data[self.expression])
