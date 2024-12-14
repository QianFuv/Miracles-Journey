# 安装教程

欢迎您查看安装教程，有任何疑问请查看常见问题页面的如何提问栏并遵循相关提问途径礼貌提问

## 第一步 - 版本选择

|  版本  |                  特点                  |                           适用人群                           |             发布周期             |
| :----: | :------------------------------------: | :----------------------------------------------------------: | :------------------------------: |
| 稳定版 | 包含了最新一段时间之内的修改和错误修复 |          对于不追求最新版而追求稳定的玩家的最佳选择          | 新增、删除和修改内容足够多时发布 |
| 测试版 |      拥有最新的更新内容和错误修复      | 对于急需获取最新更新和错误修复的玩家和开发测试人员的最佳选择 |   每一次更新均为一次测试版发布   |

## 第二步 - 版本下载

> 由于整合包还处于测试阶段，因此<sapn class="marker-text">推荐下载最新测试版游玩</sapn>以获取最新更新和 Bug 修复

### 稳定版

:::tabs

== Github

1. 进入整合包最新版本的[发布页面](https://github.com/QianFuv/Miracles-Journey/releases/latest)
2. 点击 `Assets` 列表下的 `Miracles-Journey-x.x.x.zip` 文件下载（“x”为版本号）

== Alist

1. 进入整合包 [Alist 托管页面](https://alist.qianf.fun/)
2. 点击最上方`版本列表`文件夹进入整合包版本列表
3. 选择<sapn class="marker-text">修改时间最新的版本</sapn>右键选择下载

== 群文件

1. 进入整合包官方 Q 群：[点击加群](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=ZhRJUzbJ0KzlyBMu_SOcuqGkVg5VYpVT&authKey=g2%2BmqmzVTf1OeqqLgMRITVZ6ytQUm%2FoIG8BRqinpPGyD%2Bft5i72IuZprh8pRBI0m&noverify=0&group_code=160373490)
2. 在群文件内点击`版本列表`文件夹进入整合包版本列表
3. 选择<sapn class="marker-text">上传时间最新的版本</sapn>下载

== 自构建

1. 安装 [Go](https://go.dev/dl/) 语言环境
2. 安装 [Packwiz](https://github.com/packwiz/packwiz)：`go install github.com/packwiz/packwiz@latest`
3. 进入[仓库标签列表](https://github.com/QianFuv/Miracles-Journey/tags)，选择<sapn class="marker-text">最新的标签</sapn>下方对应的 `Zip` 文件按钮下载压缩包并解压至合适目录
4. 进入解压目录内的 `pack` 文件夹
5. 打开 Cmd 使用 `packwiz curseforge export` 导出整合包（导出的整合包为同目录下的 `Miracles-Journey-x.x.x.zip` 文件，“x”为版本号）

:::

### 测试版

:::tabs

== Github Actions

1. 进入整合包[自动构建页面](https://github.com/QianFuv/Miracles-Journey/actions)
2. 点击打开<sapn class="marker-text">最新的（最上面的）构建</sapn>
3. 没有登陆 Github 账号的需要在页面右上角登陆 Github（如已登录请跳过此步骤）
4. 点击页面下方 `Artifacts` 列表内的文件下载

== 自构建

1. 安装 [Go](https://go.dev/dl/) 语言环境
2. 安装 [Packwiz](https://github.com/packwiz/packwiz)：`go install github.com/packwiz/packwiz@latest`
3. 下载[最新仓库文件](https://github.com/QianFuv/Miracles-Journey/archive/refs/heads/main.zip)并解压至合适的目录
4. 进入解压目录内的 `pack` 文件夹
5. 打开 Cmd 使用 `packwiz curseforge export` 导出整合包（导出的整合包为同目录下的 `Miracles-Journey-x.x.x.zip` 文件，“x”为版本号）

:::

## 第三步 - 安装整合包

直接将下载好的压缩包拖入 [PCL](https://github.com/Hex-Dragon/PCL2) 和 [HMCL](https://github.com/HMCL-dev/HMCL) 安装即可，启动器会自动识别整合包名称和下载整合包全部文件

## 第四步 - Java 环境下载

> 本整合包借助 GraalvmJDK 提供的高性能优化方案和参数达到最大的优化效果，请您无论是否有安装过 Java 环境，都按照指南下载 GraalvmJDK
>

1. 进入整合包版本文件夹内的 `graalvm21` 文件夹，使用管理员运行 `download.bat` 脚本，将自动下载 GraalvmJDK21 到当前目录
2. 如果您使用的是 PCL 启动器，则不需要进行多余操作；如果使用的是 HMCL 启动器，需要在 `游戏设置` 中手动选择刚刚下载的 GraalvmJDK21

## 第五步 - 启动参数配置

推荐使用的启动参数为（只能与 GraalvmJDK 搭配使用）：

```
-XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysActAsServerClassMachine -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:AllocatePrefetchStyle=3 -XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=400M -XX:NonNMethodCodeHeapSize=12M -XX:ProfiledCodeHeapSize=194M -XX:NonProfiledCodeHeapSize=194M -XX:-DontCompileHugeMethods -XX:+PerfDisableSharedMem -XX:+UseFastUnorderedTimeStamps -XX:+UseCriticalJavaThreadPriority -XX:+EagerJVMCI -Dgraal.TuneInlinerExploration=1 -XX:+UseG1GC -XX:MaxGCPauseMillis=37 -XX:+PerfDisableSharedMem -XX:G1HeapRegionSize=16M -XX:G1NewSizePercent=40 -XX:G1ReservePercent=15 -XX:SurvivorRatio=32 -XX:G1MixedGCCountTarget=3 -XX:G1HeapWastePercent=20 -XX:InitiatingHeapOccupancyPercent=20 -XX:G1RSetUpdatingPauseTimePercent=0 -XX:MaxTenuringThreshold=1 -XX:G1SATBBufferEnqueueingThresholdPercent=30 -XX:G1ConcMarkStepDurationMillis=5.0 -XX:GCTimeRatio=99
```

粘贴上面的启动参数至下方启动器对应位置即可：

:::tabs

== PCL

`版本设置` -> `设置` -> `高级启动选项` -> `JVM 参数头`

== HMCL

`版本管理` -> `游戏设置` -> `启用版本特定游戏设置` -> `高级设置` -> `编辑高级设置` -> `游戏参数`

:::

## 第六步 - 启动器配置

### 内存分配

> 由于整合包体积较大，所以在实际游玩环境下由于元数据、缓存等原因内存会有额外 8G 左右的消耗

- 对于电脑内存为 16G 的玩家，不推荐游玩此整合包
- 对于电脑内存大于或等于 32G 的玩家，建议分配 12G 游玩本整合包（如果你的可用内存大于 24G，建议分配 16G 游玩）
