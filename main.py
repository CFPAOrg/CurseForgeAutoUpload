# !/usr/bin/python3

import os
import time

import requests


# 文件上传请求
def upload(file_name='', display_name='', changelog=''):
    headers = {'X-Api-Token': os.getenv('CFTOKEN')}
    file = {'file': file_name}
    metadata = {'meta': {"displayName": display_name,
                         "changelog": changelog,
                         "gameVersions": [
                             6756
                         ],
                         "releaseType": "release"
                         }
                }
    response = requests.post('http://httpbin.org/post', headers=headers, file=file, metadata=metadata)
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
        # 再剔除 zh_cn_old
        os.system('rm -f {}/project/assets/{}/lang/zh_cn_old.lang'.format(path, modid))
        # 最后判断文件是否为空
        if os.path.getsize('{}/project/assets/{}/lang/zh_cn.lang'.format(path, modid)) == 0:
            os.system('rm -rf {}/project/assets/{}'.format(path, modid))

    # 最后打包
    os.system('mv {}/project/assets ./'.format(path))
    os.system(
        'zip -r -9 "Minecraft-Mod-Language-Modpack-{}.zip" "assets" "pack.mcmeta"  "pack.png" "README.md" "LICENSE"'.format(
            version))


if __name__ == '__main__':
    # 获取 +1 的版本信息
    version_in = version_add(version_get(), 0, 0, 1)

    # 打包
    zip(path='Minecraft-Mod-Language-Package', version=version_in)

    # 上传
    file = 'Minecraft-Mod-Language-Package-{}.zip'.format(version_in)
    display = 'Minecraft-Mod-Language-Package-{}'.format(version_in)
    log = '自动更新，本次更新时间：{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # r = upload(file_name=file, display_name=display, changelog=log)

    # 存版本
    # if r.status_code == 200:
    #    version_set(version_in)
