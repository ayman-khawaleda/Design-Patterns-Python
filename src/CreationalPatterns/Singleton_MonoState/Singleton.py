def SingletonDec(class_instance):
    """DECORATOR THAT CREATES A SINGLETON."""
    instances = {}
    def get_instance(*args,**kwargs):
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args,**kwargs)
        return instances[class_instance]
    return get_instance

class Singleton(type):
    """METACLASS THAT CREATES A SINGLETON BASED ON TYPE CLASS"""

    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



