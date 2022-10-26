#Sort
import random
import time
a = [i for i in range(1,10000001)]
b = [i for i in range(10000000,0)]
c = [i for i in range(random.randrange(1,10000001))]

# insertion
def insertion_sort(a):

    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

#0.93110 sec
start = time.time()
insertion_sort(a)
end = time.time()
print(f"{end-start:.5f} sec")

# 0.0003 sec
start = time.time()
insertion_sort(b)
end = time.time()
print(f"{end-start:.5f} sec")

#0.80010
start = time.time()
insertion_sort(c)
end = time.time()
print(f"{end-start:.5f} sec")

# merge
def merge_sort(a):
    if len(a) < 2:
        return a

    cen = len(a) // 2
    low_a = merge_sort(a[:cen])
    high_a = merge_sort(a[cen:])

    merged_list = []
    l = h = 0
    while l < len(low_a) and h < len(high_a):
        if low_a[l] < high_a[h]:
            merged_list.append(low_a[l])
            l += 1
        else:
            merged_list.append(high_a[h])
            h += 1
    merged_list += low_a[l:]
    merged_list += high_a[h:]
    return merged_list

# 19.69260 sec
start = time.time()
merge_sort(a)
end = time.time()
print(f"{end-start:.5f} sec")

# 0.00003 sec
start = time.time()
merge_sort(b)
end = time.time()
print(f"{end-start:.5f} sec")

# 16.49941 sec
start = time.time()
merge_sort(c)
end = time.time()
print(f"{end-start:.5f} sec")


# quick
def qsort(a, left, right):
    pl = left
    pr = right
    x = a[(left+right)//2]

    while pl <= pr:
        while a[pl] < x : pl +=1
        while a[pr] > x : pr -=1
        if pl <= pr:
            a[pl], a[pr] = a[pr],a[pl]
            pl +=1
            pr -=1
    if left < pr : qsort(a,left,pr)
    if pl < right: qsort(a,pl,right)

def quick_sort(a):
    qsort(a,0,len(a-1))

# 20.00457 sec
start = time.time()
merge_sort(a)
end = time.time()
print(f"{end-start:.5f} sec")

# 0.00003 sec
start = time.time()
merge_sort(b)
end = time.time()
print(f"{end-start:.5f} sec")

# 16.49171 sec
start = time.time()
merge_sort(c)
end = time.time()
print(f"{end-start:.5f} sec")

"""
2.
priority Queue
- 데이터들이 우선순위를 가지고 있고 우선순위가 높은 데이터가 먼저 나간다.
- 배열, 연결 리스트 등의 여러가지 방법으로 구현가능, 가장 효율적인 구조는 heap이다.
heap
- 완전이진트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다.
- 여러 개의 값들중에서 가장 큰값이나 가장 작은 값을 빠르게 찾아내도록 만들어진 자료구조이다.
* 다른 정렬들의 비해서 추가적인 배열이 필요하지않으며, 최대 최소값을 빠르게 찾아낼수있다. 

4.
카운터 정렬과 기수정렬이 가자 효율적일 때 
- 같은 숫자의 데이터들이 있어도 그 데이터들을 서로 비교하지
않기때문에 안정성을 가진다.

- 제한적인 부분은 임시작업으로 사용되는 메모리가 따로 필요하다.
"""

# 5.2D Peak Finder를 구현하시오.
def findPeakEle(a):
    left = 0
    right = len(a) -1

    if len(a) <=1: 
        return 0

    while (left < right):
        pivot = (left+right)/2
        num = a[pivot]
        nextNum = a[pivot+1]

        if num < nextNum:
            left = pivot +1
        else:
            right = pivot

    return left 

# 프로그래머스 실전 문제 풀이 
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    return str(int(''.join(numbers)))


