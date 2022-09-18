import requests, time, linecache, os, subprocess, sys
version = (linecache.getline(r'.\steamapps\common\Counter-Strike Global Offensive Beta - Dedicated Server\csgo\steam.inf',3)).split('PatchVersion=')[1] #读Steam.inf
download = (linecache.getline(r'.\AutoUpdateSetting.ini',1).split('Download=')[1]).replace("\n", "") #读Steamcmd.exe参数
start = (linecache.getline(r'.\AutoUpdateSetting.ini',2).split('ServerStart=')[1]).replace("\n", "") #读Srcds.exe参数
os.system('color 0f') #设置黑底亮白色
print("开发 & 调试: ELDment")
print("技术援助 & 赞助: Minio & Tea")
print("程序状态: 运行中！\n")
flag = 0
while flag == 0:
    get = requests.get('http://api.steampowered.com/ISteamApps/UpToDateCheck/v1/?appid=730&version=' + version) #查询版本
    get.encoding = 'utf-8'
    check = get.text[41:45] #切割str
    if check != "true": #判断版本是否过时，如未过时切割后的str应为true
        print("[AU] 版本过时! [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]") #世界级Debug
        flag = 1 #世界级Debug
    else:
        print("[AU] 版本未过时...持续探测中 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]") #世界级Debug
        #flag = 1 #世界级Debug
        time.sleep(300) #防止CPU累坏了，给他休息10秒 XDD
###################################################################
#############以上代码是一个循环，版本过时后会执行以下代码#############
###################################################################
time.sleep(10)
#print("出来了！！！") #世界级Debug
os.system('cls') #设置黑底亮白色
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
print("开发 & 调试: ELDment")
print("技术援助 & 赞助: Minio & Tea\n")
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('taskkill /f /t /im srcds.exe>nul')
print("已强制结束Srcds进程。 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('echo ' + download + '>AutoUpdateTool.bat') #强制写出bat
print("已强制写出Steamcmd启动脚本。 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('echo Developer ^& Debugger: ELDment >AutoUpdateLog.txt')
os.system('echo Technical Assistance ^& Sponsorship: Minio ^& Tea >>AutoUpdateLog.txt') #在这里由衷感谢Minio提供的帮助以及茶糜（Tea社服主）提供的测试服务器！
os.system('echo ========================================================================== >>AutoUpdateLog.txt')
print("开始更新并订阅进程，更新状态你可以在本程序所在目录下AutoUpdateLog.txt中查看。 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
res = subprocess.Popen(["AutoUpdateTool.bat"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8") #订阅下载进程
while res.poll() is None: #进程是否终止
    filename = 'AutoUpdateLog.txt'
    with open(filename, 'a') as file_object:
        file_object.write(res.stdout.readline()) #写出订阅进程的控制台输出（这个输出是方便你debug的，本程序并不会调用它[我说这句话，是为了防止你在看代码的时候心想：这个B...站用户输出控制台干嘛？]）
###################################################################
#############以上代码是一个循环，进程终止后会执行以下代码#############
###################################################################
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('cd .\steamapps\common\Counter-Strike Global Offensive Beta - Dedicated Server&&echo ' + start + ' >AutoUpdateServerTool.bat&&ping -n 2 127.0.0.1>nul&&start AutoUpdateServerTool.bat') #强制写出Srcds.exe启动bat
print("已强制写出Srcds启动脚本，并且该脚本已经启动。 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('cd %cd%&&echo ping -n 10 127.0.0.1^>nul>AutoUpdateRestart.bat&&echo start ' + os.path.basename(sys.argv[0]) + '>>AutoUpdateRestart.bat') #强制写重启程序
print("已强制写出本程序重启启动脚本，并且该脚本已经启动。 [" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]")
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('start AutoUpdateRestart.bat') #启动重启程序
os._exit(0) #结束自己等待重开
