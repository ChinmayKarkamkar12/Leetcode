class Solution:
    def can_place(self, stalls, k, distance):
        count = 1
        last = stalls[0]
        for pos in stalls[1:]:
            if pos - last >= distance:
                count += 1
                last = pos
                if count == k:
                    return True
        return False

    def maxDistance(self, stalls, k):
        stalls.sort()
        low = 0
        high = stalls[-1] - stalls[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.can_place(stalls, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans