'''In this question we are using mergesort to find the count of smaller number in the right direction'''


def countSmaller(nums):
    def solve(arr):
        half = len(arr)//2
        if half:
            left = solve(arr[:half])
            right = solve(arr[half:])
            for i in range(len(arr))[::-1]:
                if not right or left and left[-1][1]>right[-1][1]:
                    result[left[-1][0]] += len(right)
                    arr[i] = left.pop()
                else:
                    arr[i] = right.pop()

        return arr


    result = [0]*len(nums)
    solve(list(enumerate(nums)))
    return result


nums = [5,2,6,1]
print(countSmaller(nums))