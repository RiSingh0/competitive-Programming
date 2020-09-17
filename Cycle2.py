class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast=head
        slow=head
        while True:
            fast=fast.next.next if fast.next else None
            slow=slow.next
            if fast == slow or fast == None:
                break
        if not fast:
            return None
        fast=head
       
        while fast != slow:
            fast=fast.next
            slow=slow.next
        return slow
