
import time
from mmtturtlestrategy import MMTTurtleStrategy

# 简单测试
if __name__ == "__main__":
    strategy = MMTTurtleStrategy()
    # 初始化完成标志，假设需要设置为True
    strategy.m_isInit = True  

    # 模拟一些数据，实际使用中需要根据具体情况替换
    # 例如，这里需要模拟 contracts 数据并调用 onContracts 方法
    # contracts = [...]
    # strategy.onContracts(contracts)

    while True:
        try:
            # 调用 update 方法
            strategy.update()
            # 可以在这里添加其他需要持续执行的逻辑

            # 模拟每1秒执行一次，可根据实际需求调整时间间隔
            time.sleep(1)  
        except KeyboardInterrupt:
            print("程序已停止")
            break