# mmtutility.py
import datetime

# 假设这些枚举值在 mmtdatatype.py 中定义
from include.mmtdatatype import MMTExchange, MMTTradeApiType, MMTCurrency, MMTOrderType, MMTTradeDirection
from include.mmtcontract import MMTContract

# 常量 PRECISION 需根据实际情况定义
PRECISION = 1e-6

def toNaturalTime(time: datetime.datetime, exchange: MMTExchange):
    """
    将时间转换为自然时间
    :param time: 输入的时间
    :param exchange: 交易所类型
    :return: 转换后的时间
    """
    if isChinaCFExchange(exchange):
        hour = time.hour
        weekend = time.weekday()
        if hour > 18:
            if weekend > 0:
                return time - datetime.timedelta(days=1)
            else:
                return time - datetime.timedelta(days=3)
        elif hour < 8 and weekend == 0:
            return time - datetime.timedelta(days=2)
    return time

def isEarlierByNatural(left: datetime.datetime, right: datetime.datetime, exchange: MMTExchange):
    """
    判断左时间是否早于右时间（按自然时间）
    :param left: 左时间
    :param right: 右时间
    :param exchange: 交易所类型
    :return: 左时间是否早于右时间
    """
    return toNaturalTime(left, exchange) < toNaturalTime(right, exchange)

def isChinaCFExchange(exchange: MMTExchange):
    """
    判断是否为中国商品期货交易所
    :param exchange: 交易所类型
    :return: 是否为中国商品期货交易所
    """
    return exchange in [MMTExchange.MMT_EX_SHFE, MMTExchange.MMT_EX_CZCE, MMTExchange.MMT_EX_DCE, MMTExchange.MMT_EX_INE]

def isChinaSIFExchange(exchange: MMTExchange):
    """
    判断是否为中国金融期货交易所
    :param exchange: 交易所类型
    :return: 是否为中国金融期货交易所
    """
    return exchange == MMTExchange.MMT_EX_CFFEX

def isChinaFuturesExchange(exchange: MMTExchange):
    """
    判断是否为中国期货交易所
    :param exchange: 交易所类型
    :return: 是否为中国期货交易所
    """
    return isChinaCFExchange(exchange) or isChinaSIFExchange(exchange)

def isChinaStockExchange(exchange: MMTExchange):
    """
    判断是否为中国股票交易所
    :param exchange: 交易所类型
    :return: 是否为中国股票交易所
    """
    return exchange in [MMTExchange.MMT_EX_SSE, MMTExchange.MMT_EX_SZSE]

def isChinaExchange(exchange: MMTExchange):
    """
    判断是否为中国交易所
    :param exchange: 交易所类型
    :return: 是否为中国交易所
    """
    return isChinaStockExchange(exchange) or isChinaFuturesExchange(exchange)

def isChinaNight(time: datetime.datetime):
    """
    判断是否为中国夜间时间
    :param time: 输入的时间
    :return: 是否为中国夜间时间
    """
    hour = time.hour
    return hour > 18 or hour < 8

def isChinarMornig(time: datetime.datetime):
    """
    判断是否为中国上午时间
    :param time: 输入的时间
    :return: 是否为中国上午时间
    """
    hour = time.hour
    return 8 < hour < 12

def isChinaAfternoon(time: datetime.datetime):
    """
    判断是否为中国下午时间
    :param time: 输入的时间
    :return: 是否为中国下午时间
    """
    hour = time.hour
    return 12 < hour < 18

def stringToTradeApiType(exchange: str):
    """
    将交易所名称字符串转换为交易 API 类型
    :param exchange: 交易所名称字符串
    :return: 交易 API 类型
    """
    if exchange.lower() == "ctp":
        return MMTTradeApiType.MMT_TAT_CTP
    elif exchange.lower() == "deribit":
        return MMTTradeApiType.MMT_TAT_DERIBIT
    elif exchange.lower() == "okex":
        return MMTTradeApiType.MMT_TAT_OKEX
    elif exchange.lower() == "ht":
        return MMTTradeApiType.MMT_TAT_HT
    return MMTTradeApiType.MMT_TAT_NULL

