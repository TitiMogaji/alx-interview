#!/usr/bin/python3 
 """ 
 This is a module that provides a function for determining if all 
 boxes in a given list can be opened. 
 """ 
  
  
 def canUnlockAll(boxes): 
     """ 
     Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    
     """ 
     n = len(boxes) 
     seen_boxes = set([0]) 
     unseen_boxes = set(boxes[0]).difference(set([0])) 
     while len(unseen_boxes) > 0: 
         boxIdx = unseen_boxes.pop() 
         if not boxIdx or boxIdx >= n or boxIdx < 0: 
             continue 
         if boxIdx not in seen_boxes: 
             unseen_boxes = unseen_boxes.union(boxes[boxIdx]) 
             seen_boxes.add(boxIdx) 
     return n == len(seen_boxes

def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
