class Solution:
    def countAndSay(self, n: int) -> str:
        def rec(seq, m):
            if m == 1:
                return seq
            next_seq = list()
            l = len(seq)
            i = 0
            seq = seq + ' '
            while i < l:
                count = 1
                while seq[i] == seq[i + 1]:
                    count += 1
                    i += 1
                next_seq.append(str(count) + seq[i])
                i += 1

            return rec(''.join(next_seq), m - 1)

        return rec('1', n)


print(Solution().countAndSay(4))
