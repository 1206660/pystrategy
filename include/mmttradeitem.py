
from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType

from datetime import datetime

class MMTTradeItem:
    def __init__(self):
        # 初始化类的属性
        self.m_fundId = ""
        self.m_accountId = ""
        self.m_tradeApiType = MMTTradeApiType.MMT_TAT_NULL
        self.m_strategyId = ""
        self.m_contractId = ""
        self.m_contractType = MMTTradeApiType.MMT_CT_NULL
        self.m_localOrderId = ""
        self.m_combinationId = ""
        self.m_legId = ""
        self.m_orderPrice = 0
        self.m_orderVolume = 0
        self.m_direction = MMTTradeApiType.MMT_TD_NULL
        self.m_orderType = MMTTradeApiType.MMT_OT_NULL
        self.m_systemId = ""
        self.m_exchangeId = ""
        self.m_orderRef = ""
        self.m_tradeId = ""
        self.m_orderTime = datetime.now()
        self.m_filledPrice = 0
        self.m_filledVolume = 0
        self.m_filledTime = datetime.now()
        self.m_unfilledVolume = 0
        self.m_cancelledVolume = 0
        self.m_cancelledTime = datetime.now()
        self.m_rejectedVolume = 0
        self.m_rejectedTime = datetime.now()
        self.m_untriggeredTime = datetime.now()
        self.m_orderStatus = MMTTradeApiType.MMT_OS_NULL
        self.m_realizedPnl = 0
        self.m_floatingPnl = 0
        self.m_totalPnl = 0
        self.m_commission = 0
        self.m_slippage = 0