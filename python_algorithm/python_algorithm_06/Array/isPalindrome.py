import collections
from typing import Deque
import re #정규표현식 불러오기

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # isalnum(): 영문자, 숫자 여부 판별하여 False, True 변환
                strs.append(char.lower()) # 모든 문자 소문자 변환하여 str에 입력
                print('문자 처리: ', strs)

        # 팰린드롬 여부 판별
        while len(strs) > 1:  # strs의 길이가 1 이상이면 반복

            # pop(0): 맨 앞의 값, pop(): 맨 뒤의 값을 가져옴
            if strs.pop(0) != strs.pop():
                return False

    def isPalindrome1(self, s: str) -> bool:

        # 자료형 데크로 선언
        strs: Deque = collections.deque()  # 데크 생성
        print('\n데크 생성: ', strs)

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                print('문자 처리: ', strs)

        while len(strs) > 1:
            if strs.popleft() != strs.pop():  # 데크의 popleft()는 O(1), 리스트의 pop(0)이 O(n)
                return False
            return True

    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링: re.sub(''정규표현식', 대상 문자열, 치환 문자)
        s = re.sub('[^a-z0-9]', '', s) #s 중, 알파벳과 숫자가 아닌 것을 ''로 바꿔라
        print('\n문자 처리: ', s)

        return s == s[::-1]  # 슬라이싱 [::-1]: 배열 뒤집기