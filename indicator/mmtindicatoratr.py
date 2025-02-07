# mmtindicatoratr.py
from mmtindicator import MMTIndicator

class MMTIndicatorATR(MMTIndicator):
    def __init__(self, length=14, offset=0):
        super().__init__(offset)
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
            temp = count - self.m_length - self.m_offset + index
            true_high = lines[temp].m_high
            true_low = lines[temp].m_low
            if temp > 0:
                if true_high < lines[temp - 1].m_close:
                    true_high = lines[temp - 1].m_close
                if true_low > lines[temp - 1].m_close:
                    true_low = lines[temp - 1].m_close
            self.m_value += (true_high - true_low)
        self.m_value /= self.m_length
        self.m_isValid = True