class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            prev_cost, curr_gas, j = cost[i], gas[i], i
            while curr_gas > 0:
                j = (j + 1) % len(gas)
                curr_gas = curr_gas - prev_cost
                if curr_gas < 0: break
                prev_cost, curr_gas = cost[j], curr_gas + gas[j]
                if j == i: return i
        return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            curr_gas, j = None, i
            while curr_gas == None or curr_gas >= 0:
                if j == i and curr_gas != None: return i
                curr_gas = gas[j] if curr_gas == None else curr_gas + gas[j]
                curr_gas = curr_gas - cost[j]
                j = (j + 1) % len(cost)
        return -1