# mmtindicatorma.py
from mmtindicator import MMTIndicator

class MMTIndicatorMA(MMTIndicator):
    def __init__(self, length=21, offset=0, price_type=None):
        super().__init__(offset, price_type)
        self.m_length = length

    def __del__(self):
        pass

    def calculate(self, lines):
        count = len(lines)
        if count < self.m_length + self.m_offset:
            self.m_value = 0
            self.m_isValid = False
            return

        self.m_value = 0
        for index in range(self.m_length):
            self.m_value += lines[count - index - 1 - self.m_offset].getPrice(self.m_priceType)
        self.m_value /= self.m_length
        self.m_isValid = True