class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def min_cost(day_i=0, curr_cost=0):
            if day_i >= len(days): return curr_cost
            day_pass = min_cost(day_i+1, curr_cost+costs[0])
            i = mi = wi = day_i
            while wi < len(days) and days[wi] - days[i] < 7: wi += 1
            week_pass = min_cost(wi, curr_cost+costs[1])
            while mi < len(days) and days[mi] - days[i] < 30: mi += 1
            month_pass = min_cost(mi, curr_cost+costs[2])
            return min(day_pass, week_pass, month_pass)
        return min_cost()