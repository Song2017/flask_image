def write_files(file_name: str, data: str):
    with open(file_name, "a+") as f:
        f.write(data)
