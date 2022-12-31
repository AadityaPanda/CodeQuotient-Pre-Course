def reverseKElementsQueue(self, k: int) -> None:
  for i in range(k // 2):
    self.queue[i], self.queue[k - 1 - i] = self.queue[k - 1 - i], self.queue[i]