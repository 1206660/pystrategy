# 导入 Python 中的 datetime 模块，用于处理日期和时间
from datetime import datetime

from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType


# 定义 MMTOrderInfo 类
class MMTOrderInfo:
    def __init__(self):
        # 初始化各个属性
        self.m_fundId = ""
        self.m_strategyId = ""
        self.m_accountId = ""
        self.m_tradeApiType = MMTTradeApiType.MMT_TAT_NULL
        self.m_contractId = ""
        self.m_exchangeId = ""
        self.m_localOrderId = ""
        self.m_combinationId = ""
        self.m_legId = ""
        self.m_price = 0.0
        self.m_volume = 0.0
        self.m_direction = MMTTradeApiType.MMT_TD_NULL
        self.m_orderType = MMTTradeApiType.MMT_OT_NULL
        self.m_stopPrice = 0.0
        self.m_isPassive = False
        self.m_orderTime = datetime.now()