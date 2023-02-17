#5

class FileNotExists(Exception):
    def __init__(self):
        super(FileNotExists, self).__init__()


def validate_file_exists(path) -> callable:
    def func1(function):
        def func2(*args, **kwargs):
            if path.exists(path) is False:
                raise FileNotExists()
                return func2()
        return func1()


