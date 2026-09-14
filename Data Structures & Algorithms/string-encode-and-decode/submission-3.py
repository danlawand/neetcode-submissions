class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            n = len(s)
            n_digits = len(str(n))
            encoded_string = f"{encoded_string}{n_digits}{n}{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        n = len(s)
        pointer = 0
        response = []
        while pointer < n:
            n_digits = int(s[pointer])
            numChar = int(s[pointer+1:pointer+n_digits+1])
            response.append(s[pointer+n_digits+1:pointer+n_digits+numChar+1])
            pointer+=n_digits+numChar+1
        return response