# mmtutility.py

# 假设这些枚举类型在其他文件中定义，这里简单模拟
MMT_OT_LIMIT = 1
MMT_OT_MARKET = 2
MMT_OT_STOP_LIMIT = 3
MMT_OT_STOP_MARKET = 4

def orderTypeToString(orderType):
    if orderType == MMT_OT_LIMIT:
        return "LIMIT"
    elif orderType == MMT_OT_MARKET:
        return "MARKET"
    elif orderType == MMT_OT_STOP_LIMIT:
        return "STOP_LIMIT"
    elif orderType == MMT_OT_STOP_MARKET:
        return "STOP_MARKET"
    else:
        return ""