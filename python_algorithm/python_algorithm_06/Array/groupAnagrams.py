import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 키를 삽입하려 할 경우, keyError 발생
        # default를 list로 설정하여 .append 기능 사용하기
        # value 값은 list 디폴트
        anagrams = collections.defaultdict(list)
        print('anagrams 확인: ', anagrams)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            # sorted()는 문자열도 정렬하며 결과를 리스트 형태로 리턴함
            # 리턴된 리스트 형태를 키로 사용하기 위해 join()으로 합치고 이를 키로 하는 딕셔너리 구성
            # list는 key 값을 쓰지 못하기 때문에 join() 함수는 리스트를 문자열로 바꾸게 됨
            # ' ': 문자 사이에 공백 추가
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())