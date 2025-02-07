# 导入必要的模块
from abc import ABC, abstractmethod
from typing import List, Dict

# 定义 MMTStrategyInterface 类，继承自 ABC（抽象基类）
class MMTStrategyInterface(ABC):
    # 定义析构函数，在 Python 中不需要显式声明为 virtual
    def __del__(self):
        pass

    # 定义抽象方法 getObject，对应 C++ 中的纯虚函数
    @abstractmethod
    def getObject(self):
        pass

    # 定义抽象方法 setFund，对应 C++ 中的纯虚函数
    @abstractmethod
    def setFund(self, fundId: str):
        pass

    # 定义抽象方法 getFundId，对应 C++ 中的纯虚函数
    @abstractmethod
    def getFundId(self) -> str:
        pass

    # 定义抽象方法 setAccounts，对应 C++ 中的纯虚函数
    @abstractmethod
    def setAccounts(self, accounts: List[Dict]):
        pass

    # 定义抽象方法 getAccounts，对应 C++ 中的纯虚函数
    @abstractmethod
    def getAccounts(self) -> List[Dict]:
        pass

    # 定义抽象方法 setStrategyId，对应 C++ 中的纯虚函数
    @abstractmethod
    def setStrategyId(self, strategyId: str):
        pass

    # 定义抽象方法 getStrategyId，对应 C++ 中的纯虚函数
    @abstractmethod
    def getStrategyId(self) -> str:
        pass

    # 定义抽象方法 setParameters，对应 C++ 中的纯虚函数
    @abstractmethod
    def setParameters(self, parameters: Dict):
        pass

    # 定义抽象方法 getParameters，对应 C++ 中的纯虚函数
    @abstractmethod
    def getParameters(self) -> Dict:
        pass

    # 定义抽象方法 start，对应 C++ 中的纯虚函数
    @abstractmethod
    def start(self):
        pass

    # 定义抽象方法 stop，对应 C++ 中的纯虚函数
    @abstractmethod
    def stop(self):
        pass