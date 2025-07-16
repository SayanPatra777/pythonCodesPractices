nums=[3,2,2,3]
val=3
count=nums.count(val)
print(count)
for i in range(count):
    nums.remove(val)
print(nums)