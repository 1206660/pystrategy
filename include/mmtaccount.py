# 假设 mmtdatatype 模块中定义了 MMTTradeApiType 和 MMTCurrency 枚举类型
# 这里简单用整数常量代替，实际使用时需要根据具体情况调整
MMT_TAT_NULL = 0
MMT_CUR_CNY = 1

class MMTAccount:
    def __init__(self):
        # 初始化成员变量
        self.m_id = ""
        self.m_name = ""
        self.m_password = ""

        # ctp 相关
        self.m_brokerId = ""
        self.m_frontAddressMd = ""
        self.m_frontAddressTrade = ""
        self.m_productInfo = ""
        self.m_authCode = ""

        # deribit 相关
        self.m_apiKey = ""
        self.m_apiSecret = ""
        self.m_restUrl = ""
        self.m_websocketUrl = ""

        # ok 相关
        self.m_passPhrase = ""
        self.m_contractType = ""

        # ht 相关
        self.m_fundAccountId = ""  # 资金账号
        self.m_orderStation = ""

        self.m_tradeApiType = MMT_TAT_NULL
        self.m_balance = 0
        self.m_available = 0
        self.m_currentMargin = 0
        self.m_currency = MMT_CUR_CNY

        self.m_tradeApi = None

# 重载 == 运算符
def operator_eq(account1, account2):
    return account1.m_id == account2.m_id and account1.m_tradeApiType == account2.m_tradeApiType

# 重载 < 运算符
def operator_lt(account1, account2):
    if account1.m_id < account2.m_id:
        return True
    elif account1.m_id > account2.m_id:
        return False
    return account1.m_tradeApiType < account2.m_tradeApiType

# 定义 MMTAccountPointer 类型，在 Python 中可以使用类的实例来代替指针
MMTAccountPointer = MMTAccount