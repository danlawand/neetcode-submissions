class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        # number of chars str
        for s in strs:
            n = len(s)
            n_digits = len(str(n))
            encoded = encoded+f"{n_digits}{len(s)}{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        response = []
        start = 0
        print(s)
        print(len(s))
        end = len(s)
        while start < end:
            n_digits = int(s[start])
            numChar = int(s[start+1:start+n_digits+1])
            response.append(s[start+n_digits+1:start+n_digits+numChar+1])
            start += n_digits+numChar+1
        return response