class solution:
     
     def add_two_numbers(self, l1: listnode, l2: listnode)-> listnode:
          
          dummy = listnode()
          curr = dummy
          
          while l1 or l2:
               v1 = l1.val if l1 else 0
               v2 = l2.val if l2 else 0
               
               val = v1 + v2 + carry
               carry = val // 10
               val = val % 10
               
               curr.next = listnode(Val)
               
               curr = curr.next 
               
               l1 = l1.next if l1 else None
               l2 = l2.next if l2 else None
               
          return dummy.next
          
               
               

     