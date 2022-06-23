import os
import shutil
import contextlib
import subprocess

from optimise.data import *

class Optimiser:
    
    def __init__(self):
        self.ult_perf = "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"
        self.local = os.getenv("LOCALAPPDATA")
        self.roaming = os.getenv("APPDATA")
    
    def call_command(self, command: str, is_reg: bool=False):
        if is_reg:
            command = command.split(' ')
            with contextlib.suppress(IndexError):
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
    
    def del_reg(self, path: str, valueName: str=None):
        path = path.replace(' ', '^')
        if valueName is None:
            return self.call_command(f"Reg delete {path} /f", True)
        return self.call_command(f"Reg delete {path} /v {valueName} /f", True)
    
    def get_powerplans(self):
        return [powerplan for powerplan in self.get_output("powercfg /L").splitlines() if "Power Scheme GUID" in powerplan]

    def get_files_by_type(self, type: str):
        for root, __, files in os.walk("c:/"):
            for file in files:
                if file.endswith(f".{type}"):
                    yield os.path.join(root, file)

    def delete_file(self, folder, is_file=False):
        if not os.path.isdir(folder) and is_file is False:
            return
        if not is_file:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception:
                    yield (file_path, 1)
                else:
                    yield (file_path, 0)
        else:
            try:
                if os.path.isfile(folder) or os.path.islink(folder):
                    os.unlink(folder)
            except Exception:
                yield (folder, 1)
            else:
                yield (folder, 0)
    
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
        return "Successfully added/activated Ultimate Performance Powerplan."
    
    def power_optimisation(self):
        for path, values in powerReg.items():
            for valueName, type, value in values:
                rcode = self.add_reg(valueName, path, type, value).returncode
                yield (path, valueName, value, rcode)
        return
        
    def memory_optimisation(self):
        # Disable Memory Compression
        self.call_command('powershell -NoProfile -Command "Disable-MMAgent -mc"')
        # Memory Optimisation through Registry
        for path, values in memReg.items():
            for valueName, type, value in values:
                rcode = self.add_reg(valueName, path, type, value).returncode
                yield (path, valueName, value, rcode)
        for cmd, cmt in fsutil_cmds:
            rcode = self.call_command(cmd).returncode
            yield (cmt, rcode)

    def debloat(self):
        for path, values in debloatReg.items():
            for valueName, type, value in values:
                rcode = self.add_reg(valueName, path, type, value).returncode
                yield (path, valueName, value, rcode)
        for path in delBloatReg:
            rcode = self.del_reg(path).returncode
            yield (path, rcode)

    def cleaner(self):
        for data, app in cachePaths.items():
            if data == "local":
                for name in app:
                    for path in app[name]:
                        folder = self.local + path
                        for _path, rcode in self.delete_file(folder):
                            yield (_path, rcode)
            elif data == "roaming":
                for name in app:
                    for path in app[name]:
                        folder = self.roaming + path
                        for _path, rcode in self.delete_file(folder):
                            yield (_path, rcode)
            elif data == "misc":
                for name in app:
                    for folder in app[name]:
                        for _path, rcode in self.delete_file(folder):
                            yield (_path, rcode)
        
        for file in self.get_files_by_type("log"):
            for deleted_file, rcode in self.delete_file(file, True):
                yield (deleted_file, rcode)

    def gameBooster(self):
        for path, values in gameReg.items():
            for valueName, type, value in values:
                rcode = self.add_reg(valueName, path, type, value).returncode
                yield (path, valueName, value, rcode)