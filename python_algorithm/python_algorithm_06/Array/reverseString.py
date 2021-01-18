from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverseString1(self, s: List[str]) -> None:
        s.reverse() #리버스는 값을 반환해주지 않고 단순히 해당 list를 뒤섞음, None 반환
        return s #None 반환 대신 값 반환을 위해 사용
