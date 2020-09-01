#!/usr/bin/python3
from urllib.request import Request, urlretrieve
from urllib.request import urlopen

import paramiko
import sys
import os
import time
import json

import requests


# 文件上传请求
def upload(file_name='', display_name='', changelog=''):
    header = {'X-Api-Token': sys.argv[1]}  # os.getenv('CFTOKEN')
    meta = {'metadata': json.dumps({"displayName": display_name, "changelog": changelog, "gameVersions": [
                                   6756], "releaseType": "release"}, ensure_ascii=False)}

    response = requests.post('https://minecraft.curseforge.com/api/projects/268591/upload-file',
                             headers=header, data=meta, files={'file': (file_name, open(file_name, 'rb'))})
    return response


# 没弄到如何获取已有版本信息，放弃，直接改成存文件
def version_get():
    version = ''
    with open('version.txt', 'r', encoding='utf-8') as f:
        version = f.readline().rsplit('\n')
    return version[0]


# 版本自动加
# i j k 对应 version 的三个版本数字
def version_add(version, i=0, j=0, k=0):
    version_list = version.split('.', 2)
    i = int(version_list[0]) + i
    j = int(version_list[1]) + j
    k = int(version_list[2]) + k
    return '{}.{}.{}'.format(str(i), str(j), str(k))


# 写入版本信息
def version_set(version):
    with open('version.txt', 'w', encoding='utf-8') as f:
        f.writelines(version)


# 资源包打包
# 传入 project 所在的文件夹
def zip(path='.', version=''):
    for modid in os.listdir(path + '/project/assets'):
        # 先判断 zh_cn 存在不存在
        if not os.path.exists('{}/project/assets/{}/lang/zh_cn.lang'.format(path, modid)):
            continue
        # 剔除 en_us
        os.system('rm -f {}/project/assets/{}/lang/en_us.lang'.format(path, modid))
        # 剔除 en_us_old
        os.system(
            'rm -f {}/project/assets/{}/lang/en_us_old.lang'.format(path, modid))
        # 再剔除 zh_cn_old
        os.system(
            'rm -f {}/project/assets/{}/lang/zh_cn_old.lang'.format(path, modid))
        # 最后判断文件是否为空
        if os.path.getsize('{}/project/assets/{}/lang/zh_cn.lang'.format(path, modid)) == 0:
            os.system('rm -rf {}/project/assets/{}'.format(path, modid))

    # 最后打包
    os.system('mv {}/project/* ./'.format(path))
    os.system(
        'zip -r -9 "Minecraft-Mod-Language-Package-{}.zip" "assets" "pack.mcmeta"  "pack.png" "README.md" "LICENSE"'.format(
            version))
    os.system('rm -rf ./Minecraft-Mod-Language-Package')
    os.system('rm -rf ./assets')
    os.system('rm -rf ./pack.png')
    os.system('rm -rf ./pack.mcmeta')

# 获取文件下载地址


def get_file():
    request = Request(
        'https://api.github.com/repos/CFPAOrg/Minecraft-Mod-Language-Package/releases/latest')
    response_body_bytes = urlopen(request).read()
    response_body_str = str(response_body_bytes, 'utf-8')
    cache_json = json.loads(response_body_str)
    url = cache_json['assets'][0]["browser_download_url"]
    return url

def scp_file()
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sys.argv[2], port=12356, username=root, password=sys.argv[3])
    with closing(Read(ssh_client.get_transport(), '/var/www/html/files/')) as scp:
        scp.receive('Minecraft-Mod-Language-Modpack.zip')

if __name__ == '__main__':
    # 获取 +1 的版本信息
    version_in = version_add(version_get(), 0, 0, 1)

    # 打包
    #zip(path='Minecraft-Mod-Language-Package', version=version_in)
    # 重命名
    print("下载最新文件……")
    scp_file()
    print("下载完成")
    file = 'Minecraft-Mod-Language-Package-{}.zip'.format(version_in)
    os.rename("Minecraft-Mod-Language-Modpack.zip", file)
    print("重命名完成")

    # 上传
    display = 'Minecraft-Mod-Language-Package-{}'.format(version_in)
    log = '自动更新，本次更新时间：{}'.format(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()))
    r = upload(file_name=file, display_name=display, changelog=log)

    os.remove(file)
    # 存版本
    if (r.status_code == 200):
        version_set(version_in)
