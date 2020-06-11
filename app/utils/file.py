import time
from typing import AnyStr

from . import project_file


def read_file(filename) -> AnyStr:
    with open(filename, "r") as fh:
        text = fh.read()
    return text


def write_files(file_name: str, data: str):
    file_name = project_file(file_name)

    with open(file_name, "a+") as f:
        f.writelines(time.strftime("%d/%m/%Y %H:%M:%S"))
        f.writelines("\t")
        f.writelines(data)
        f.writelines("\n")


if __name__ == '__main__':
    print(read_file('app.py'))
