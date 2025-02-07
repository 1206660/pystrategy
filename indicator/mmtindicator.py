# mmtindicator.py

class MMTIndicator:
    def __init__(self, offset=0, price_type=None):
        self.m_value = 0
        self.m_isValid = False
        self.m_offset = offset
        self.m_priceType = price_type

    def __del__(self):
        pass

    def calculate(self, lines):
        raise NotImplementedError("Subclasses should implement this method")