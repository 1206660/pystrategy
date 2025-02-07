# mmtutility.py
import datetime

# 假设这些枚举值在 mmtdatatype.py 中定义
from include.mmtdatatype import MMTExchange, MMTContractType, MMTDeliveryType, MMTTradeDirection, MMTOrderType, \
    MMTOrderOpenCloseType, MMTOrderStatus, MMTTradeApiType, MMTCommissionRateType, MMTCurrency, MMTPrictType
from include.mmtcontract import MMTContract
from datetime import datetime, timedelta

PRECISION = 1e-6  # 假设的精度值

class MMTUtility:
    @staticmethod
    def toNaturalTime(time: datetime, exchange):
        if MMTUtility.isChinaCFExchange(exchange):
            hour = time.hour
            weekend = time.weekday() + 1  # Python 中 weekday() 返回 0-6，这里调整为 1-7
            if hour > 18:
                if weekend > 1:
                    return time - timedelta(days=1)
                else:
                    return time - timedelta(days=3)
            elif hour < 8 and weekend == 1:
                return time - timedelta(days=2)
        return time

    @staticmethod
    def isEarlierByNatural(left: datetime, right: datetime, exchange):
        return MMTUtility.toNaturalTime(left, exchange) < MMTUtility.toNaturalTime(right, exchange)

    @staticmethod
    def isChinaCFExchange(exchange):
        return exchange in [MMTExchange.MMT_EX_SHFE, MMTExchange.MMT_EX_CZCE, MMTExchange.MMT_EX_DCE, MMTExchange.MMT_EX_INE]

    @staticmethod
    def isChinaSIFExchange(exchange):
        return exchange == MMTExchange.MMT_EX_CFFEX

    @staticmethod
    def isChinaFuturesExchange(exchange):
        return MMTUtility.isChinaCFExchange(exchange) or MMTUtility.isChinaSIFExchange(exchange)

    @staticmethod
    def isChinaStockExchange(exchange):
        return exchange in [MMTExchange.MMT_EX_SSE, MMTExchange.MMT_EX_SZSE]

    @staticmethod
    def isChinaExchange(exchange):
        return MMTUtility.isChinaStockExchange(exchange) or MMTUtility.isChinaFuturesExchange(exchange)

    @staticmethod
    def isChinaNight(time: datetime):
        hour = time.hour
        return hour > 18 or hour < 8

    @staticmethod
    def isChinarMornig(time: datetime):
        hour = time.hour
        return hour > 8 and hour < 12

    @staticmethod
    def isChinaAfternoon(time: datetime):
        hour = time.hour
        return hour > 12 and hour < 18

    @staticmethod
    def stringToTradeApiType(exchange: str):
        if exchange.lower() == "ctp":
            return MMTTradeApiType.MMT_TAT_CTP
        elif exchange.lower() == "deribit":
            return MMTTradeApiType.MMT_TAT_DERIBIT
        elif exchange.lower() == "okex":
            return MMTTradeApiType.MMT_TAT_OKEX
        elif exchange.lower() == "ht":
            return MMTTradeApiType.MMT_TAT_HT
        return MMTTradeApiType.MMT_TAT_NULL

    @staticmethod
    def tradeApiTypeToString(tradeApiType):
        if tradeApiType == MMTTradeApiType.MMT_TAT_CTP:
            return "CTP"
        elif tradeApiType == MMTTradeApiType.MMT_TAT_DERIBIT:
            return "DERIBIT"
        elif tradeApiType == MMTTradeApiType.MMT_TAT_OKEX:
            return "OKEX"
        elif tradeApiType == MMTTradeApiType.MMT_TAT_HT:
            return "HT"
        elif tradeApiType == MMTTradeApiType.MMT_TAT_NULL:
            return ""
        return ""

    @staticmethod
    def isBuy(direction):
        return direction in [MMTTradeDirection.MMT_TD_BUY, MMTTradeDirection.MMT_TD_BUYTOCOVER]

    @staticmethod
    def isOpen(direction):
        return direction in [MMTTradeDirection.MMT_TD_BUY, MMTTradeDirection.MMT_TD_SELLSHORT]

    @staticmethod
    def getCounterPartyDirection(direction):
        if direction == MMTTradeDirection.MMT_TD_BUY:
            return MMTTradeDirection.MMT_TD_SELL
        elif direction == MMTTradeDirection.MMT_TD_SELL:
            return MMTTradeDirection.MMT_TD_BUY
        elif direction == MMTTradeDirection.MMT_TD_SELLSHORT:
            return MMTTradeDirection.MMT_TD_BUYTOCOVER
        elif direction == MMTTradeDirection.MMT_TD_BUYTOCOVER:
            return MMTTradeDirection.MMT_TD_SELLSHORT
        elif direction == MMTTradeDirection.MMT_TD_NULL:
            return MMTTradeDirection.MMT_TD_NULL
        return None

    @staticmethod
    def getOppositeDirection(direction):
        if direction == MMTTradeDirection.MMT_TD_BUY:
            return MMTTradeDirection.MMT_TD_SELLSHORT
        elif direction == MMTTradeDirection.MMT_TD_SELL:
            return MMTTradeDirection.MMT_TD_BUYTOCOVER
        elif direction == MMTTradeDirection.MMT_TD_SELLSHORT:
            return MMTTradeDirection.MMT_TD_BUY
        elif direction == MMTTradeDirection.MMT_TD_BUYTOCOVER:
            return MMTTradeDirection.MMT_TD_SELL
        elif direction == MMTTradeDirection.MMT_TD_NULL:
            return MMTTradeDirection.MMT_TD_NULL
        return None

    @staticmethod
    def stringToCurrency(currency: str):
        currency = currency.upper()
        if currency == "CNY":
            return MMTCurrency.MMT_CUR_CNY
        elif currency == "USD":
            return MMTCurrency.MMT_CUR_USD
        elif currency == "HKD":
            return MMTCurrency.MMT_CUR_HKD
        elif currency == "BTC":
            return MMTCurrency.MMT_CUR_BTC
        elif currency == "ETH":
            return MMTCurrency.MMT_CUR_ETH
        elif currency == "USDT":
            return MMTCurrency.MMT_CUR_USDT
        return MMTCurrency.MMT_CUR_NULL

    @staticmethod
    def currencyToString(currency):
        if currency == MMTCurrency.MMT_CUR_CNY:
            return "CNY"
        elif currency == MMTCurrency.MMT_CUR_USD:
            return "USD"
        elif currency == MMTCurrency.MMT_CUR_HKD:
            return "HKD"
        elif currency == MMTCurrency.MMT_CUR_BTC:
            return "BTC"
        elif currency == MMTCurrency.MMT_CUR_ETH:
            return "ETH"
        elif currency == MMTCurrency.MMT_CUR_USDT:
            return "USDT"
        return ""

    @staticmethod
    def orderTypeToString(orderType):
        if orderType == MMTOrderType.MMT_OT_LIMIT:
            return "LIMIT"
        elif orderType == MMTOrderType.MMT_OT_MARKET:
            return "MARKET"
        elif orderType == MMTOrderType.MMT_OT_STOP_LIMIT:
            return "STOP_LIMIT"
        elif orderType == MMTOrderType.MMT_OT_STOP_MARKET:
            return "STOP_MARKET"
        return ""

    @staticmethod
    def exchangeToString(exchange):
        if exchange == MMTExchange.MMT_EX_DCE:
            return "DCE"
        elif exchange == MMTExchange.MMT_EX_INE:
            return "INE"
        elif exchange == MMTExchange.MMT_EX_SSE:
            return "SSE"
        elif exchange == MMTExchange.MMT_EX_CZCE:
            return "CZCE"
        elif exchange == MMTExchange.MMT_EX_SHFE:
            return "SHFE"
        elif exchange == MMTExchange.MMT_EX_SZSE:
            return "SZSE"
        elif exchange == MMTExchange.MMT_EX_CFFEX:
            return "CFFEX"
        elif exchange == MMTExchange.MMT_EX_DERIBIT:
            return "DERIBIT"
        elif exchange == MMTExchange.MMT_EX_OKEX:
            return "OKEX"
        return ""

    @staticmethod
    def calculateProfit(contract, openPrice: float, closePrice: float, volume: float, direction, isCoin: bool, coinPrice: float):
        value = 0
        if not MMTUtility.isBuy(direction):
            volume = -volume
        if contract.m_deliveryType == MMTDeliveryType.MMT_DT_NORMAL:
            value = volume * contract.m_volumeMultiple * (closePrice - openPrice)
            if isCoin:
                if abs(coinPrice) < PRECISION:
                    value = 0
                else:
                    value /= coinPrice
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_INVERSE:
            if abs(openPrice) > PRECISION:
                value = volume * contract.m_volumeMultiple * (closePrice - openPrice) / openPrice
            if isCoin:
                if abs(coinPrice) < PRECISION:
                    value = 0
                else:
                    value /= coinPrice
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_QUANTO:
            value = volume * contract.m_volumeMultiple * (closePrice - openPrice)
            if not isCoin:
                value *= coinPrice
        return value

    @staticmethod
    def calculateCommission(contract, price: float, volume: float, commissionRate: float, isCoin: bool, coinPrice: float):
        value = 0
        if contract.m_deliveryType == MMTDeliveryType.MMT_DT_NORMAL:
            value = volume * contract.m_volumeMultiple * price * commissionRate
            if isCoin:
                if abs(coinPrice) < PRECISION:
                    value = 0
                else:
                    value /= coinPrice
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_INVERSE:
            value = volume * contract.m_volumeMultiple * commissionRate
            if isCoin:
                if abs(coinPrice) < PRECISION:
                    value = 0
                else:
                    value /= coinPrice
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_QUANTO:
            value = volume * contract.m_volumeMultiple * price * commissionRate
            if not isCoin:
                value *= coinPrice
        return value

    @staticmethod
    def calculateSlippage(contract, price: float, volume: float, slippageRate: float, isCoin: bool, coinPrice: float):
        value = 0
        if contract.m_deliveryType == MMTDeliveryType.MMT_DT_NORMAL:
            value = volume * contract.m_volumeMultiple * slippageRate * contract.m_priceTick
            if isCoin:
                if abs(coinPrice) < PRECISION:
                    value = 0
                else:
                    value /= coinPrice
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_INVERSE:
            if abs(price) > PRECISION:
                value = volume * contract.m_volumeMultiple / price * slippageRate * contract.m_priceTick
            if isCoin:
                if abs(coinPrice) < PRECISION:
                    value = 0
                else:
                    value /= coinPrice
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_QUANTO:
            value = volume * contract.m_volumeMultiple * slippageRate * contract.m_priceTick
            if not isCoin:
                value *= coinPrice
        return value

    @staticmethod
    def calculateMargin(contract, price: float, volume: float):
        value = 0
        if contract.m_deliveryType == MMTDeliveryType.MMT_DT_NORMAL:
            value = volume * contract.m_volumeMultiple * price * contract.m_leverageRatio
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_INVERSE:
            if abs(price) > PRECISION:
                value = volume * contract.m_volumeMultiple / price * contract.m_leverageRatio
        elif contract.m_deliveryType == MMTDeliveryType.MMT_DT_QUANTO:
            value = volume * contract.m_volumeMultiple * price * contract.m_leverageRatio
        return value


# 模板函数转换为普通函数
def isGreater(left, right):
    return left > right + PRECISION


def isLess(left, right):
    return left < right - PRECISION


def isEqual(left, right):
    return abs(left - right) <= PRECISION


def isGreaterEqual(left, right):
    return left >= right - PRECISION


def isLessEqual(left, right):
    return left <= right + PRECISION


def isNotEqual(left, right):
    return abs(left - right) > PRECISION


# 以下是简单的使用示例
if __name__ == "__main__":
    # 假设创建一个简单的 contract 对象
    class MMTContract:
        def __init__(self):
            self.m_deliveryType = MMTDeliveryType.MMT_DT_NORMAL
            self.m_volumeMultiple = 10
            self.m_leverageRatio = 0.1
            self.m_priceTick = 0.01

    contract = MMTContract()
    open_price = 100.0
    close_price = 110.0
    volume = 10
    direction = MMTTradeDirection.MMT_TD_BUY
    is_coin = False
    coin_price = 1.0

    profit = MMTUtility.calculateProfit(contract, open_price, close_price, volume, direction, is_coin, coin_price)
    print(f"Profit: {profit}")