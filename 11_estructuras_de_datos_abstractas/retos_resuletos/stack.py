class Stack:
  def __init__(self):
    self.__stack = []

  def add(self, value):
    self.__stack.append(value)

  def pop(self):
    return self.stack.pop()

  def __len__(self):
    return len(self.__stack)

  @property
  def is_empty(self):
    return self.__stack == []

  @property
  def top(self):
    if len(self.__stack):
            return self.__stack[-1]
        return None