def tradeApiTypeToString(tradeApiType: MMTTradeApiType):
    """
    将交易 API 类型转换为字符串
    :param tradeApiType: 交易 API 类型
    :return: 交易 API 类型对应的字符串
    """
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

def isBuy(direction: MMTTradeDirection):
    """
    判断交易方向是否为买入
    :param direction: 交易方向
    :return: 是否为买入
    """
    return direction in [MMTTradeDirection.MMT_TD_BUY, MMTTradeDirection.MMT_TD_BUYTOCOVER]

def isOpen(direction: MMTTradeDirection):
    """
    判断交易方向是否为开仓
    :param direction: 交易方向
    :return: 是否为开仓
    """
    return direction in [MMTTradeDirection.MMT_TD_BUY, MMTTradeDirection.MMT_TD_SELLSHORT]

def getCounterPartyDirection(direction: MMTTradeDirection):
    """
    获取交易方向的对手方方向
    :param direction: 交易方向
    :return: 对手方方向
    """
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

def getOppositeDirection(direction: MMTTradeDirection):
    """
    获取交易方向的相反方向
    :param direction: 交易方向
    :return: 相反方向
    """
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

def stringToCurrency(currency: str):
    """
    将货币名称字符串转换为货币类型
    :param currency: 货币名称字符串
    :return: 货币类型
    """
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

def currencyToString(currency: MMTCurrency):
    """
    将货币类型转换为字符串
    :param currency: 货币类型
    :return: 货币类型对应的字符串
    """
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

def orderTypeToString(orderType: MMTOrderType):
    """
    将订单类型转换为字符串
    :param orderType: 订单类型
    :return: 订单类型对应的字符串
    """
    if orderType == MMTOrderType.MMT_OT_LIMIT:
        return "LIMIT"
    elif orderType == MMTOrderType.MMT_OT_MARKET:
        return "MARKET"
    elif orderType == MMTOrderType.MMT_OT_STOP_LIMIT:
        return "STOP_LIMIT"
    elif orderType == MMTOrderType.MMT_OT_STOP_MARKET:
        return "STOP_MARKET"
    return ""

def exchangeToString(exchange: MMTExchange):
    """
    将交易所类型转换为字符串
    :param exchange: 交易所类型
    :return: 交易所类型对应的字符串
    """
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

def calculateProfit(contract: MMTContract, openPrice: float, closePrice: float, volume: float,
                    direction: MMTTradeDirection, isCoin: bool, coinPrice: float):
    """
    计算利润
    :param contract: 合约信息
    :param openPrice: 开仓价格
    :param closePrice: 平仓价格
    :param volume: 交易量
    :param direction: 交易方向
    :param isCoin: 是否为加密货币
    :param coinPrice: 加密货币价格
    :return: 利润
    """
    value = 0
    if not isBuy(direction):
        volume = -volume
    if contract.m_deliveryType == 0:  # 假设 MMT_DT_NORMAL 为 0
        value = volume * contract.m_volumeMultiple * (closePrice - openPrice)
        if isCoin:
            if abs(coinPrice) < PRECISION:
                value = 0
            else:
                value /= coinPrice
    elif contract.m_deliveryType == 1:  # 假设 MMT_DT_INVERSE 为 1
        if abs(openPrice) > PRECISION:
            value = volume * contract.m_volumeMultiple * (closePrice - openPrice) / openPrice
        if isCoin:
            if abs(coinPrice) < PRECISION:
                value = 0
            else:
                value /= coinPrice
    elif contract.m_deliveryType == 2:  # 假设 MMT_DT_QUANTO 为 2
        value = volume * contract.m_volumeMultiple * (closePrice - openPrice)
        if not isCoin:
            value *= coinPrice
    return value

