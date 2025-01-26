class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub('[^a-zA-Z0-9]','',s.lower())
        for n in range(len(string)//2):
            if string[n] != string[len(string)-n-1]:
                return False
        return True