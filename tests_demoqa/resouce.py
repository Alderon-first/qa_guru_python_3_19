import os


def path_file(name_file):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, name_file))


print(1)

