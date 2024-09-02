class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        deriv = sentence.split()

        for idx, d in enumerate(deriv):
            root_len = 101
            ans = d
            for root in dictionary:
                if d[:len(root)] == root:
                    if len(root) < root_len:
                        root_len = len(root)
                        ans = root

            deriv[idx] = ans

        return ' '.join(deriv)