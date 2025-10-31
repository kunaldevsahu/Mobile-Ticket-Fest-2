def rob( nums):
    rob, norob = 0, 0
    for num in nums:
        newRob = norob + num
        newNoRob = max(norob, rob)
        rob, norob = newRob, newNoRob
    return max(rob, norob)
nums=list(map(int,input().split()))
