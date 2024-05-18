from typing import List

# Annotations in variables.
a: int = 10
print(a)

b: float = 10.0
print(b)

c: str = "Hello"
print(c)

print(__annotations__)  # Display all the annotations defined globally

# Annotations in Functions
def add_nums(arg1: int, arg2: float) -> str:
    result = a + int(b)
    print(add_nums.__annotations__)  # Display annotations of the function.
    return str(result)


print(add_nums(10, 15.5))

list_var: List[int] = [1, 2, 3, 4]
list_var.append(5)  # Appended integer.
print(list_var)

#Annotations in Classes
class Abc:
    def __init__(self, age: int, name: str, full_name: List[3]):
        self.age = age
        self.name = name
        self.fullname = full_name
        print("Fullname :", full_name[0], full_name[1], full_name[2])

Abc(30, "dhami", ["Gurpreet", "Singh", "Dhami"])

# Class types as Annotations
from typing import Type
type_abc: Type[Abc] = Abc(30, "dhami", ["Gurpreet", "Singh", "Dhami"])
