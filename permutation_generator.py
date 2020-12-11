def customPermutationGenerator(nums):
    if nums!=[]:
        for i in range(1,len(nums)):
            if nums[0]!=nums[i]:
                nums[0],nums[i]=nums[i],nums[0]
            else:continue
if __name__ == "__main__":
    data=[1,0,1,0,2,3,4,5]
    for i in customPermutationGenerator(data):
        print(i)