class call:
    def __init__(self, start, end, using, n):
        self.start = start
        self.end = end
        self.using = using
        self.n = n
        self.left_call_done = False
        self.right_call_done = False

    def __str__(self):
        return f"{self.start} --> {self.end}"


def toh(start, end, using, n):
    call_stack = [call(start, end, using, n)]
    while call_stack != []:
        
        current_call = call_stack[-1]
        if (current_call.left_call_done) and (current_call.right_call_done):
            call_stack.pop(len(call_stack) - 1)
        elif not current_call.left_call_done:
            if current_call.n != 0:
                call_stack.append(
                    call(current_call.start, current_call.using,
                         current_call.end, current_call.n - 1))
            current_call.left_call_done = True
        elif not current_call.right_call_done:
            if current_call.n != 0:
                print(current_call)
                call_stack.append(
                    call(current_call.using, current_call.end,
                         current_call.start, current_call.n - 1))
            current_call.right_call_done = True


if __name__ == "__main__":
    toh("A", "C", "B", 3)
 