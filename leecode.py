"""题目： 给一非空的单词列表， 返回前K个出现的次数最多的单
 词，返回的答案按单词出现的频率由高到低的顺序进行排序
 如果不同的单词出现的频率相同，按字母的顺序进行排列"""




import collections
import operator
import heapq


class Solution1():
    def topFrequent(self, words, k):
        cn = [(-j, i) for i, j in collections.Counter(words).items()]

        # 使用了堆排序，当元组中的第一个元素相同时，直接怼第二个元素进行排序
        return [j[1] for j in heapq.nsmallest(k, cn)]


class Solution2():
    def topFrequent(self, words, k):
        cn = [(key, value) for key, value in collections.Counter(words).items()]

        #可以利用元组中的元素进行对按照第二个元素进行排序
        return [y[0] for y in sorted(cn, key=lambda x:(x[0], x[1]))[:k]]





if __name__ == '__main__':
    A = Solution1()
    ret = A.topFrequent(["i", "love", "leetcode", "i", "love", "b", "coding", "i", "coding", "b", "b", "coding"], 3)
    print(ret)


