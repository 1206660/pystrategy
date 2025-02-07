# mmttradeapi.py
from typing import List, Dict, Callable
from dataclasses import dataclass

from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType

from include.mmtcontract import MMTContract
from include.mmtorder import MMTOrder
from include.mmtorderinfo import MMTOrderInfo
from include.mmtposition import MMTPosition
from include.mmtaccount import MMTAccount
from include.mmttrade import MMTTrade
from include.mmttickdata import MMTTickData
from include.mmtcommissionrate import MMTCommissionRate
from include.mmttradeapiinterface import MMTTradeApiInterface
from utility.mmtline import MMTLine


@dataclass
class MMTTradeApi:
    m_fundId: str = ""
    m_accountParameters: Dict = None
    m_subscribeContracts: set = None
    m_thread: bool = False  # 简单用布尔值模拟线程状态

    def __init__(self, parent=None):
        self.m_accountParameters = {}
        self.m_subscribeContracts = set()
        self.m_thread = False

    def getObject(self):
        return self

    def setFund(self, fundId: str):
        self.m_fundId = fundId

    def getFundId(self) -> str:
        return self.m_fundId

    def setAccountParameters(self, accountParameters: Dict):
        self.m_accountParameters = accountParameters

    def getAccountParameters(self) -> Dict:
        return self.m_accountParameters

    def addSubcribeContracts(self, contracts: set):
        self.m_subscribeContracts.update(contracts)

    def getSubcribeContracts(self) -> set:
        return self.m_subscribeContracts

    def start(self):
        self.m_thread = True
        if hasattr(self, 'onStart') and callable(self.onStart):
            self.onStart()

    def stop(self):
        if self.m_thread:
            self.m_thread = False
            if hasattr(self, 'onStop') and callable(self.onStop):
                self.onStop()

    # 模拟信号，使用回调函数
    def connect_signalMarketDataConnected(self, callback: Callable):
        self.signalMarketDataConnected_callback = callback

    def emit_signalMarketDataConnected(self):
        if hasattr(self, 'signalMarketDataConnected_callback') and callable(self.signalMarketDataConnected_callback):
            self.signalMarketDataConnected_callback()

    # 其他信号类似，这里省略部分代码以节省篇幅

    def onStart(self):
        pass

    def onStop(self):
        pass

    def onSubscribeMarketData(self, contracts: List[MMTContract]) -> int:
        return 0

    def onSendOrder(self, orderInfo: MMTOrderInfo) -> int:
        return 0

    def onCancelOrder(self, orderInfo: MMTOrderInfo) -> int:
        return 0

    def onSendOrders(self, orderInfos: List[MMTOrderInfo]):
        pass

    def onCancelOrders(self, orderInfos: List[MMTOrderInfo]):
        pass

    def onSendBulkOrders(self, orderInfos: List[MMTOrderInfo]) -> int:
        return 0

    def onCancelBulkOrders(self, orderInfos: List[MMTOrderInfo]) -> int:
        return 0

    def onQueryContracts(self) -> int:
        return 0

    def onQueryMarketDatus(self) -> int:
        return 0

    def onQueryLines(self, contract: str) -> int:
        return 0

    def onQueryPositions(self) -> int:
        return 0

    def onQueryOrders(self) -> int:
        return 0

    def onQueryOrder(self, systemId: str) -> int:
        return 0

    def onQueryOrder(self, contractId: str, systemId: str) -> int:
        return 0

    def onQueryTrades(self) -> int:
        return 0

    def onQueryCommissionRate(self, contract: str) -> int:
        return 0

    def onQueryAccount(self, currency: MMTCurrency) -> int:
        return 0