from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []  # 문자, 숫자 구분

        for log in logs:
            if log.split()[1].isdigit():  # 숫자로 변환 가능한지 확인
                digits.append(log)  # 변환되면 digits에 추가
            else:  # 변환되지 않으면 letters에 추가
                letters.append(log)

        # 두 개의 키를 람다 표현식으로 정렬
        # 식별자를 제외한 문자열 [1:]을 키로 정렬하며 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록 람자 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # 문자 + 숫자 순서로 이어 붙이고 return
        return letters + digits