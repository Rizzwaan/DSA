from abc import ABC, abstractmethod


class AverageCalcuator(ABC):

    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Cant compute the average of zero item")

            return total_sum / num_items
        finally:
            self.dispose()

        @abstractmethod
        def has_next(self):
            pass

        @abstractmethod
        def next_item(self):
            pass

        def dispose(self):
            pass
