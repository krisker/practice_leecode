import collections
import operator
import heapq


class Solution():
    def topFrequent(self, words, k):
        cn = [(-j, i) for i, j in collections.Counter(words).items()]

        # 使用了堆排序，当元组中的第一个元素相同时，直接怼第二个元素进行排序
        return [j[1] for j in heapq.nsmallest(k, cn)]



if __name__ == '__main__':
    A = Solution()
    ret = A.topFrequent(["i", "love", "leetcode", "i", "love", "b", "coding", "i", "coding", "b", "b", "coding"], 3)
    print(ret)


