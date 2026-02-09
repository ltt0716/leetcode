nums=[2,6,5,4,8,9,1,2,11,65,23,11,2,4,5,3,9,8,7,4,1,66]


def prti(l,r):
    if l>=r:
        return
    print(l,r)
    privot=nums[r]
    print(nums)

    i=l-1
    for j in range(l,r):
        if nums[j]<=privot:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]

    nums[i+1],nums[r]=nums[r],nums[i+1]
    # return 
    prti(l,i)
    prti(i+2,r)

                

def quicksort():
    l,r=0,len(nums)-1
    prti(l,r)



quicksort()
print(nums)
