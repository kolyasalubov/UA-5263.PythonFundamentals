def class_name_changer(cls, new_name):
    cls.__name__ = new_name

class MyClass:
    pass

myObject = MyClass()
class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)