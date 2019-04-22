class MyClass(object):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def run(self):
        print('Hello, World!')

