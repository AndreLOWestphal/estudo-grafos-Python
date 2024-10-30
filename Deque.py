from collections import deque

deque_objeto = deque()

deque_objeto.append(1)
deque_objeto.append(2)
deque_objeto.appendleft(0)

print(f'Deque: ', deque_objeto)

print(f'Removendo elementos do deque: ')
print(deque_objeto.pop())
print(deque_objeto.popleft())