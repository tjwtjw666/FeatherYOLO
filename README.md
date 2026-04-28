# FeatherYOLO (English Version)

## Project Introduction
FeatherYOLO is a tail feather recognition model improved based on YOLOv11, specifically designed for identifying and detecting bird tail feather features. The model has been optimized for tail feather recognition, improving accuracy and speed.

## Model Features
- Based on YOLOv11 architecture with specific optimizations for tail feather recognition
- Supports real-time tail feather detection and recognition
- High-precision recognition of tail feather features from different bird species
- Lightweight design suitable for edge device deployment
- Custom modules including HDRAB (Hierarchical Dual Residual Attention Block), V7DownSampling, and LTND (Lightweight Transformer Neck Decoder) for improved feature extraction and fusion

The source code for our proposed custom modules (HDRAB, V7DownSampling) can be found in `ultralytics/nn/extra_modules/block.py`. The LTND detection head implementation is located in `ultralytics/nn/extra_modules/head.py`. Reviewers can directly inspect the architectural modifications here.

## Installation

### Environment Requirements
- Python 3.8+
- PyTorch 2.0+
- Ultralytics YOLO (Modified version with additional modules)

### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/tjwtjw666/FeatherYOLO.git
   cd FeatherYOLO
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Detection
Use the pre-trained model for tail feather detection:

```bash
python detect.py --weights FeatherYOLO.pt --source path/to/images
```

### Training
Train the model with custom dataset:

```bash
python train.py --data feather.v9i.yolov11/data.yaml --weights yolov11n.pt --epochs 100
```

### Web Image Crawling (Example Script)
This repository provides an example script for keyword-based web image crawling and recognition:

```bash
python image_crawler.py
```

**Note:** This script requires:
- A `keywords.xlsx` file with keywords in a sheet named "Keywords"
- The `openpyxl` library for Excel operations

### Additional Scripts
Please note that other data collection and processing scripts mentioned in the paper are not included in this public repository due to platform sensitivity and compliance considerations. The provided `image_crawler.py` serves as a demonstration example.

## Dataset Information

This project uses the `feather.v9i.yolov11` dataset, which includes:
- Training, validation, and test sets
- Annotated tail feather samples
- Data configuration file `data.yaml`

## Model Files

- `FeatherYOLO.pt` - Pre-trained model weights
- `FeatherYOLO.yaml` - Model configuration file

## Evaluation

Evaluate model performance using the validation set:

```bash
python val.py --weights FeatherYOLO.pt --data feather.v9i.yolov11/data.yaml
```

## Project Structure

```
FeatherYOLO/
├── FeatherYOLO.pt          # Pre-trained model
├── FeatherYOLO.yaml        # Model configuration
├── detect.py               # Detection script
├── train.py                # Training script
├── val.py                  # Validation script
├── image_crawler.py        # Web image crawling example script
├── feather.v9i.yolov11/    # Dataset
│   ├── train/              # Training data
│   ├── val/                # Validation data
│   ├── test/               # Test data
│   └── data.yaml           # Data configuration
└── ultralytics/            # Modified Ultralytics YOLO library with additional modules
```

## License

This project is open source under the MIT License.

## Contribution

Welcome to submit Issues and Pull Requests to improve the FeatherYOLO model.

---

# FeatherYOLO (中文版本)

## 项目介绍
FeatherYOLO是一个基于YOLOv11改进的尾羽识别模型，专门用于识别和检测鸟类尾羽特征。该模型在YOLO基础上进行了针对性优化，提高了尾羽识别的准确率和速度。

## 模型特点
- 基于YOLOv11架构，进行了尾羽识别的特定优化
- 支持实时尾羽检测和识别
- 高精度识别不同种类鸟类的尾羽特征
- 轻量级设计，适用于边缘设备部署
- 自定义模块包括HDRAB（层次双残差注意力模块）、V7DownSampling和LTND（轻量级Transformer Neck解码器），用于改进特征提取和融合

我们提出的自定义模块（HDRAB、V7DownSampling）的源代码位于 `ultralytics/nn/extra_modules/block.py`。LTND检测头实现位于 `ultralytics/nn/extra_modules/head.py`。审稿人可以直接在此检查架构修改。

## 安装方法

### 环境要求
- Python 3.8+
- PyTorch 2.0+
- Ultralytics YOLO（修改版本，包含额外模块）

### 安装步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/tjwtjw666/FeatherYOLO.git
   cd FeatherYOLO
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 检测
使用预训练模型进行尾羽检测：

```bash
python detect.py --weights FeatherYOLO.pt --source path/to/images
```

### 训练
使用自定义数据集训练模型：

```bash
python train.py --data feather.v9i.yolov11/data.yaml --weights yolov11n.pt --epochs 100
```

### 网络图片爬取（示例脚本）
本仓库提供了一个基于关键词的网络图片爬取和识别示例脚本：

```bash
python image_crawler.py
```

**注意：** 此脚本需要：
- 一个 `keywords.xlsx` 文件，包含名为"Keywords"的工作表
- `openpyxl` 库用于Excel操作

### 其他脚本说明
请注意，论文中提到的其他数据收集和处理脚本由于平台敏感性和合规性考虑，未包含在本公开仓库中。提供的 `image_crawler.py` 仅作为演示示例。

## 数据集信息

本项目使用了 `feather.v9i.yolov11` 数据集，包含：
- 训练集、验证集和测试集
- 标注好的尾羽样本
- 数据配置文件 `data.yaml`

## 模型文件

- `FeatherYOLO.pt` - 预训练模型权重
- `FeatherYOLO.yaml` - 模型配置文件

## 评估

使用验证集评估模型性能：

```bash
python val.py --weights FeatherYOLO.pt --data feather.v9i.yolov11/data.yaml
```

## 项目结构

```
FeatherYOLO/
├── FeatherYOLO.pt          # 预训练模型
├── FeatherYOLO.yaml        # 模型配置
├── detect.py               # 检测脚本
├── train.py                # 训练脚本
├── val.py                  # 验证脚本
├── image_crawler.py        # 网络图片爬取示例脚本
├── feather.v9i.yolov11/    # 数据集
│   ├── train/              # 训练数据
│   ├── val/                # 验证数据
│   ├── test/               # 测试数据
│   └── data.yaml           # 数据配置
└── ultralytics/            # 修改版的Ultralytics YOLO库，包含额外模块
```

## 许可证

本项目基于MIT许可证开源。

## 贡献

欢迎提交Issue和Pull Request来改进FeatherYOLO模型。
