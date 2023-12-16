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

   ‘’‘

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




   
