#비재귀적인 퀵 정렬 구현하기

from practice_4C_1 import Stack
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left]~a[right]를 퀵 정렬(비재귀적인 퀵 정렬)"""
    range= Stack(right-left+1)                                    #스택 생성

    range.push((left, right))                                     #여기서 (left, right) 는 튜플이다

    while not range.is_empty():
        pl, pr = left, right = range.pop()                        #왼쪽, 오른쪽 커서 꺼냄
        x = a[(left+right)//2]                                    #피벗

        while pl<=pr:
            while a[pl] < x: pl+= 1
            while a[pr] < x: pr-= 1
            if pl<=pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))                      #왼쪽 그룹의 커서를 저장
        if pl < right: range.push((pl, right))                    #오른쪽 그룹의 커서를 저장

#이하생략..