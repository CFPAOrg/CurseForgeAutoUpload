![pack.png](https://i.loli.net/2018/02/18/5a8974407b453.png)
---

| CurseForge 下载量 | 支持版本 | 翻译进度 | Github Actions | 最新快照版本 |
| :--: | :--: | :--: | :--: | :--: |
| [![CurseForge](http://cf.way2muchnoise.eu/full_simplified-chinese-localization-resource-package_downloads.svg)](https://minecraft.curseforge.com/projects/simplified-chinese-localization-resource-package) | [![CurseForge](http://cf.way2muchnoise.eu/versions/simplified-chinese-localization-resource-package.svg)](https://minecraft.curseforge.com/projects/simplified-chinese-localization-resource-package)  | ![weblate](https://weblate.exz.me/widgets/langpack/-/svg-badge.svg) | ![Packer](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package/workflows/Packer/badge.svg?branch=1.12.2) | [![GitHub release](https://img.shields.io/github/release/CFPAOrg/Minecraft-Mod-Language-Package.svg)](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package/releases/latest) |

## 仓库说明

这是 Minecraft 模组汉化项目的仓库，本项目目前采用 Weblate 平台进行模组项目翻译；<br>
用以解决模组作者不接收汉化、汉化提交更新速度慢等诸多问题；<br>
想要参与翻译？请访问我们的官方网站，仔细阅读相关事宜加入我们：<br>

### <https://cfpa.team>

或者直接向这个仓库提交 PR 即可；

翻译还是需要有一些注意事项，具体参见：[《Minecraft Mod简体中文翻译规范与指南》](https://github.com/Meow-J/Mod-Translation-Styleguide/blob/master/README.md)。

## 授权

本作品采用 [知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)（[简体中文](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)）进行许可，[协议全文可在此找到](./LICENSE)。<br>

## 使用方式

点击 [此处](https://minecraft.curseforge.com/projects/simplified-chinese-localization-resource-package) 可打开 curseforge 页面下载 release 版本资源包。<br>
点击 [此处](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package/releases/latest) 可以下载快照版本资源包（推荐下载不带 Lite 的版本）。<br>
只需要像**普通材质包**一样，在游戏中加载上该资源包，即可拥有汉化。建议装上该资源包后重启游戏，避免出现其他问题。

## 相关信息

**目前的翻译计划是什么样的呢？我可以递交想翻译的列表么？**<br>
目前是基于 curseforge 网站，选取了 1.12.2 版本，按照受欢迎程度下载了 600 多个模组。如果你有什么想要额外添加翻译的模组，可以通过 github 的 issue，或者直接邮箱递交意见或建议。<br>
其他版本目前还暂时没有涉足计划（不过1.7.10应该是不会做了）。

关于具体的宣传，可以参见 [MCBBS 推广宣传帖](http://www.mcbbs.net/thread-774087-1-1.html)；<br>
关于整个事情的经过，可以查看酒石酸菌的[博客帖子](https://baka943.coding.me/2018/01/03/2018-01-03-AnIntroForWeblate/);

**你们是怎么做到流水线式的翻译的？**<br>
emmmm，原理其实很简单。<br>

- 通过爬虫爬取 curseforge 的热门模组；
- 脚本推送回 GitHub 仓库；
- Weblate 检测到仓库变动，自动抓取 GitHub 变动；
- 翻译人员在 Weblate 上翻译，Weblate 自动推回到 GitHub；
- Github Actions 检测到仓库变动，自动构建并打包；
- Github Actions 自动发布到 GitHub 的 release 上，以供下载；

## 鸣谢

感谢 `phi` 搭建出了 weblate 服务器，还实现了机翻功能；<br>
感谢 `PeakXing` 制作的logo；<br>
感谢 `雪尼`、`FledgeXu`、`asdflj` 等在内的诸多人的意见和建议；<br>
感谢 `雪尼`、`yuanjie000` 对 weblate 管理的维护和帮助； 感谢`卡米西村`各位提供的技术支持和服务器，能够使爬虫运行。<br>
感谢本项目的最初贡献者 `Aemande123`，`DYColdWind`，`Snownee`，`forestbat`，`3TUSK`，`SihenZhang`，`MoXiaoFreak`，`gloomy_banana`，`yuanjie000`，`exia00125`，`luckyu19` 提供的汉化。（排名不分先后）<br>
感谢玩家 `R_liu` 提供的拔刀剑本地化；<br>
资源包中镶嵌了 `3TUSK` 提供的[全角标点修复文件](./project/assets/minecraft/readme.md)；<br>
最后感谢那些参与翻译，并致力于本地化推广的各位玩家，你们辛苦了。<br>
在本页面的 [Contributors](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package/graphs/contributors) 页面可以查看所有翻译贡献者。
