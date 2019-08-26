#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Sort:
    temp = 0

    def sort1(self, nums):
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[j]>nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        for i in nums:
            print(i)

if __name__ == '__main__':
    s = Sort()
    s.sort1([7,4,2,8])
