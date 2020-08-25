class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        temp=head
        while temp:
            new = Node(temp.val,temp.next,None)
            temp.next = new
            if temp.next:
                temp=temp.next.next
            else:
                temp=temp.next
        
        temp=head
        flip=0
        while temp:
            #print(temp.val)
            if flip == 0 and temp.next:
                new = temp.next
                new.random = temp.random.next if temp.random else None
            flip = 0 if flip == 1 else 0
            if temp.next:
                temp=temp.next.next
            else:
                temp=temp.next
        
        
        head1=head.next
        temp=head1
        while temp:
            if temp.next:
                temp.next=temp.next.next
            else:
                temp.next=None
            temp=temp.next
            
        return head1