def calculateCommission(contract: MMTContract, price: float, volume: float, commissionRate: float, isCoin: bool, coinPrice: float):
    """
    计算佣金
    :param contract: 合约信息
    :param price: 价格
    :param volume: 交易量
    :param commissionRate: 佣金率
    :param isCoin: 是否为加密货币
    :param coinPrice: 加密货币价格
    :return: 佣金
    """
    value = 0
    if contract.m_deliveryType == 0:  # 假设 MMT_DT_NORMAL 为 0
        value = volume * contract.m_volumeMultiple * price * commissionRate
        if isCoin:
            if abs(coinPrice) < PRECISION:
                value = 0
            else:
                value /= coinPrice
    elif contract.m_deliveryType == 1:  # 假设 MMT_DT_INVERSE 为 1
        value = volume * contract.m_volumeMultiple * commissionRate
        if isCoin:
            if abs(coinPrice) < PRECISION:
                value = 0
            else:
                value /= coinPrice
    elif contract.m_deliveryType == 2:  # 假设 MMT_DT_QUANTO 为 2
        value = volume * contract.m_volumeMultiple * price * commissionRate
        if not isCoin:
            value *= coinPrice
    return value

def calculateSlippage(contract: MMTContract, price: float, volume: float, slippageRate: float, isCoin: bool, coinPrice: float):
    """
    计算滑点
    :param contract: 合约信息
    :param price: 价格
    :param volume: 交易量
    :param slippageRate: 滑点率
    :param isCoin: 是否为加密货币
    :param coinPrice: 加密货币价格
    :return: 滑点
    """
    value = 0
    if contract.m_deliveryType == 0:  # 假设 MMT_DT_NORMAL 为 0
        value = volume * contract.m_volumeMultiple * slippageRate * contract.m_priceTick
        if isCoin:
            if abs(coinPrice) < PRECISION:
                value = 0
            else:
                value /= coinPrice
    elif contract.m_deliveryType == 1:  # 假设 MMT_DT_INVERSE 为 1
        if abs(price) > PRECISION:
            value = volume * contract.m_volumeMultiple / price * slippageRate * contract.m_priceTick
        if isCoin:
            if abs(coinPrice) < PRECISION:
                value = 0
            else:
                value /= coinPrice
    elif contract.m_deliveryType == 2:  # 假设 MMT_DT_QUANTO 为 2
        value = volume * contract.m_volumeMultiple * slippageRate * contract.m_priceTick
        if not isCoin:
            value *= coinPrice
    return value

def calculateMargin(contract: MMTContract, price: float, volume: float):
    """
    计算保证金
    :param contract: 合约信息
    :param price: 价格
    :param volume: 交易量
    :return: 保证金
    """
    value = 0
    if contract.m_deliveryType == 0:  # 假设 MMT_DT_NORMAL 为 0
        value = volume * contract.m_volumeMultiple * price * contract.m_leverageRatio
    elif contract.m_deliveryType == 1:  # 假设 MMT_DT_INVERSE 为 1
        value = volume * contract.m_volumeMultiple / price * contract.m_leverageRatio
    elif contract.m_deliveryType == 2:  # 假设 MMT_DT_QUANTO 为 2
        value = volume * contract.m_volumeMultiple * price * contract.m_leverageRatio
    return value

def isGreater(left, right):
    """
    判断左值是否大于右值
    :param left: 左值
    :param right: 右值
    :return: 左值是否大于右值
    """
    return left > right + PRECISION

def isLess(left, right):
    """
    判断左值是否小于右值
    :param left: 左值
    :param right: 右值
    :return: 左值是否小于右值
    """
    return left < right - PRECISION

def isEqual(left, right):
    """
    判断左值是否等于右值
    :param left: 左值
    :param right: 右值
    :return: 左值是否等于右值
    """
    return abs(left - right) <= PRECISION


def isGreaterEqual(left, right):
    """
    判断左值是否大于等于右值
    :param left: 左值
    :param right: 右值
    :return: 如果左值大于等于右值则返回True，否则返回False
    """
    return left >= right - PRECISION