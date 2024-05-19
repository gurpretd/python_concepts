a: int
b: int


def func(a, b):
    print(a, b)


a = 10
b = 10
func(a, b)

# Forward Declaration of Class
import typing

NewClass = typing.NewType("NewClass", None)
myStr: str
myNumber: int
myObject: NewClass

print("Forward Declared Class")
