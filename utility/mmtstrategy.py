# mmtstrategy.py

from typing import List, Dict, Any
import threading
import datetime

from include.mmttickdata import MMTTickData
from include.mmtcontract import MMTContract
from include.mmtorderinfo import MMTOrderInfo
from include.mmtorder import MMTOrder
from include.mmttrade import MMTTrade
from include.mmtposition import MMTPosition
from include.mmtstrategyinterface import MMTStrategyInterface
from utility.mmtline import MMTLine
from utility.mmtutility import MMTUtility

# 模拟 Qt 的 QObject 类（简单实现）
class QObject:
    def __init__(self, parent=None):
        self.parent = parent

class MMTStrategy(QObject, MMTStrategyInterface):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_fundId = ""
        self.m_accounts = []
        self.m_accountId = ""
        self.m_tradeApiType = None
        self.m_strategyId = ""
        self.m_parameters = {}
        self.m_thread = threading.Thread(target=self._thread_run)
        self.m_currentLocalOrdeId = 0
        self.m_backtestStartDate = None

        # 模拟信号的回调函数列表
        self.signalSubscribeMarketData_callbacks = []
        self.signalSendOrders_callbacks = []
        self.signalCancelOrders_callbacks = []
        self.signalSendBulkOrders_callbacks = []
        self.signalCancelBulkOrders_callbacks = []

    def getObject(self):
        return self

    def setFund(self, fundId: str):
        self.m_fundId = fundId

    def getFundId(self) -> str:
        return self.m_fundId

    def setAccounts(self, accounts: List[Dict[str, Any]]):
        self.m_accounts = accounts
        if accounts:
            self.m_accountId = accounts[0].get("account_id", "")
            self.m_tradeApiType = MMTUtility.stringToTradeApiType(accounts[0].get("account_type", ""))

    def getAccounts(self) -> List[Dict[str, Any]]:
        return self.m_accounts

    def setStrategyId(self, strategyId: str):
        self.m_strategyId = strategyId

    def getStrategyId(self) -> str:
        return self.m_strategyId

    def setParameters(self, parameters: Dict[str, Any]):
        self.m_parameters = parameters
        self.m_parameters["strategy_id"] = self.m_strategyId
        self.onParameterChanged(self.m_parameters, True)

    def getParameters(self) -> Dict[str, Any]:
        return self.m_parameters

    def start(self):
        self.m_thread.start()

    def stop(self):
        if self.m_thread:
            self.m_thread.join()
            self.m_thread = None

    def reset(self):
        pass

    def setBacktestStartDate(self, date: datetime.date):
        self.m_backtestStartDate = date

    # 模拟信号发射
    def emit_signalSubscribeMarketData(self, contracts: List[MMTContract]):
        for callback in self.signalSubscribeMarketData_callbacks:
            callback(contracts)

    def emit_signalSendOrders(self, orderInfos: List[MMTOrderInfo]):
        for callback in self.signalSendOrders_callbacks:
            callback(orderInfos)

    def emit_signalCancelOrders(self, orderInfos: List[MMTOrderInfo]):
        for callback in self.signalCancelOrders_callbacks:
            callback(orderInfos)

    def emit_signalSendBulkOrders(self, orderInfos: List[MMTOrderInfo]):
        for callback in self.signalSendBulkOrders_callbacks:
            callback(orderInfos)

    def emit_signalCancelBulkOrders(self, orderInfos: List[MMTOrderInfo]):
        for callback in self.signalCancelBulkOrders_callbacks:
            callback(orderInfos)

    # 模拟槽函数
    def onStart(self):
        pass

    def onStop(self):
        pass

    def onMarketDataConnected(self):
        pass

    def onMarketDataDisconnected(self):
        pass

    def onTradeConnected(self):
        pass

    def onTradeDisconnected(self):
        pass

    def onError(self, code: int, msg: str):
        pass

    def onParameterChanged(self, parameters: Dict[str, Any], first: bool):
        pass

    def onTickData(self, tickData: MMTTickData):
        pass

    def onOrder(self, order: MMTOrder):
        pass

    def onTrade(self, trade: MMTTrade):
        pass

    def onPosition(self, position: MMTPosition):
        pass

    def onContracts(self, contracts: List[MMTContract]):
        pass

    def onMarketDatus(self, marketDatus: Dict[str, Dict[str, MMTTickData]]):
        pass

    def onLines(self, lines: List[MMTLine], num: int):
        pass

    def onBacktestLine(self, lines: List[MMTLine]):
        pass

    def onBacktestTickData(self, tickDatas: List[MMTTickData]):
        pass

    def closeAllPosition(self):
        pass

    def getLocalOrderId(self) -> int:
        self.m_currentLocalOrdeId += 1
        return self.m_currentLocalOrdeId

    def sendOrders(self, orderInfos: List[MMTOrderInfo]):
        for orderInfo in orderInfos:
            orderInfo.m_fundId = self.m_fundId
            orderInfo.m_accountId = self.m_accountId
            orderInfo.m_tradeApiType = self.m_tradeApiType
            orderInfo.m_strategyId = self.m_strategyId
        self.emit_signalSendOrders(orderInfos)

    def cancelOrders(self, orderInfos: List[MMTOrderInfo]):
        for orderInfo in orderInfos:
            orderInfo.m_fundId = self.m_fundId
            orderInfo.m_accountId = self.m_accountId
            orderInfo.m_tradeApiType = self.m_tradeApiType
            orderInfo.m_strategyId = self.m_strategyId
        self.emit_signalCancelOrders(orderInfos)

    def sendBulkOrders(self, orderInfos: List[MMTOrderInfo]):
        for orderInfo in orderInfos:
            orderInfo.m_fundId = self.m_fundId
            orderInfo.m_accountId = self.m_accountId
            orderInfo.m_tradeApiType = self.m_tradeApiType
            orderInfo.m_strategyId = self.m_strategyId
        self.emit_signalSendBulkOrders(orderInfos)

    def cancelBulkOrders(self, orderInfos: List[MMTOrderInfo]):
        for orderInfo in orderInfos:
            orderInfo.m_fundId = self.m_fundId
            orderInfo.m_accountId = self.m_accountId
            orderInfo.m_tradeApiType = self.m_tradeApiType
            orderInfo.m_strategyId = self.m_strategyId
        self.emit_signalCancelBulkOrders(orderInfos)

    def _thread_run(self):
        self.onStart()