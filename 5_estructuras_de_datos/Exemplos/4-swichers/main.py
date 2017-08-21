switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

print(switcher.get(0, "nothing"))
print(switcher.get(5, "nothing"))


switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

print('---' * 10)

def zero():
    print("zero")

def one():
    print("one")

def default():
    print("default")

switcher = {
        0: zero,
        1: one,
    }

func = switcher.get(4, default)
func()
