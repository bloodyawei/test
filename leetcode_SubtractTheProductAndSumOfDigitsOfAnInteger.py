class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_ = str(n)
        product=1
        summary=0
        for i in range(len(n_)):
            product *= int(n_[i])
            summary += int(n_[i])
        return product-summary