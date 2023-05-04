from gg import mapath, file_name
from pympler import asizeof 

def find_in_file (pattern: str):
    with open(mapath,'r+') as file:
        file.truncate(0)
    with open(file_name, 'r', encoding='latin-1') as file, open(mapath, 'a') as file2:
        while True:
            line = file.readline()
            if pattern in line:
                file2.write(line)
                yield line
            elif not line:
                break
    with open(mapath, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
    print("Size of the file: %d bytes" %asizeof.asizeof(mapath))
    with open(mapath, 'r', encoding='latin-1') as res:
        lines = len(res.readlines())
    print('Total Number of lines:', lines)
results = find_in_file(
    pattern = input("enter a line: "),)
data = list(results)



