# mmtlinemanager.py

import os
import logging
from datetime import date

from mmtline import MMTLine
from include.mmtcontract import MMTContract
from include.mmttickdata import MMTTickData
from mmtfilemanager import MMTFileManager

class MMTLineManager:
    def __init__(self, line, contract, scale, maxCount=1000, minCount=500, isSave=False, isTick=False, historyDayCount=0, beforeDate=date.today()):
        self.m_lines = [line]
        self.m_contract = contract
        self.m_scale = scale
        self.m_maxCount = maxCount
        self.m_minCount = minCount
        self.m_isSave = isSave
        self.m_isTick = isTick
        self.m_historyDayCount = historyDayCount
        self.m_beforeDate = beforeDate
        self.init(line)

    def __del__(self):
        if self.m_isSave:
            self.saveLastLine()

    def init(self, line):
        self.m_lines.append(line)

        if self.m_isTick:
            self.readHistoryTicks()
        else:
            self.readHistoryLines()

        return True

    def onTick(self, tickData):
        if tickData.m_time is None:
            return

        lastLine = self.m_lines[-1] if self.m_lines else None
        if lastLine is None:
            return

        newLines = lastLine.newLine(tickData, self.m_scale, self.m_contract)
        if not newLines:
            lastLine.update(tickData, self.m_scale, self.m_contract)
        else:
            for tempLine in newLines:
                if self.m_isSave:
                    self.saveLastLine()
                self.m_lines.append(tempLine)
                if len(self.m_lines) > self.m_maxCount:
                    self.m_lines.pop(0)

    def onLine(self, line):
        if line.m_startTime is None:
            return

        lastLine = self.m_lines[-1] if self.m_lines else None
        if lastLine is None:
            return

        newLines = lastLine.newLine(line, self.m_scale, self.m_contract)
        if not newLines:
            lastLine.update(line, self.m_scale, self.m_contract)
        else:
            for tempLine in newLines:
                # if self.m_isSave:
                #     logging.info("SAVE LAST LINE")
                #     self.saveLastLine()
                self.m_lines.append(tempLine)
                if len(self.m_lines) > self.m_maxCount:
                    self.m_lines.pop(0)

    def size(self):
        return len(self.m_lines)

    def isNull(self):
        return not self.m_lines or self.m_lines[0].m_startTime is None

    def getLine(self, index):
        if index < 0:
            return None
        if self.size() < index + 1:
            return None
        return self.m_lines[self.size() - index - 1]

    def readHistoryLines(self):
        if self.m_historyDayCount <= 0:
            return

        lines = MMTFileManager.getLines(self.m_contract.m_id, self.m_historyDayCount, self.m_beforeDate)
        for line in lines:
            self.onLine(line)

    def readHistoryTicks(self):
        if self.m_historyDayCount <= 0:
            return

        tickDatus = MMTFileManager.getTicks(self.m_contract.m_id, self.m_historyDayCount, self.m_beforeDate)
        for tickData in tickDatus:
            self.onTick(tickData)

    def saveLastLine(self):
        if self.m_scale != 60.0:
            return

        line = self.m_lines[-1] if self.m_lines else None
        if line is None:
            return

        file_path = os.path.join(MMTFileManager.getM1Dir(self.m_contract.m_id), f"{self.m_contract.m_id}_{line.m_startTime.strftime('%Y%m%d')}.csv")
        try:
            with open(file_path, 'a') as file:
                file.write(f"{line.m_startTime.strftime('%Y-%m-%d %H:%M:%S')},{line.m_open:.6f},{line.m_high:.6f},{line.m_low:.6f},{line.m_close:.6f},{line.m_volume:.6f},{line.m_turnover:.6f},{line.m_openInterest:.6f},0.0\n")
        except Exception as e:
            logging.info(f"can't open file to save last line. contract id: {self.m_contract.m_id}. time: {line.m_startTime.strftime('%Y-%m-%d %H:%M:%S')}")