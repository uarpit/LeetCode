#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:33:09 2020
Given a sorted array nums, remove the duplicates in-place 
such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.
@author: arpit
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        junk = len(nums)
        for i in range(0,len(nums)):
            if nums[i] != prev:
                if junk < i:
                    prev = nums[i]
                    nums[junk],nums[i] = nums[i],nums[junk]
                    junk +=1
                else:
                    prev = nums[i]
            else:
                if junk <= i:
                    pass
                else:
                    junk = i
                
        return junk
    
if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    
    for i in range(0,s.removeDuplicates(nums)):
        print(nums[i],end=" ")