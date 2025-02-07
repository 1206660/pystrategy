# mmttrade.py
from dataclasses import dataclass
from datetime import datetime

# 假设这些枚举类型在其他文件中定义，这里简单模拟

from mmtdatatype import MMT_TAT_NULL, MMT_TD_NULL, MMT_OT_NULL

@dataclass
class MMTTrade:
    m_fundId: str = ""
    m_accountId: str = ""
    m_tradeApiType: int = MMT_TAT_NULL
    m_strategyId: str = ""
    m_localOrderId: str = ""
    m_contractId: str = ""
    m_direction: int = MMT_TD_NULL
    m_orderType: int = MMT_OT_NULL
    m_price: float = 0.0
    m_volume: float = 0.0
    m_time: datetime = datetime.now()
    m_frontId: str = ""
    m_sessionId: str = ""
    m_orderRef: str = ""
    m_systemId: str = ""
    m_tradeId: str = ""
    m_exchangeId: str = ""

    def __init__(self,
                 fundId="",
                 accountId="",
                 tradeApiType=MMT_TAT_NULL,
                 strategyId="",
                 localOrderId="",
                 contractId="",
                 direction=MMT_TD_NULL,
                 orderType=MMT_OT_NULL,
                 price=0.0,
                 volume=0.0,
                 time=datetime.now(),
                 frontId="",
                 sessionId="",
                 orderRef="",
                 systemId="",
                 tradeId="",
                 exchangeId=""):
        self.m_fundId = fundId
        self.m_accountId = accountId
        self.m_tradeApiType = tradeApiType
        self.m_strategyId = strategyId
        self.m_localOrderId = localOrderId
        self.m_contractId = contractId
        self.m_direction = direction
        self.m_orderType = orderType
        self.m_price = price
        self.m_volume = volume
        self.m_time = time
        self.m_frontId = frontId
        self.m_sessionId = sessionId
        self.m_orderRef = orderRef
        self.m_systemId = systemId
        self.m_tradeId = tradeId
        self.m_exchangeId = exchangeId