import requests, time, linecache, os, subprocess, sys
version = (linecache.getline(r'.\steamapps\common\Counter-Strike Global Offensive Beta - Dedicated Server\csgo\steam.inf',3)).split('PatchVersion=')[1] #读Steam.inf
download = (linecache.getline(r'.\AutoUpdateSetting.ini',1).split('Download=')[1]).replace("\n", "") #读Steamcmd.exe参数
start = (linecache.getline(r'.\AutoUpdateSetting.ini',2).split('ServerStart=')[1]).replace("\n", "") #读Srcds.exe参数

flag = 0
while flag == 0:
    get = requests.get('http://api.steampowered.com/ISteamApps/UpToDateCheck/v1/?appid=730&version=' + version) #查询版本
    get.encoding = 'utf-8'
    check = get.text[41:45] #切割str
    if check != "true": #判断版本是否过时，如未过时切割后的str应为true
        print("版本过时!!!!!") #世界级Debug
        flag = 1 #世界级Debug
    else:
        print("版本未过时") #世界级Debug
        #flag = 1 #世界级Debug
    time.sleep(10) #防止CPU累坏了，给他休息10秒
###################################################################
#############以上代码是一个循环，版本过时后会执行以下代码#############
###################################################################
#print("出来了！！！") #世界级Debug
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('echo ' + download + '>AutoUpdateTool.bat') #强制写出bat
time.sleep(1) #每天一个好习惯：让代码歇一会 XDD
os.system('echo Developer ^& Debugger: ELDment >AutoUpdateLog.txt')
os.system('echo Technical Assistance ^& Sponsorship: Minio ^& Tea >>AutoUpdateLog.txt') #在这里由衷感谢Minio提供的帮助以及茶糜（Tea社服主）提供的测试服务器！
os.system('echo ========================================================================== >>AutoUpdateLog.txt')
res = subprocess.Popen(["AutoUpdateTool.bat"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8") #订阅下载进程
while res.poll() is None: #进程是否终止
    filename = 'AutoUpdateLog.txt'
    with open(filename, 'a') as file_object:
        file_object.write(res.stdout.readline()) #写出订阅进程的控制台输出（这个输出是方便你debug的，本程序并不会调用它[我说这句话，是为了防止你在看代码的时候心想：这个B...站用户输出控制台干嘛？]）
###################################################################
#############以上代码是一个循环，进程终止后会执行以下代码#############
###################################################################
os.system('cd .\steamapps\common\Counter-Strike Global Offensive Beta - Dedicated Server&&echo ' + start + ' >AutoUpdateServerTool.bat&&ping -n 2 127.0.0.1>nul&&AutoUpdateServerTool.bat') #强制写出Srcds.exe启动bat
os.system('echo ping -n 10 127.0.0.1>nul&&' + os.path.basename(sys.argv[0]) + ' >AutoUpdateRestart.bat') #强制写重启程序
os.system('AutoUpdateRestart.bat') #启动重启程序
sys.exit(1) #结束自己等待重开
