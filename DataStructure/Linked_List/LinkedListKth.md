# White board
![cc7](./Untitled%20(11).jpg)

# Solution
```
 def kth_from_end(self, k):
        p1 = self.head
        p2 = self.head

        # Move the p1 pointer ahead by k positions
        for _ in range(k):
            if p1 is None:
                return None  # List is shorter than k elements
            p1 = p1.next

        # Move both the p1 and p2 pointers until the p1 pointer reaches the end
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next

        # Return the value of the node pointed to by the p2 pointer
        return p2.value
```