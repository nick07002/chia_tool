# Chia Inscription Minting Tool

**Disclaimer: This tool is for minting Chia inscriptions and should be used at your own risk. Please exercise caution when using it.**

## Prerequisites

Before you can use this tool, make sure you have the following prerequisites installed on your system:

- **Python**: Ensure that Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- **Pip**: Pip is the package manager for Python. It should be included with your Python installation. You can check if Pip is installed by running `pip --version` in your terminal.

## Usage

1. Clone this repository to your local machine.

2. Open the `mojo.py` file in the project directory.

3. Replace the Chia address on **line 21** with your own Chia address.

4. Run the tool using the following command in your terminal:

   ```bash
   python3 mojo.py


# Chia Inscription Minting Tool

**免责声明：此工具用于铸造Chia铭文，使用时需自担风险。在使用时请谨慎操作。**

## 先决条件

在使用此工具之前，请确保您的系统上已安装以下先决条件：
此工具只在Linux测试过，mac应该可以直接用。windows并没有测试。

- **Python**：确保您的计算机上已安装Python。您可以从[python.org](https://www.python.org/downloads/)下载它。
- **Chia** 本地需要先安装chia: https://www.chia.net/downloads/
- **Pip**：Pip是Python的包管理器。它应该随Python一起安装。您可以在终端中运行`pip --version`来检查是否安装了Pip。

## 使用方法

1. 将此存储库克隆到您的本地计算机。

2. 在项目目录中打开`mojo.py`文件。

3. 在**第21行**上用您自己的Chia地址替换Chia地址。

4. 读取钱包指纹

   ```bash
   
      $ chia wallet show
         Active Wallet Key (*):
            -Fingerprint:           1999988888
            -Label:                 LFG Bram
            -Sync Status:           Synced

         Wallet Keys:
         1)    4149998888   LFG Chia
         2)  * 1999988888   LFG Bram
         Choose a wallet key [1-2] ('q' to quit, or Enter to use 1999988888):
   
5. 使用以下命令在终端中运行工具：
   ```bash
   python3 mojo.py  --finger 1999988888



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
