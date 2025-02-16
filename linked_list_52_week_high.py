class Node:
    def _init_(self, price):
        self.price = price
        self.next = None

def find_52_week_high(head):
    max_price = float('-inf')
    current = head
    
    while current:
        if current.price > max_price:
            max_price = current.price
        current = current.next
    
    return max_price
