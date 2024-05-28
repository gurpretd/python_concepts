
class debug_params:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        for i in args:
            if type(i) is not int:
                print("Error: Only integers accepted")
                return
        return self._func(*args, **kwargs)

@debug_params
def sum_op(num1: int, num2: int):
    return num1 + num2


print(sum_op(10, 20))
print(sum_op("10", 20))

#static method decorator

class math_ops:
    num1 =0
    num2 = 0
    result = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        self.result = self.num1 + self.num2

    @classmethod
    def get_result(cls):
        print(cls.result)

    @staticmethod
    def get_description():
        print("Hello")

math_op = math_ops(10,20)
math_op.get_description()
math_op.get_result()
