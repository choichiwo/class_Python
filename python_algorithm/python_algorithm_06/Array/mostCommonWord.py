import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()  # 소문자와 ' ' 기준으로 쪼개기
                 if word not in banned]  # banned를 제외한 단어 저장(예제에서는 hit)
        print('단어 처리: ', words)

        counts = collections.Counter(words)

        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        # (1)은 n을 의미하며, 2차원이므로 [0][0]을 이용
        return counts.most_common(1)[0][0]