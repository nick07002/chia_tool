# Chia Inscription Minting Tool

**Disclaimer: This tool is for minting Chia inscriptions and should be used at your own risk. Please exercise caution when using it.**

## Prerequisites

Before you can use this tool, make sure you have the following prerequisites installed on your system:

- **Python**: Ensure that Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- **Pip**: Pip is the package manager for Python. It should be included with your Python installation. You can check if Pip is installed by running `pip --version` in your terminal.

## Usage

1. Clone this repository to your local machine.

2. Open the `run.py` file in the project directory.

3. Replace the Chia address on **line 21** with your own Chia address.

4. Run the tool using the following command in your terminal:

   ```bash
   python3 run.py --tick <coin_name> --iter <number_of_iterations> --fee <transaction_fee>

   for example:

   python3 run.py --tick bram --iter 2 --fee 0.0001


# Chia Inscription Minting Tool

**免责声明：此工具用于铸造Chia铭文，使用时需自担风险。在使用时请谨慎操作。**

## 先决条件

在使用此工具之前，请确保您的系统上已安装以下先决条件：

- **Python**：确保您的计算机上已安装Python。您可以从[python.org](https://www.python.org/downloads/)下载它。

- **Pip**：Pip是Python的包管理器。它应该随Python一起安装。您可以在终端中运行`pip --version`来检查是否安装了Pip。

## 使用方法

1. 将此存储库克隆到您的本地计算机。

2. 在项目目录中打开`run.py`文件。

3. 在**第21行**上用您自己的Chia地址替换Chia地址。

4. 使用以下命令在终端中运行工具：
   注意：！！！ 你最好先测试 循环1次或2次，然后检查你的钱包无误在加大循环次数！！！
   另：python3 或者 python都可以运行
   ```bash
   python3 run.py --tick <coin_name> --iter <number_of_iterations> --fee <transaction_fee>

   例如：

   python3 run.py --tick bram --iter 2 --fee 0.0001


## 备注
1. 查询气费网站 https://dashboard.chia.net/d/46EAA05E/mempool-transactions-and-fees?orgId=1 右下角
2. 查询铭文列表： https://unimojo.io/#/xchs
   
