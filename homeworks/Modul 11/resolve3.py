# Домашнее задание по теме "Интроспекция"

def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_attributes = [attributes for attributes in dir(obj) if not callable(getattr(obj, attributes))]
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_module = obj.__class__.__module__


    result = {'type': obj_type,
              'attributes': obj_attributes,
              'methods': obj_methods,
              'module': obj_module}

    return result


class MyClass:
    def __init__(self):
        self.a = 2
        self.b = 6

    def my_method(self):
        pass


obj = MyClass()
number_info_1 = introspection_info(42)
number_info_2 = introspection_info(obj)


for key, value in number_info_1.items():
    print(f"{key}: {value}")

print()

for key, value in number_info_2.items():
    print(f"{key}: {value}")
