class StackNode:
    def __init__(self, value):
        self.value = value
        self.next_pointer = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self.stack_size = 0

    def push(self, value):
        if self.top == None:  # Stack是空的
            self.top = StackNode(value)
        else:  # 已經self.top在Stack內
            new_node = StackNode(value)
            new_node.next_pointer = self.top  # 舊的next要連接上去
            self.top = new_node  # 新的top
            self.stack_size += 1

    def pop(self):  # 把最上面的拿出來，換二哥上
        if self.top == None:
            return None
        else:
            node = self.top
            self.top = self.top.next_pointer
            self.stack_size -= 1
            return node.value

    def peeK(self):
        # if self.top == None:
        #   return node
        # else:
        #   return self.top.value if self.top else None
        return self.top.value if self.top else None

    def size(self):
        return self.stack_size

    def trace_overall(self):
        trace_node = self.top
        while trace_node:
            print(f"|{trace_node.value:4}|")  # 靠左對齊 最多容納4位數
            trace_node = trace_node.next_pointer
        print("-" * 6)


class LinkedStackByList:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    def size(self):
        return len(self.stack)

    def trace_overall(self):
        print(self.stack)


if __name__ == '__main__':

    # linked_stack = LinkedStack()
    linked_stack = LinkedStackByList()
    linked_stack.push(1)
    linked_stack.push(2)
    linked_stack.push(4)
    print("Peek:", linked_stack.peek())
    linked_stack.push(116)
    print("Peek:", linked_stack.peek())
    linked_stack.trace_overall()  # (由1開始推到頂端，由後往前看)
    print("Pop:", linked_stack.pop())
    print("Pop:", linked_stack.pop())
    print("Peek:", linked_stack.peek())
    print("Pop:", linked_stack.pop())
    print("Pop:", linked_stack.pop())
    print("Peek:", linked_stack.peek())
