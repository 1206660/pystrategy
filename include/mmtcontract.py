# mmtcontract.py

# 假设 mmtdatatype 模块中定义了相应的枚举类型
# 这里简单用整数常量代替，实际使用时需要根据具体情况调整

from mmtdatatype import MMT_TAT_NULL, MMT_EX_NULL, MMT_DT_NULL, MMT_CT_NULL

PRECISION = 0.000001

class MMTContract:
    def __init__(self):
        self.m_id = ""
        self.m_name = ""
        self.m_type = MMT_CT_NULL
        self.m_deliveryType = MMT_DT_NULL
        self.m_exchange = MMT_EX_NULL
        self.m_tradeApiType = MMT_TAT_NULL
        self.m_priceTick = 0
        self.m_volumeMultiple = 0
        self.m_minVolume = 0
        self.m_leverageRatio = 1
        self.m_takerCommissionRate = 0
        self.m_makerCommissionRate = 0

    # 价格按照 price_tick 向上取整
    def ceilToPriceTick(self, price):
        return (int((price - PRECISION) / self.m_priceTick) + 1) * self.m_priceTick

    # 价格按照 price_tick 向下取整
    def floorToPriceTick(self, price):
        return int((price + PRECISION) / self.m_priceTick) * self.m_priceTick

    # 价格按照 price_tick 四舍五入取整
    def roundToPriceTick(self, price):
        return round(price / self.m_priceTick) * self.m_priceTick

    # 成交量按照 min_volume 向上取整
    def ceilToMinVolume(self, volume):
        return (int((volume - PRECISION) / self.m_minVolume) + 1) * self.m_minVolume

    # 成交量按照 min_volume 向下取整
    def floorToMinVolume(self, volume):
        return int((volume + PRECISION) / self.m_minVolume) * self.m_minVolume

    # 成交量按照 min_volume 四舍五入取整
    def roundToMinVolume(self, volume):
        return round(volume / self.m_minVolume) * self.m_minVolume

# 重载 == 运算符
def __eq__(contract1, contract2):
    return contract1.m_id == contract2.m_id and contract1.m_exchange == contract2.m_exchange

# 重载 < 运算符
def __lt__(contract1, contract2):
    if contract1.m_exchange < contract2.m_exchange:
        return True
    elif contract1.m_exchange > contract2.m_exchange:
        return False
    return contract1.m_id < contract2.m_id

# 定义哈希函数
def qHash(contract, seed=0):
    result = hash(contract.m_id) ^ seed
    result ^= hash(contract.m_exchange) ^ seed
    return result