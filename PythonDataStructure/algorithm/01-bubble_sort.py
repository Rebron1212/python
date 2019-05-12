
# coding: utf-8


"""
冒泡排序：
一个一个的往后冒泡, 每次冒泡都会将序列中最大的数冒到最后
加入现在又拿一个序列  [33,12,4,34,32,3,66,5]
两个两个的比较，只要前者比后者大，就交换位置，如下：
第一趟：33 和 12 比，前者大，故交换位置，第一趟的第一次比较后是12,33,4,..,5
第二次比较是第二个和第三个比，即 33 和 4 比较，前者大，交换位置12,4,33,34..
第三次比较是第三个和第四个比，即 33 和 34 比较，后者大，不用交换位置12,4,33,34..
第四次比较是第四个和第五个比，即 34 和 32 比较，前者大，交换位置12,4,33,32,34,3..
...
第一趟比较结束后的结果是 [12,4,33,32,3,34,5,66]

再重复上述操作，
第二趟的结果是 [4,12,32,3,33,5,34,66]

每一趟比较完后被冒出的不再比较，因为已经最大了，就没必要再比较了

考虑特出情况，如果已经排好了就不再进行比较了

写代码思路：
首先看第一趟，开始第一个和第二个比较，然后第二个和第三个比较。。。第n-1和第n个比较
即，如果有n个数，第一趟需要比较n-1次
第二趟比较又是从头开始，只是最后一个不用比较了，所以共比较n-2次
。。。
最坏的情况下最后一趟也就只比较一次了

"""
def bubble_sort(alist):
	
	for j in range(len(alist)-1):
		count = 0
		for i in range(0, len(alist)-1-j):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				count += 1
				print(count)
		if 0 == count:
			return


if __name__ == '__main__':
	# alist = [33,12,4,34,32,3,66,5]
	alist = [1,2,3,4,5,6,7]
	bubble_sort(alist)
	print(alist)



