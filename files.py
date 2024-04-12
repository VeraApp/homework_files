def count_string(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        count = len(lines)
    return count


def read_files(filename):
    with open(filename, encoding='utf-8') as f:
        data = f.read()
    return data

def main():
    filesname = ['1.txt', '2.txt', '3.txt']
    dir_count_string_in_files = {}
    for filename in filesname:
        count_line = count_string(filename)
        dir_count_string_in_files[filename] = count_line
    sorted_files = sorted(dir_count_string_in_files.items(), key=lambda item:item[1])

    for filename, count_line in sorted_files:
        data = read_files(filename)
        with open('result.txt', 'a') as res:
            res.write(filename + '\n')
            res.write(str(count_line) + '\n')
            res.write(data + '\n')

if __name__ == "__main__":
    main()



