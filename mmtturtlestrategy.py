import logging
import os
from typing import List

from include.mmtcontract import MMTContract
from include.mmtorder import MMTOrder
from include.mmttickdata import MMTTickData

from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType

class MMTTurtleStrategy:
    def __init__(self):
        # 初始化参数
        self.m_period = 900
        self.m_longPeriod = 3600
        self.m_positionControl = 1
        self.m_maxVolume = 0.03
        self.m_longLength = 56
        self.m_shortLength = 14
        self.m_atrCountOpen = 8
        self.m_atrCountClose = 6
        self.m_stopLossRate = 0.05
        self.m_maxSlippage = 10
        self.m_isRun = False
        self.m_maxATRShort = 0
        self.m_role = 0
        self.m_openPrice = 0
        self.m_atrTrade = 0
        self.m_isReduceLong = False
        self.m_isReduceShort = False
        self.m_position = 0
        self.m_positionLP = 0
        self.m_lineManager = None
        self.m_lineManagerLP = None
        self.m_isDoublePeriod = False
        self.m_isMarketDataConnected = False
        self.m_isTradeConnected = False
        self.m_isCurrentLineTrade = False
        self.m_isInit = False
        self.m_updateStatus = False
        self.m_currentPrice = 0
        self.m_currentTradeDirection = None  # 假设 MMT_TD_NULL 在 Python 中为 None
        self.m_currentSendingVolume = 0

        # 指标
        self.m_atrList = []
        # 假设 MMTIndicatorHighest、MMTIndicatorLowest 等类已经在 Python 中定义
        self.m_highest = None
        self.m_lowest = None
        self.m_atrShort = None
        self.m_atrLong = None
        self.m_macd = None
        self.m_highestLP = None
        self.m_lowestLP = None
        self.m_atrShortLP = None
        self.m_atrLongLP = None
        self.m_macdLP = None

        # 存储变量
        self.m_signalContractName = ""
        self.m_tradeContractName = ""
        self.m_signalContract = None
        self.m_tradeContract = None
        self.m_orderInfos = {}
        self.m_unfilledVolume = {}

        self.m_signalTickData = MMTTickData()

    def onContracts(self, contracts: List[MMTContract]):
        for contract in contracts:
            if self.m_tradeApiType == contract.m_tradeApiType and contract.m_id == self.m_signalContractName:
                self.m_signalContract = contract
                logging.info(f"signal contract. contract id: {contract.m_id}"
                             f". exchange: {contract.m_exchange}"
                             f". type: {contract.m_type}"
                             f". delivery type: {contract.m_deliveryType}"
                             f". min volume: {contract.m_minVolume}"
                             f". volume multiple: {contract.m_volumeMultiple}"
                             f". price tick: {contract.m_priceTick}")
            if self.m_tradeApiType == contract.m_tradeApiType and contract.m_id == self.m_tradeContractName:
                self.m_tradeContract = contract
                logging.info(f"trade contract. contract id: {contract.m_id}"
                             f". exchange: {contract.m_exchange}"
                             f". type: {contract.m_type}"
                             f". delivery type: {contract.m_deliveryType}"
                             f". min volume: {contract.m_minVolume}"
                             f". volume multiple: {contract.m_volumeMultiple}"
                             f". price tick: {contract.m_priceTick}")

    def update(self):
        if not self.m_isInit:
            return False

        if self.m_signalTickData.m_latestPrice <= 0.0:
            return False

        self.m_currentPrice = self.m_signalTickData.m_latestPrice

        # 更新 K 线
        old_time = self.m_lineManager.getLine(0).m_startTime
        self.m_lineManager.onTick(self.m_signalTickData)
        new_time = self.m_lineManager.getLine(0).m_startTime
        if self.m_isDoublePeriod:
            self.m_lineManagerLP.onTick(self.m_signalTickData)

        if old_time != new_time:
            # 输出 K 线
            line1 = self.m_lineManager.getLine(1)
            if line1:
                logging.info(f"{line1.m_startTime.strftime('%Y-%m-%d %H:%M:%S')}, "
                             f"{line1.m_open}, {line1.m_high}, {line1.m_low}, {line1.m_close}")
            if self.m_isDoublePeriod:
                line1LP = self.m_lineManagerLP.getLine(1)
                if line1LP:
                    logging.info(f"{line1LP.m_startTime.strftime('%Y-%m-%d %H:%M:%S')}, "
                                 f"{line1LP.m_open}, {line1LP.m_high}, {line1LP.m_low}, {line1LP.m_close}")

            # 新的 K 线可以开启交易
            self.m_isCurrentLineTrade = False

            line2 = self.m_lineManager.getLine(2)
            if line1 and line2 and line1.m_startTime.date() != line2.m_startTime.date():
                self.m_isReduceLong = self.m_isReduceShort = False
                self.writeParameters()

            if not self.updateIndicators():
                return False

            if len(self.m_lineManager) <= self.m_longLength * 2 + 2 or \
                    (self.m_isDoublePeriod and len(self.m_lineManagerLP) <= self.m_longLength * 2 + 2):
                return False

            if len(self.m_atrList) < self.m_longLength:
                return False

            logging.info(f"atrShort: {self.m_atrShort.m_value}"
                         f". atrLong: {self.m_atrLong.m_value}"
                         f". macddiff: {self.m_macd.m_diff}"
                         f". macddea: {self.m_macd.m_value}"
                         f". highest: {self.m_highest.m_value}"
                         f". lowest: {self.m_lowest.m_value}"
                         f". maxAtrShort: {self.m_maxATRShort}")
            if self.m_isDoublePeriod:
                logging.info(f"atrShortLP: {self.m_atrShortLP.m_value}"
                             f". atrLongLP: {self.m_atrLongLP.m_value}"
                             f". macddiffLP: {self.m_macdLP.m_diff}"
                             f". macddeaLP: {self.m_macdLP.m_value}"
                             f". highestLP: {self.m_highestLP.m_value}"
                             f". lowestLP: {self.m_lowestLP.m_value}")

        return True

    def onOrder(self, order: MMTOrder):
        if order.m_strategyId.lower() != self.m_strategyId.lower():
            return

        logging.info(f"on order. contract id: {order.m_contractId}"
                     f". local order id: {order.m_localOrderId}"
                     f". order ref: {order.m_orderRef}"
                     f". system id: {order.m_systemId}"
                     f". order price: {order.m_orderPrice}"
                     f". order volume: {order.m_orderVolume}"
                     f". filled price: {order.m_filledPrice}"
                     f". filled volume: {order.m_filledVolume}"
                     f". unfilled volume: {order.m_unfilledVolume}"
                     f". cancelled volume: {order.m_cancelledVolume}"
                     f". rejected volume: {order.m_rejectedVolume}"
                     f". order status: {order.m_orderStatus}")

        if order.m_localOrderId in self.m_unfilledVolume:
            filled_volume = self.m_unfilledVolume[order.m_localOrderId] - order.m_unfilledVolume
            if filled_volume > 0.0:
                if self.isBuy(order.m_direction):  # 假设 isBuy 方法已经实现
                    self.m_position += filled_volume
                    self.writeParameters()
                else:
                    self.m_position -= filled_volume
                    self.writeParameters()
                self.m_currentSendingVolume -= filled_volume
                if self.m_currentSendingVolume <= 0.0:
                    self.m_currentTradeDirection = None
                self.writeParameters()
                self.m_unfilledVolume[order.m_localOrderId] = order.m_unfilledVolume

        if order.m_localOrderId in self.m_orderInfos:
            if order.m_orderStatus in [MMTOrderStatus.MMT_OS_FILLED, MMTOrderStatus.MMT_OS_CANCELLED, MMTOrderStatus.MMT_OS_REJECTED]:  # 假设这些常量已经定义
                del self.m_orderInfos[order.m_localOrderId]
                del self.m_unfilledVolume[order.m_localOrderId]

    def sellCondition(self):
        if self.m_currentTradeDirection is not None:
            return False

        if self.m_role <= 0:
            return False

        # 止损
        stop_loss_price = max(self.calculateStopLossPrice(self.m_openPrice, self.m_stopLossRate, True),
                              self.m_openPrice - self.m_atrCountClose * self.m_atrLong.m_value * 2.0)
        stop_loss_price = self.m_tradeContract.floorToPriceTick(stop_loss_price)
        if self.m_currentPrice < stop_loss_price:
            self.m_currentSendingVolume = abs(self.m_position)
            self.m_role = 0
            self.m_isCurrentLineTrade = True
            self.writeParameters()
            return True

        if self.m_isCurrentLineTrade:
            return False

        return False

    def writeTradeItem(self, trade):
        fund_dir = os.path.join("funds", self.m_fundId, "items")
        os.makedirs(fund_dir, exist_ok=True)
        file_path = os.path.join(fund_dir, f"MMTradeTurtleStrategy_{self.m_strategyId}_{self.m_accountId}_items.txt")
        try:
            with open(file_path, "a") as file:
                file.write(f"{trade.m_contractId}, "
                           f"{trade.m_time.timestamp() * 1000}, "
                           f"{trade.m_direction}, "
                           f"{trade.m_price}, "
                           f"{trade.m_volume}\n")
        except Exception as e:
            logging.info(f"can't open parameters file. Error: {str(e)}")

