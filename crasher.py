import subprocess as s,os,sys,ctypes as c
def a():
    try:return c.windll.shell32.IsUserAnAdmin()
    except:return 0
if not a():c.windll.shell32.ShellExecuteW(None,"runas",sys.executable,f'"{os.path.abspath(__file__)}"',None,1)
s.run([f'{os.environ["userprofile"]}/nmf/notmyfault64.exe',"/bugcheck","0xE2"])