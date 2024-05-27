def say_hi(func):
    def inner_wrapper():
        print("hi from decorator")
        func()

    return inner_wrapper


@say_hi
def actual_func():
    print("I am the actual function")


# actual_func()


# with fixed arguments


def validate_age(func):
    def validator(age: int):
        if age > 140 or age < 0:
            print("age is invalid")
        else:
            print("age is valid")

    return validator


@validate_age
def set_age(input_age: int):
    age = input_age

#
# set_age(150)
# set_age(50)


# With Variable number of arguments
def validate_result(func):
    def validator(*args, **kwargs):
        print("****START ***** ")
        invalidate = False
        if type(args[0]) is not str:
            invalidate = True
            print("Invalid name ( Name Must be string)")
        if (type(args[1]) is not int) or (args[1] < 0 or args[1] > 140):
            print("invalid age")
            invalidate = True

        for key, value in kwargs.items():
            #Marks must be in range 0 to 100.
            if (value < 0) or (value >100):
                invalidate = True
                print(f"invalid marks {value} for subject {key}".format(key, value))

        if invalidate:
            print("Report not generated")
        else:
            func(*args, **kwargs)
        print("**** STOP ***** ")

    return validator


@validate_result
def evaluate_result(name: str, age: int, **kwargs):
    print("** FINAL REPORT START")
    print(f"Report for {name} aged {age} is below".format(name, age))
    for key, value in kwargs.items():
        print(f"            Marks in {key} are {value}".format(key, value))
    print("** FINAL REPORT END")

evaluate_result("gurpreet", 30, )
evaluate_result("gurpreet", 300, )
evaluate_result(111, 300, maths = 90, science = 70, art = 100)
evaluate_result(111, 300, maths = 90, science = 70, art = 1000)
evaluate_result("Gurpreet", 30, maths = 90, science = 70, art = 100)