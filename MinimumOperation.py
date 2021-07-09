'''Minimum increment/decrement operation to make all the elements equal in array'''


def minimumOperation(nums):
    n = len(nums)

    cost = 0

    nums.sort()

    k = nums[int(n//2)]

    for i in range(n):
        cost = cost+abs(nums[i]-k)


    if n%2 == 0:
        tempCost = 0
        k = nums[int(n//2)-1]

        for i in range(n):
            tempCost = tempCost + abs(nums[i]-k)

        cost = min(cost,tempCost)

    return cost


nums = [3, 4, 2, 11]
print(minimumOperation(nums))
