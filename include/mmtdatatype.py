# mmtdatatype.py

# 定义精度常量
PRECISION = 1E-10

# 交易所
class MMTExchange:
    # NULL
    MMT_EX_NULL = 0
    # 中金所
    MMT_EX_CFFEX = 1
    # 上海期货交易所
    MMT_EX_SHFE = 2
    # 大连期货交易所
    MMT_EX_DCE = 3
    # 郑州期货交易所
    MMT_EX_CZCE = 4
    # 上海能源交易所
    MMT_EX_INE = 5
    # 上海证券交易所
    MMT_EX_SSE = 6
    # 深圳证券交易所
    MMT_EX_SZSE = 7
    # DERIBIT
    MMT_EX_DERIBIT = 8
    # OKEX
    MMT_EX_OKEX = 9

# 合约类型
class MMTContractType:
    # NULL
    MMT_CT_NULL = 0
    # 股票
    MMT_CT_STOCK = 1
    # 期货
    MMT_CT_FUTURES = 2
    # 期权
    MMT_CT_OPTION = 3

# 结算类型
class MMTDeliveryType:
    # NULL
    MMT_DT_NULL = 0
    # 普通合约
    MMT_DT_NORMAL = 1
    # 反向合约
    MMT_DT_INVERSE = 2
    # quanto合约
    MMT_DT_QUANTO = 3

# 交易方向
class MMTTradeDirection:
    # NULL
    MMT_TD_NULL = 0
    # 开多
    MMT_TD_BUY = 1
    # 平多
    MMT_TD_SELL = 2
    # 开空
    MMT_TD_SELLSHORT = 3
    # 平空
    MMT_TD_BUYTOCOVER = 4

# 订单类型
class MMTOrderType:
    # NULL
    MMT_OT_NULL = 0
    # 限价单
    MMT_OT_LIMIT = 1
    # 市价单
    MMT_OT_MARKET = 2
    # 损价单
    MMT_OT_STOP_LIMIT = 3
    # 损价市价单
    MMT_OT_STOP_MARKET = 4

# 订单开平类型
class MMTOrderOpenCloseType:
    # NULL
    MMT_OOCT_NULL = 0
    # 开仓
    MMT_OOCT_OPEN = 1
    # 平仓
    MMT_OOCT_CLOSE = 2
    # 平昨
    MMT_OOCT_CLOSE_YESTODAY = 3
    # 平今
    MMT_OOCT_CLOSE_TODAY = 4

# 订单状态
class MMTOrderStatus:
    # 未知
    MMT_OS_NULL = 0
    # 已经发送
    MMT_OS_SENT = 1
    # 挂单
    MMT_OS_PENDING = 2
    # 部分成交
    MMT_OS_PART_FILLED = 3
    # 成交
    MMT_OS_FILLED = 4
    # 部成部撤
    MMT_OS_PART_CANCELLED = 5
    # 撤单
    MMT_OS_CANCELLED = 6
    # 部分撤单
    MMT_OS_PART_REJECTED = 7
    # 拒绝
    MMT_OS_REJECTED = 8
    # 损价单未触发
    MMT_OS_UNTRIGGERED = 9
    # 未完成
    MMT_OS_NOT_DONE = 10
    # 完成
    MMT_OS_DONE = 11

# 交易接口
class MMTTradeApiType:
    # NULL
    MMT_TAT_NULL = 0
    # CTP
    MMT_TAT_CTP = 1
    # DERIBIT
    MMT_TAT_DERIBIT = 2
    # OKEX
    MMT_TAT_OKEX = 3
    # HuaTai
    MMT_TAT_HT = 4

# 手续费类型
class MMTCommissionRateType:
    # NULL
    MMT_CRT_NULL = 0
    # 按照合约价值
    MMT_CRT_VALUE = 1
    # 按照合约数量
    MMT_CRT_VOLUME = 2

# 币种类型
class MMTCurrency:
    # NUL
    MMT_CUR_NULL = 0
    # 人民币
    MMT_CUR_CNY = 1
    # 美元
    MMT_CUR_USD = 2
    # 港币
    MMT_CUR_HKD = 3
    # BTC
    MMT_CUR_BTC = 4
    # ETH
    MMT_CUR_ETH = 5
    # USDT
    MMT_CUR_USDT = 6

# 价格类型
class MMTPrictType:
    # NULL
    MMT_PT_NULL = 0
    # 开盘价
    MMT_PT_OPEN = 1
    # 最高价
    MMT_PT_HIGH = 2
    # 最低价
    MMT_PT_LOW = 3
    # 收盘价
    MMT_PT_CLOSE = 4