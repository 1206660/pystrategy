# 导入必要的库
from PyQt5.QtCore import QDateTime, QTime, QDate
import math

from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType
from include.mmtcontract import MMTContract
from include.mmttickdata import MMTTickData
from mmtutility import MMTUtility


class MMTLine:
    def __init__(self):
        self.m_contractId = ""
        self.m_exchange = None
        self.m_startTime = QDateTime()
        self.m_endTime = QDateTime()
        self.m_open = 0.0
        self.m_high = 0.0
        self.m_low = 0.0
        self.m_close = 0.0
        self.m_volume = 0.0
        self.m_turnover = 0.0
        self.m_openInterest = 0.0
        self.m_factor = 1.0
        self.m_tradeDate = QDate()
        self.m_contractCode = ""

    def update(self, line, scale, contract):
        if not line.m_startTime.isValid():
            return

        if self.m_startTime.isValid() and MMTUtility.isEarlierByNatural(line.m_startTime, self.m_startTime, contract.m_exchange):
            return

        if not self.m_startTime.isValid():
            self.m_startTime = self.getStartTime(line.m_startTime, scale, contract)
            self.m_open = line.m_open
            self.m_high = line.m_high
            self.m_low = line.m_low
        else:
            if self.m_high < line.m_high:
                self.m_high = line.m_high
            if self.m_low > line.m_low:
                self.m_low = line.m_low

        if MMTUtility.isEarlierByNatural(self.m_endTime, line.m_endTime, contract.m_exchange):
            self.m_endTime = line.m_endTime

        self.m_close = line.m_close
        self.m_volume = line.m_volume
        self.m_turnover = line.m_turnover
        self.m_openInterest = line.m_openInterest

    def update(self, tick, scale, contract):
        if not tick.m_time.isValid():
            return

        if MMTUtility.isEarlierByNatural(tick.m_time, self.m_startTime, contract.m_exchange):
            return

        if not self.m_startTime.isValid():
            self.m_startTime = self.getStartTime(tick.m_time, scale, contract)
            self.m_open = self.m_high = self.m_low = tick.m_latestPrice
        else:
            if self.m_high < tick.m_latestPrice:
                self.m_high = tick.m_latestPrice
            if self.m_low > tick.m_latestPrice:
                self.m_low = tick.m_latestPrice

        if MMTUtility.isEarlierByNatural(self.m_endTime, tick.m_time, contract.m_exchange):
            self.m_endTime = tick.m_time

        self.m_close = tick.m_latestPrice
        self.m_volume = tick.m_volume
        self.m_turnover = tick.m_turnover
        self.m_openInterest = tick.m_openInterest

    def newLine(self, tick, scale, contract):
        return []

    def newLine(self, line, scale, contract):
        return []

    def getStartTime(self, time, scale, contract):
        return QDateTime()

    def createLine(self):
        return MMTLine()

    def getPrice(self, priceType):
        if priceType == MMTPrictType.MMT_PT_OPEN:
            return self.m_open
        elif priceType == MMTPrictType.MMT_PT_HIGH:
            return self.m_high
        elif priceType == MMTPrictType.MMT_PT_LOW:
            return self.m_low
        elif priceType == MMTPrictType.MMT_PT_CLOSE:
            return self.m_close
        return 0.0

    def isCloseTime(self, time, exchange, scale):
        if MMTUtility.isChinaExchange(exchange):
            hour = time.time().hour()
            minute = time.time().minute()

            # 11:30和15：00
            if (hour == 11 and minute == 30) or (hour == 15 and minute == 0):
                return True
            # 期货交易所10：15
            elif scale <= 15.0 and hour == 10 and minute == 15 and MMTUtility.isChinaCFExchange(exchange):
                return True
            # 夜盘
            # TODO
        return False

class MMTKLine(MMTLine):
    def __init__(self):
        super().__init__()

    def newLine(self, line, scale, contract):
        lines = []

        if not self.m_startTime.isValid():
            return lines

        if 86400 == int(scale) and self.m_startTime.date() == line.m_startTime.date():
            return lines

        if self.isCloseTime(line.m_startTime, contract.m_exchange, scale):
            return lines

        if MMTUtility.toNaturalTime(self.m_startTime, contract.m_exchange).secsTo(MMTUtility.toNaturalTime(line.m_startTime, contract.m_exchange)) < scale:
            return lines

        newLine = self.createLine()
        newLine.m_startTime = self.getStartTime(line.m_startTime, scale, contract)
        newLine.m_endTime = line.m_endTime
        newLine.m_open = line.m_open
        newLine.m_high = line.m_high
        newLine.m_low = line.m_low
        newLine.m_close = line.m_close
        newLine.m_volume = line.m_volume
        newLine.m_turnover = line.m_turnover
        newLine.m_openInterest = line.m_openInterest

        lines.append(newLine)

        return lines

    def newLine(self, tick, scale, contract):
        lines = []

        if not self.m_startTime.isValid():
            return lines

        if 86400 == int(scale) and self.m_startTime.date() == tick.m_time.date():
            return lines

        if self.isCloseTime(tick.m_time, contract.m_exchange, scale):
            return lines

        if MMTUtility.toNaturalTime(self.m_startTime, contract.m_exchange).secsTo(MMTUtility.toNaturalTime(tick.m_time, contract.m_exchange)) < scale:
            return lines

        newLine = self.createLine()
        newLine.m_startTime = self.getStartTime(tick.m_time, scale, contract)
        newLine.m_endTime = tick.m_time
        newLine.m_open = newLine.m_high = newLine.m_low = newLine.m_close = tick.m_latestPrice
        newLine.m_volume = tick.m_volume
        newLine.m_turnover = tick.m_turnover
        newLine.m_openInterest = tick.m_openInterest

        lines.append(newLine)

        return lines

    def getStartTime(self, time, scale, contract):
        if 86400 == int(scale):
            return QDateTime(time.date())

        openTime = time
        if MMTUtility.isChinaExchange(contract.m_exchange):
            hour = time.time().hour()
            # 夜盘21：00之后
            if hour > 18:
                openTime.setTime(QTime(21, 0, 0))
            # 下午
            elif hour > 12:
                if MMTUtility.isChinaCFExchange(contract.m_exchange):
                    openTime.setTime(QTime(13, 30, 0))
                else:
                    openTime.setTime(QTime(13, 00, 0))
            # 上午
            elif hour > 8:
                if MMTUtility.isChinaCFExchange(contract.m_exchange):
                    openTime.setTime(QTime(9, 0, 0))
                else:
                    openTime.setTime(QTime(9, 30, 0))
            # 上海期货交易所夜盘00:00-02:30
            else:
                openTime.setTime(QTime(21, 0, 0))
                openTime = openTime.addDays(-1)

            # 集合竞价时间调整
            if time < openTime:
                time = openTime

            return openTime.addSecs(math.floor(openTime.secsTo(time) / scale) * scale)

        openTime.setTime(QTime(0, 0, 0))
        return openTime.addSecs(math.floor(openTime.secsTo(time) / scale) * scale)

    def createLine(self):
        return MMTKLine()