class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:

            # left가 0보다 크고 right가 글자 수보다 작거나 같고 s[left] == s[오른쪽-1]이면 반복
            # s[left] == s[ringt-1]: 짝수 expand는 "bb", 홀수 expand는 "bab"를 찾기 위함
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # 슬라이싱은 n-1 위치 출력, 인덱스는 n 위치 출력
                left -= 1
                right += 1

            # while문에서 팰린드롬을 찾았을 때 -1 했으므로 반대로 해주는 것
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 슬라이딩 윈도우 우측으로 이동
        # 제일 긴 펠린드롬을 result에 저장하고 더 긴것을 찾으면 갱신
        # max( key=len) 필수, 글자수를 기준으로 max값 선별
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),  # 짝수 투포인터
                         expand(i, i + 2),  # 홀수 투포인터
                         key=len)
        return result