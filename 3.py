def rearrange_by_frequency(nums: list[int]) -> list[int]:

    a=sorted(nums)
    sum=0
    x=set()
    for i in a:
        a.count(i)
        x.add(a.count(i))

    print(x)


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))