#230810(THUR)
#014. 절댓값 힙 구현하기(백준 실버1 11286번)

from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:   #절댓값을 기준으로 정렬하고 같으면 음수 우선정렬
        myQueue.put((abs(request),request))