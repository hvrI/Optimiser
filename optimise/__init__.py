import os
import subprocess

from optimise.data import *

class Optimiser:
    
    def __init__(self):
        self.ult_perf = "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"
    
    def call_command(self, command: str, is_reg: bool=False):
        if is_reg:
            command = command.split(' ')
            command[2] = command[2].replace('^', ' ')
            command[4] = command[4].replace('^', ' ')
            return subprocess.run(command, stdout=subprocess.DEVNULL)
        return subprocess.run(command.split(' '), stdout=subprocess.DEVNULL)
    
    def get_output(self, command: str):
        return subprocess.check_output(command.split(' ')).decode('utf-8')
    
    def add_reg(self, valueName: str, path: str, type: str, value: str):
        valueName = valueName.replace(' ', '^')
        path = path.replace(' ', '^')
        return self.call_command(f"Reg add {path} /v {valueName} /t {type} /d {value} /f", True)
    
    def del_reg(self, valueName: str, path: str):
        path = path.replace(' ', '^')
        return self.call_command(f"Reg delete {path} /v {valueName} /f", True)
    
    def get_powerplans(self):
        return [powerplan for powerplan in self.get_output("powercfg /L").splitlines() if "Power Scheme GUID" in powerplan]
    
    def powerplan(self):
        powerplans = self.get_powerplans()
        current_powerplan = [powerplan for powerplan in powerplans if '*' in powerplan][-1]
        if "Ultimate Performance" in current_powerplan:
            return "Ultimate Performance Powerplan has already in use."
        for powerplan in powerplans:
            if "Ultimate Performance" in powerplan:
                break
        else:
            self.call_command(self.ult_perf)
        powerplans = self.get_powerplans()
        ult_perf = [powerplan for powerplan in powerplans if 'Ultimate Performance' in powerplan][-1]
        ult_perf_id = ult_perf[ult_perf.index(': ') + 2 : ult_perf.index('  (')]
        self.call_command(f"powercfg /SETACTIVE {ult_perf_id}")
        return "Successfully added/activated Ultimate Performance Powerplan"
    
    def power_optimisation(self):
        for path, values in powerReg.items():
            for valueName, type, value in values:
                self.add_reg(valueName, path, type, value)
        return
        
    def memory_optimisation(self):
        # Fsutil
        for cmd in fsutil_cmds:
            self.call_command(cmd)
        # Disable Memory Compression
        self.call_command('powershell -NoProfile -Command "Disable-MMAgent -mc"')
        # Memory Optimisation through Registry
        for path, values in memReg.items():
            for valueName, type, value in values:
                self.add_reg(valueName, path, type, value)
            
        print("Optimised memory")
