# mmtindicatormacd.py
from mmtindicator import MMTIndicator

class MMTIndicatorMACD(MMTIndicator):
    def __init__(self, short_length=12, long_length=26, diff_length=9, offset=0, price_type=None):
        super().__init__(offset, price_type)
        self.m_shortLength = short_length
        self.m_longLength = long_length
        self.m_diffLength = diff_length
        self.m_shortEma = 0
        self.m_longEma = 0
        self.m_diff = 0

    def __del__(self):
        pass

    def calculate(self, lines):
        count = len(lines)
        if count <= self.m_offset:
            self.m_isValid = False
            self.m_shortEma = 0
            self.m_longEma = 0
            self.m_diff = 0
            self.m_value = 0
            return

        if self.m_isValid:
            price = lines[count - 1 - self.m_offset].getPrice(self.m_priceType)
            self.m_shortEma = (self.m_shortEma * (self.m_shortLength - 1) + price * 2) / (self.m_shortLength + 1)
            self.m_longEma = (self.m_longEma * (self.m_longLength - 1) + price * 2) / (self.m_longLength + 1)
            self.m_diff = self.m_shortEma - self.m_longEma
            self.m_value = (self.m_value * (self.m_diffLength - 1) + self.m_diff * 2) / (self.m_diffLength + 1)
            self.m_isValid = True
            return

        self.m_shortEma = lines[0].getPrice(self.m_priceType)
        self.m_longEma = lines[0].getPrice(self.m_priceType)
        self.m_value = 0
        for index in range(1, count - self.m_offset):
            price = lines[index].getPrice(self.m_priceType)
            self.m_shortEma = (self.m_shortEma * (self.m_shortLength - 1) + price * 2) / (self.m_shortLength + 1)
            self.m_longEma = (self.m_longEma * (self.m_longLength - 1) + price * 2) / (self.m_longLength + 1)
            self.m_diff = self.m_shortEma - self.m_longEma
            self.m_value = (self.m_value * (self.m_diffLength - 1) + self.m_diff * 2) / (self.m_diffLength + 1)
        self.m_isValid = True