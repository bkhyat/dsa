def get_num(n_rows):
    if n_rows == 0:
        return [[]]
    result = [[1]]
    for i in range(1, n_rows):
        current = [1]
        for j in range(1, i):
            current.append(result[i - 1][j - 1] + result[i - 1][j])
        current.append(1)

        result.append(current)

    return result

if __name__ == '__main__':
    num_rows = 1
    print(get_num(num_rows))