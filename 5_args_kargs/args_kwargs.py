def function_with_args(*args_normal, **named_args):
    print("normal args", *args_normal)
    print("named args", str(named_args))

    for values in args_normal:
        print(args_normal)
    for key, values in named_args.items():
        print(key, ":", values)


function_with_args(10, "hello", d="aaa", k=10.44)

function_with_args(10,  20, 30, "hello", named_1 = 100, named_2 = "aa", named_3 = 100.20)


def function_with_mixed_args(arg1: int, agr2: str, *args_normal, **named_args):
    print("normal args", *args_normal)
    print("named args", str(named_args))



function_with_mixed_args(10, "hello", 30, named1="aaa", named_2=10, named_3=100.20)
