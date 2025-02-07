# mmtcommissionrate.py

# 假设 mmtdatatype 模块中定义了 MMTCommissionRateType 枚举类型
# 这里简单用整数常量代替，实际使用时需要根据具体情况调整
MMT_CRT_NULL = 0

class MMTCommissionRate:
    def __init__(self):
        # 初始化成员变量
        self.m_type = MMT_CRT_NULL
        self.m_openRate = 0
        self.m_closeRate = 0
        self.m_closeTodayRate = 0
        # 初始化合约 ID 为空字符串
        self.m_contractId = ""

    def init(self):
        # 将合约 ID 置为空字符串
        self.m_contractId = ""
        # 将类型置为 MMT_CRT_NULL
        self.m_type = MMT_CRT_NULL
        # 将开仓、平仓、平今手续费率都置为 0
        self.m_openRate = self.m_closeRate = self.m_closeTodayRate = 0