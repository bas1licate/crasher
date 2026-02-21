import subprocess as s,os,sys,ctypes as c
if not c.windll.shell32.IsUserAnAdmin():c.windll.shell32.ShellExecuteW(None,"runas",sys.executable,f'"{os.path.abspath(__file__)}"',None,1)
s.run([f'{os.environ["userprofile"]}/nmf/notmyfault64.exe',"/bugcheck","0xE2"])
