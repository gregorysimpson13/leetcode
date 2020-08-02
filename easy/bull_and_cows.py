class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess_miss, secret_miss = defaultdict(int), defaultdict(int)
        a, b = 0, 0
        for s, g in zip(secret, guess):
            if s == g: a = a+1
            else:
                guess_miss[g] += 1
                secret_miss[s] += 1
        for key, val in secret_miss.items():
            b = b + min(val, guess_miss[key])
        return "{}A{}B".format(a,b)