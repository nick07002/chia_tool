# Chia铭文 FAQ:

## 支持什么操作系统？

代码可以支持Linux (Ubuntu, Centos, Redhat, Deepin等）MacOS 都经过了测试。

Windows有版友也跑起来了。


## 我怎么安装python  或者python3?

英文教程 ： https://www.python.org/download/releases/2.5/msi/

中文教程： https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624

确定你的python安装好再进行下一步

## 如何安装 Chia 客户端。
https://www.chia.net/downloads/ 


## 如何验证chia客户端安装完成。

### A) Linux 系统，打开命令行，输入 `chia` 你应该看到如下信息
   `Usage: chia [OPTIONS] Command [ARGS]`
   
如果没有看到以上信息做如下操作：
   
1. 使用你熟悉的文本编辑器打开 `~/.bashrc` 文件。如果你熟悉Linux，可以使用 vi、emacs 等工具，如果不熟悉，
   也可以使用 gedit 等工具打开。如果需要安装 gedit，你可以参考 [gedit 安装教程](https://help.ubuntu.com/community/gedit)。

2. 在 `~/.bashrc` 文件中添加以下一行代码：
   ```shell
   export PATH=$PATH:/usr/bin
3. 在命令行中输入以下命令以使更改生效：
   ```shell
   source ~/.bashrc
   ```
   
   然后重新测试 chia 命令，现在应该可以正常运行了。
      

### B) Mac 系统，打开命令行，输入 `chia` 你应该看到如下信息
   `Usage: chia [OPTIONS] Command [ARGS]`
   
如果没有看到以上信息做如下操作：
   
1. 用你熟悉的编辑器打开 ~/.bashrc  如果你熟悉Linux 可以用 vi , emacs等工具，如果不熟悉，
       可以用atom 编辑器等工具打开。 (atom 安装教程 https://formulae.brew.sh/cask/atom) 

2. 在 `~/.bashrc` 文件中添加以下一行代码：
   ```shell
   export PATH=/Applications/Chia.app/Contents/Resources/app.asar.unpacked/daemon
3. 在命令行中输入以下命令以使更改生效：
   ```shell
   source ~/.bashrc
   ```
   
   然后重新测试 chia 命令，现在应该可以正常运行了。

## 如何运行？
在命令行里，先进入到你下载 mojo.py的文件夹。
比如在mac上，你下载了mojo.py在桌面，那你可以做如下动作
``` shell
cd ~/Desktop/
python3 mojo.py --finger <你的钱包指纹>
```
注意：实际输入命令时，不要加 `< > ` 符号

## 如何找到钱包指纹

打开chia客户端图形界面，（如果第一次打开，需要创建钱包）左上角10位数字就是你的钱包指纹
![chia UI](https://github.com/nick07002/chia_tool/blob/f1f7422cf3a6ec12091764f0c1893f78da97c166/chiafinger.png)


------

## 如何打散UTXO

我把命令行回复中英文部分翻译成中文利于理解。
首先，列出可用的币种：

``` shell
chia wallet coins list -f 590161281
```
响应：
``` shell
钱包1中总共有1个币。
1个已确认币。
0个未确认的添加。
0个未确认的移除。
已确认的币：
币ID：0x5dc5106862c7e00b0611b79137dbd7520e4c90da1bbbadb01a4518e3e4ec1797
        地址：xch1ju90mhn8nq7nnd25whap56ajf6eraxayw6qlk6f7sr0w3jf5d2ps9x0zzu 金额：0.991489895996  (991489895996 mojo)，在区块3065530中已确认
```

将现有的币分成5个0.15 XCH的币，并包含1000 mojo的区块链费用：
``` shell
chia wallet coins split -f 590161281 --number-of-coins 5 --amount-per-coin 0.15 --target-coin-id 0x5dc5106862c7e00b0611b79137dbd7520e4c90da1bbbadb01a4518e3e4ec1797 --fee 0.000000001
``` shell
结果：


``` shell
交易已发送：2489efe8c89e72459a09bb681b121c3acee0e9f40d65c37c8a9d98bb7cb47d09
要获取状态，请使用命令：chia wallet get_transaction -f 590161281 -tx 0x2489efe8c89e72459a09bb681b121c3acee0e9f40d65c37c8a9d98bb7cb47d09
```
查看交易的结果：

``` shell
chia wallet get_transaction -f 590161281 -tx 0x2489efe8c89e72459a09bb681b121c3acee0e9f40d65c37c8a9d98bb7cb47d09
```
结果：

``` shell
交易 2489efe8c89e72459a09bb681b121c3acee0e9f40d65c37c8a9d98bb7cb47d09
状态：已确认
发送金额：0.75 XCH
至地址：xch1p2hs025nkujyqk4a6qxfxfde6uvcajqhmq2kzvacj79wf8kfvaxqw3t4zp
创建时间：2023-01-05 16:15:31
```

最后，在分割后再次显示币：

``` shell
chia wallet coins list -f 590161281 --no-paginate
```
按要求，原始币已分成5个0.15 XCH的币。剩余的价值存放在第六个币中，扣除了1000 mojo的区块链费用：

``` shell
钱包1中总共有6个币。
6个已确认币。
0个未确认的添加。
0个未确认的移除。
已确认的币：
币ID：0x9781d2b0d70667cfe3dd330eddcdf77aa01e68b55bb015f2280197875022f1a6
        地址：xch1p2hs025nkujyqk4a6qxfxfde6uvcajqhmq2kzvacj79wf8kfvaxqw3t4zp 金额：0.150000000000  (150000000000 mojo)，在区块3065575中已确认

币ID：0x4e67664448a4a2341a678f3940676f13ccea27a8be3b742b9f7396f2e5a9cc32
        地址：xch15gt90usala3xducfee96lc4gu2su2ks56htav9gklwmmssh7t5gspuwrvh 金额：0.150000000000  (150000000000 mojo)，在区块3065575中已确认

币ID：0x9d3106af6877dde3d6fc00ffd5fde2813bf7db3e7e1fa69dd96685c8d061d81b
        地址：xch105khmcltukhupkzn4h88clkyqptsm88zyzg2vhlcpr76sd0vkggqm8vfdc 金额：0.150000000000  (150000000000 mojo)，在区块3065575中已确认

币ID：0x57ef317fd0c9b0139d1546fbb0ccd3006fa820abb239ec8539d5726621f387c0
        地址：xch15yr7nk
```


                 	

