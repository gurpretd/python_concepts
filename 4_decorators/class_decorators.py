
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
