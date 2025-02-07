# 假设 mmtdatatype 和 mmtorderinfo 模块已经存在，并且定义了相应的类型和常量
# 例如 MMT_TAT_NULL, MMT_TD_NULL, MMT_OT_NULL, MMT_OS_NULL 等

import mmtdatatype

class MMTOrder:
    def __init__(self, order_info=None):
        if order_info is None:
            # 对应 C++ 中的默认构造函数
            self.m_tradeApiType = MMT_TAT_NULL
            self.m_orderPrice = 0.0
            self.m_orderVolume = 0.0
            self.m_direction = MMT_TD_NULL
            self.m_orderType = MMT_OT_NULL
            self.m_filledPrice = 0.0
            self.m_filledVolume = 0.0
            self.m_unfilledVolume = 0.0
            self.m_cancelledVolume = 0.0
            self.m_rejectedVolume = 0.0
            self.m_orderStatus = MMT_OS_NULL
        else:
            # 对应 C++ 中的带参数构造函数
            self.m_fundId = order_info.m_fundId
            self.m_accountId = order_info.m_accountId
            self.m_tradeApiType = order_info.m_tradeApiType
            self.m_strategyId = order_info.m_strategyId
            self.m_contractId = order_info.m_contractId
            self.m_exchangeId = order_info.m_exchangeId
            self.m_localOrderId = order_info.m_localOrderId
            self.m_orderPrice = order_info.m_price
            self.m_orderVolume = order_info.m_volume
            self.m_direction = order_info.m_direction
            self.m_orderType = order_info.m_orderType
            self.m_filledPrice = 0
            self.m_filledVolume = 0
            self.m_unfilledVolume = order_info.m_volume
            self.m_cancelledVolume = 0
            self.m_rejectedVolume = 0
            self.m_orderStatus = MMT_OS_NULL

        # 其他成员变量
        self.m_systemId = ""
        self.m_exchangeId = ""
        self.m_frontId = ""
        self.m_sessionId = ""
        self.m_orderRef = ""
        self.m_orderTime = None
        self.m_filledPrice = 0.0
        self.m_filledVolume = 0.0
        self.m_lastFilledTime = None
        self.m_unfilledVolume = 0.0
        self.m_cancelledVolume = 0.0
        self.m_cancelledTime = None
        self.m_rejectedVolume = 0.0
        self.m_rejectedTime = None
        self.m_untriggeredTime = None