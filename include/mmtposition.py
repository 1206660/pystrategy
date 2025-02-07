# mmtposition.py

class MMTPosition:
    # 类的初始化方法，当创建对象时，如果没有传入参数，使用默认值初始化
    def __init__(self, fundId="", accountId="", tradeApiType=0, contractId=""):
        # 资金 ID
        self.m_fundId = fundId
        # 账户 ID
        self.m_accountId = accountId
        # 交易 API 类型
        self.m_tradeApiType = tradeApiType
        # 合约 ID
        self.m_contractId = contractId
        # 净持仓
        self.m_netPosition = 0.0
        # 多头持仓
        self.m_longPosition = 0.0
        # 空头持仓
        self.m_shortPosition = 0.0
        # 今日净持仓
        self.m_netPositionToday = 0.0
        # 今日多头持仓
        self.m_longPositionToday = 0.0
        # 今日空头持仓
        self.m_shortPositionToday = 0.0
        # 开仓价格
        self.m_openPrice = 0.0

    # 判断持仓是否为零的方法
    def isZero(self):
        return self.m_longPosition == 0.0 and self.m_longPositionToday == 0.0 and \
               self.m_shortPosition == 0.0 and self.m_shortPositionToday == 0.0


# 以下是使用示例
if __name__ == "__main__":
    # 创建一个 MMTPosition 对象，不传入参数，使用默认值初始化
    pos1 = MMTPosition()
    print(pos1.isZero())  # 输出: True

    # 创建一个 MMTPosition 对象，传入参数进行初始化
    pos2 = MMTPosition("FUND123", "ACCOUNT456", 1, "CONTRACT789")
    print(pos2.m_fundId)  # 输出: FUND123