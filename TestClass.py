class TestClass:
    "测试"
    count = 0

    def __init__(self, age, salary):
        self.age = age
        self.salary = salary
        TestClass.count += 1


if __name__ == '__main__':
    child1 = TestClass(1, 2)
    child2 = TestClass(3, 4)
    print(child1)
    print(child2.age)
    print(child2.salary)
    print(TestClass.count)
    print("#################")
    print(TestClass.__doc__)
    # print(TestClass.__dict__)
    print(TestClass.__name__)
    print(TestClass.__class__)


