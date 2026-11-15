def rearrange_by_frequency(nums: list[int]) -> list[int]:

    a = []

    for i in nums:
        chastota = nums.count(i)
        a.append((-chastota, i))

    a.sort()

    result = []

    for i in a:
        result.append(i[1])

    return result


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))