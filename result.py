import json
import os
import shutil
import sys
import time

from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service

author = """
    _    _                         _                    ____  _
   / \  | |_      ____ _ _   _ ___| |    __ _ _____   _|___ \/ |
  / _ \ | \ \ /\ / / _` | | | / __| |   / _` |_  / | | | __) | |
 / ___ \| |\ V  V / (_| | |_| \__ \ |__| (_| |/ /| |_| |/ __/| |
/_/   \_\_| \_/\_/ \__,_|\__, |___/_____\__,_/___|\__, |_____|_|
                         |___/                    |___/
"""


def hello_page():
    print(author)
    print("******************** XCU教务系统成绩查询助手 ********************")
    print("resp: https://github.com/AlwaysLazy21/zhengfang-result")


def init():
    config_path = f"C:/Users/{os.environ['HOMEPATH'][7:]}/result"
    if not os.path.exists(config_path): os.makedirs(config_path)
    if os.path.exists('./msedgedriver.exe'):
        shutil.move('./msedgedriver.exe', f'{config_path}/msedgedriver.exe')
    elif os.path.exists(f'{config_path[:-7]}/Desktop/msedgedriver.exe'):
        shutil.move(f'{config_path[:-7]}/Desktop/msedgedriver.exe', f'{config_path}/msedgedriver.exe')
    if not os.path.exists(f"{config_path}/msedgedriver.exe"):
        input("注意：没有找到msedgedriver.exe程序，请仔细查看 readme.md 文件")
        sys.exit()
    return json_reader()


def json_reader():
    config_path = f"C:/Users/{os.environ['HOMEPATH'][7:]}/result/config.json"
    user_info = {'教务系统登录界面网址': "", "用户名": "", "密码": "", }
    if not os.path.exists(config_path):
        return user_info
    else:
        with open(config_path, mode="r", encoding="utf-8") as f:
            info = f.read()
        if info == '' or info == {}:
            return user_info
        else:
            return json.loads(info)


def set_message(user):
    info_status = user['教务系统登录界面网址'] and user['用户名'] and user['密码']
    if info_status:
        sel = input("是（回车）/否（n）登录上次账号：")
        if not sel:
            return user
        else:
            print("使用回车跳过修改")
    for item in user:
        user[item] = input(f"{item}: ") or user[item]
    return user


def get_result(user):  # 操作selenium控制edge查成绩
    web = Edge(service=Service(f"C:/Users/{os.environ['HOMEPATH'][7:]}/result/msedgedriver.exe"))
    web.get(user['教务系统登录界面网址'])
    web.find_element(by="xpath", value='//*[@id="yhm"]').send_keys(user['用户名'])
    web.find_element(by="xpath", value='//*[@id="mm"]').send_keys(user['密码'])
    web.find_element(by="xpath", value='//*[@id="dl"]').click()
    time.sleep(2)
    web.find_element(by="xpath", value='/html/body/div[3]/div/nav/ul/li[4]').click()
    web.find_element(by="xpath", value='/html/body/div[3]/div/nav/ul/li[4]/ul/li[5]/a').click()
    web.switch_to.window(web.window_handles[-1])
    time.sleep(2)
    web.find_element(by="xpath", value='//*[@id="xnm_chosen"]/a/span').click()
    web.find_element(by="xpath", value='//*[@id="xnm_chosen"]/div/ul/li[1]').click()
    web.find_element(by="xpath", value='//*[@id="xqm_chosen"]/a/span').click()
    web.find_element(by="xpath", value='//*[@id="xqm_chosen"]/div/ul/li[1]').click()
    web.find_element(by="xpath", value='//*[@id="search_go"]').click()
    input("按任意键后，保存信息并退出程序...")
    with open(f"C:/Users/{os.environ['HOMEPATH'][7:]}/result/config.json", mode='w', encoding='utf-8') as f:
        f.write(json.dumps(user))
    web.close()
    web.switch_to.window(web.window_handles[0])
    web.close()


if __name__ == '__main__':
    hello_page()
    user_mess = init()
    user_mess = set_message(user_mess)
    get_result(user_mess)
