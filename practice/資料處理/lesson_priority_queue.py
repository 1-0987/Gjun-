import random


class MemberInQueue:
    def __init__(self, name):
        self.name = name
        self.weight = random.randint(1, 100)


class PriorityQueue:
    def __init__(self):
        self.pqueue = list()

    def enqueue(self, name):
        member = MemberInQueue(name)
        self.pqueue.append(member)
        self.pqueue.sort(key=lambda x: x.weight, reverse=True)

    def dequeue(self):
        x = self.pqueue[0]
        self.pqueue.reverse()
        self.pqueue.pop()
        self.pqueue.reverse()
        return x if len(self.pqueue) > 0 else None

    def trace_overall(self):
        print([(member.name, member.weight) for member in self.pqueue])


if __name__ == "__main__":
    member_priority_queue = PriorityQueue()
    member_priority_queue.enqueue("Peter")
    member_priority_queue.trace_overall()
    member_priority_queue.enqueue("Marry")
    member_priority_queue.trace_overall()
    member_priority_queue.enqueue("George")
    member_priority_queue.trace_overall()
    x = member_priority_queue.dequeue()
    print(x.name, x.weight)
    member_priority_queue.trace_overall()
