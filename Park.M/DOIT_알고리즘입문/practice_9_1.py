#이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, value: Any, left: Node = None,
                 right: Node = None):
        """생성자(constructor)"""
        self.key = key                                                #키
        self.value = value                                            #값
        self.left = left                                              #왼쪽 포인터
        self.right = right                                            #오른쪽 포인터

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None                                              #루트             / 빈 상태의 이진 검색트리 생성

    def search(self, key: Any) -> Any:
        """키가 key인 노드를 검색"""
        p = self.root                                                 #루트에 주목
        while True:
            if p is None:                                             #더 이상 진행할 수 없으면
                return None                                           #검색 실패
            if key == p.key:                                          #key와 노드 p의 키가 같으면
                return p.value                                        #검색 성공
            elif key < p.key:                                         #key 쪽이 작으면
                p = p.left                                            #왼쪽 서브트리에서 검색
            else:                                                     #key 쪽이 크면
                p = p.right                                           #오른쪽 서브트리에서 검색

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 노드를 삽입"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입"""
            if key == node.key:
                return False                                          #key가 이진 검색 트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:                                         #트리가 빈 상태일 경우
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)                    #재귀호출
        
    def remove(self, key: Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root                                                 # 스캔 중인 노드
        parent = None                                                 # 스캔 중인 노드의 부모노드
        is_left_child = True                                          # p는 parent의 왼쪽 자식 노드인지 확인
        
        while True:
            if p is None:                                             # 더 이상 진행할 수 없으면
                return False                                          # 그 키는 존재하지 않음
            
            if key == p.key:                                          #key와 노드p의 키가 같으면
                break                                                 #검색 성공
            
            else:
                parent = p                                            #가지를 내려가기 전에 부모를 설정
                if key < p.key:                                       #key 쪽이 작으면
                    is_left_child = True                              #여기서 내려가는 것은 왼쪽 자식
                    p = p.left                                        #왼쪽 서브트리에서 검색
                else:                                                 #key 쪽이 크면
                    is_left_child = False                             #여기서 내려가는 것은 오른쪽 자식
                    p = p.right                                       #오른쪽 서브트리에서 검색
              
        if p.left is None:                                            #p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right