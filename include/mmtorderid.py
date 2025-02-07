# 定义 MMTTradeApiType 为枚举类型，这里简单用整数常量表示

from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType


# 定义 MMTOrderId 类
class MMTOrderId:
    def __init__(self, fundId="", accountId="", tradeApiType=MMTTradeApiType.MMT_TAT_NULL, strategyId="", localOrderId=""):
        # 初始化各个属性
        self.m_fundId = fundId
        self.m_accountId = accountId
        self.m_tradeApiType = tradeApiType
        self.m_strategyId = strategyId
        self.m_localOrderId = localOrderId

    def __eq__(self, other):
        # 重载 == 运算符，用于比较两个 MMTOrderId 对象是否相等
        if isinstance(other, MMTOrderId):
            return (self.m_fundId == other.m_fundId and
                    self.m_accountId == other.m_accountId and
                    self.m_tradeApiType == other.m_tradeApiType and
                    self.m_strategyId == other.m_strategyId and
                    self.m_localOrderId == other.m_localOrderId)
        return False

    def __hash__(self):
        # 重载 __hash__ 方法，用于计算对象的哈希值
        result = hash(self.m_fundId)
        result ^= hash(self.m_accountId)
        result ^= hash(self.m_tradeApiType)
        result ^= hash(self.m_strategyId)
        result ^= hash(self.m_localOrderId)
        return result