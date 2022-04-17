"""
1) /sum_of_two accepting array of integers of any size using GET parameters.
Response of this function can be true only if sum of any two parameters equals the last one.
For example
    [1,2] returns False
    [1, 2, 3] returns True
    [1, 2, 4, 7] return False
    [1, 3, 5, 7, 9, 10] returns True
"""


def sum_of_two(arr: list) -> bool:
    for i in range(len(arr[:-1])):
        for j in range(len(arr[i-1:-1])):
            if arr[i] + arr[j] == arr[-1]:
                return True
    return False


if __name__ == '__main__':
    assert sum_of_two([1, 2]) == False
    assert sum_of_two([1, 2, 3]) == True
    assert sum_of_two([1, 2, 4, 7]) == False
    assert sum_of_two([1, 3, 5, 7, 9, 10]) == True
    assert sum_of_two([2, 3, 5]) == True
