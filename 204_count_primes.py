    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        vec = [1 for _ in range(n)]
        
        for num in range(2, n):
            if vec[num] == 1:
                for j in range(num*2, n, num):
                    vec[j] = 0
        return sum(vec) - 2
    