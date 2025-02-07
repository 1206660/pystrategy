# 导入Python的datetime模块，用于处理日期和时间
from datetime import datetime

from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType

class MMTTickData:
    def __init__(self):
        # 初始化类的属性
        self.m_contractId = ""
        self.m_exchange = MMTExchange.MMT_EX_NULL
        self.m_time = datetime.now()
        self.m_latestPrice = 0
        self.m_volume = 0
        self.m_turnover = 0
        self.m_openInterest = 0
        self.m_bidPrice1 = 0
        self.m_bidPrice2 = 0
        self.m_bidPrice3 = 0
        self.m_bidPrice4 = 0
        self.m_bidPrice5 = 0
        self.m_bidVolume1 = 0
        self.m_bidVolume2 = 0
        self.m_bidVolume3 = 0
        self.m_bidVolume4 = 0
        self.m_bidVolume5 = 0
        self.m_askPrice1 = 0
        self.m_askPrice2 = 0
        self.m_askPrice3 = 0
        self.m_askPrice4 = 0
        self.m_askPrice5 = 0
        self.m_askVolume1 = 0
        self.m_askVolume2 = 0
        self.m_askVolume3 = 0
        self.m_askVolume4 = 0
        self.m_askVolume5 = 0
        self.m_upperLimitPrice = 0
        self.m_lowerLimitPrice = 0