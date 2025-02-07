from typing import Set
from abc import ABC, abstractmethod

class MMTTradeApiInterface(ABC):
    @abstractmethod
    def getObject(self):
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def setFund(self, fundId: str):
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def getFundId(self) -> str:
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def setAccountParameters(self, parameters: dict):
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def getAccountParameters(self) -> dict:
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def addSubcribeContracts(self, contracts: Set[str]):
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def getSubcribeContracts(self) -> Set[str]:
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def start(self):
        # 抽象方法，需要在子类中实现
        pass

    @abstractmethod
    def stop(self):
        # 抽象方法，需要在子类中实现
        pass