# FeatherYOLO

## Project Introduction

FeatherYOLO is a lightweight object-detection framework for identifying pheasant tail feathers in complex cultural imagery. It was developed as a task-specific adaptation of YOLO11n for detecting elongated, texture-rich, deformed, damaged, and partially occluded feather targets embedded in costumes, performances, online images, and other visually complex cultural scenes.

FeatherYOLO is intended as an image-based screening and detection tool for avian-derived materials. It should not be interpreted as a standalone system for directly estimating population-level conservation pressure, harvest intensity, illegal trade intensity, or population decline.

---

## Model Features

- Based on YOLO11n with task-specific modifications for pheasant tail feather detection.
- Designed for detecting elongated, texture-rich, deformed, damaged, and partially occluded feather targets.
- Suitable for pheasant tail feather detection in complex cultural imagery.
- Lightweight architecture suitable for local inference and prototype deployment.
- Custom modules include HDRAB2, V7DownSampling, and LTND (LiteTexNet Detect).

The source code for HDRAB2 and V7DownSampling is provided in:

```text
ultralytics/nn/extra_modules/block.py
```

The LTND detection head is implemented in:

```text
ultralytics/nn/extra_modules/head.py
```

Reviewers can directly inspect the architectural modifications in these files.

---

## Installation

### Environment Requirements

- Python 3.9+
- PyTorch 2.0+
- Modified Ultralytics YOLO framework with additional modules

### Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/tjwtjw666/FeatherYOLO.git
cd FeatherYOLO
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Detection

Use the trained FeatherYOLO model weights for pheasant tail feather detection:

```bash
python detect.py --weights FeatherYOLO.pt --source path/to/images --imgsz 640
```

Example:

```bash
python detect.py --weights FeatherYOLO.pt --source examples/ --imgsz 640
```

The output includes detected bounding boxes, predicted feather classes, and confidence scores.

---

### Training

Train FeatherYOLO from the architecture configuration file:

```bash
python train.py --model FeatherYOLO.yaml --data feather.v9i.yolov11/data.yaml --epochs 300 --batch 32 --imgsz 640 --optimizer SGD
```

In the reported experiments, FeatherYOLO and the main comparison models were trained from their architecture configuration files. No pretrained weights were loaded.

Main training settings:

| Setting | Value |
|---|---|
| Image size | 640 × 640 |
| Epochs | 300 |
| Batch size | 32 |
| Optimizer | SGD |
| Workers | 4 |
| Image caching | Disabled |
| close_mosaic | 0 |

If your local `train.py` uses a different argument name, please keep the same experimental settings and use the corresponding command format.

---

### Evaluation

Evaluate the trained FeatherYOLO model using the validation or test set:

```bash
python val.py --weights FeatherYOLO.pt --data feather.v9i.yolov11/data.yaml --imgsz 640
```

---

### Web Image Crawling and Recognition Example

This repository provides an example script for keyword-based web image crawling and feather recognition:

```bash
python image_crawler.py
```

**Note:** This script requires:

- A `keywords.xlsx` file with keywords in a sheet named `Keywords`
- The `openpyxl` library for Excel operations

The provided `image_crawler.py` is intended as a demonstration script for low-volume exploratory screening. Other data collection and processing scripts mentioned in the manuscript are not included in this public repository due to platform sensitivity, copyright, and compliance considerations.

---

## Dataset Information

This project uses the MF-2025 pheasant feather dataset. MF-2025 contains annotated images of four pheasant feather classes:

- `Syrmaticus reevesii`
- `Chrysolophus amherstiae`
- `Chrysolophus pictus`
- `Phasianus colchicus`

The original image set was split into training, validation, and test subsets at an approximate ratio of 7:2:1. Data augmentation was applied only to the training subset to increase training diversity. After training-set expansion, the effective experimental split contained:

| Split | Images |
|---|---:|
| Training | 2335 |
| Validation | 221 |
| Test | 106 |

Validation and test images were not augmented for model evaluation.

Due to ethical and copyright considerations related to images collected from public online platforms, the complete MF-2025 dataset is available from the corresponding author upon reasonable academic request. This repository provides the dataset structure, data configuration file, example files, and instructions for using the model.

---

## Model Files

- `FeatherYOLO.pt` - trained FeatherYOLO model weights
- `FeatherYOLO.yaml` - FeatherYOLO model configuration file

---

## Model Performance

FeatherYOLO achieved the following overall performance on MF-2025:

| Model | Precision | Recall | mAP@0.5 | Parameters (M) | GFLOPs |
|---|---:|---:|---:|---:|---:|
| FeatherYOLO | 0.766 | 0.649 | 0.692 | 1.938 | 5.7 |

Ablation results:

| Model | Precision | Recall | mAP@0.5 | Parameters (M) | GFLOPs |
|---|---:|---:|---:|---:|---:|
| YOLO11 | 0.808 | 0.608 | 0.651 | 2.582 | 6.3 |
| YOLO11-HDRAB | 0.831 | 0.597 | 0.637 | 3.221 | 8.7 |
| YOLO11-HDRAB2 | 0.773 | 0.619 | 0.675 | 2.610 | 6.6 |
| YOLO11-HDRAB2-V7DS | 0.717 | 0.615 | 0.687 | 2.260 | 6.0 |
| YOLO11-HDRAB2-V7DS-LTND (FeatherYOLO) | 0.766 | 0.649 | 0.692 | 1.938 | 5.7 |

These results indicate that FeatherYOLO achieved a favourable balance between detection performance and model compactness for pheasant tail feather detection in complex cultural imagery.

---

## Web Prototype

A web-based FeatherYOLO prototype is available at:

```text
https://manqi111-feather.hf.space/
```

The prototype supports browser-based image upload and keyword-based exploratory image recognition. It is intended for low-volume interactive screening, demonstration, and methodological reproducibility rather than high-concurrency or large-scale automated deployment.

For large-scale batch processing, repeated monitoring, or high-concurrency use, local deployment using this repository and the trained model weights is recommended.

---

## Project Structure

```text
FeatherYOLO/
├── FeatherYOLO.pt              # Trained FeatherYOLO model weights
├── FeatherYOLO.yaml            # Model configuration file
├── detect.py                   # Detection script
├── train.py                    # Training script
├── val.py                      # Evaluation script
├── image_crawler.py            # Web image crawling and recognition example script
├── requirements.txt            # Python dependencies
├── feather.v9i.yolov11/        # Dataset structure, data.yaml, and example files
│   ├── train/                  # Training data structure or example files
│   ├── val/                    # Validation data structure or example files
│   ├── test/                   # Test data structure or example files
│   └── data.yaml               # Dataset configuration file
└── ultralytics/                # Modified Ultralytics YOLO framework
    └── nn/
        └── extra_modules/
            ├── block.py        # HDRAB2 and V7DownSampling
            └── head.py         # LTND detection head
```

---

## Code and Data Availability

The source code, model configuration files, training and inference scripts, example data, and instructions for using FeatherYOLO are available in this repository.

The complete MF-2025 dataset is available from the corresponding author upon reasonable academic request, subject to ethical and copyright considerations.

The web-based FeatherYOLO prototype is available at:

```text
https://manqi111-feather.hf.space/
```

---

## Citation

If you use FeatherYOLO, please cite the associated manuscript:

```text
Tang J, Wang N, Qin X. FeatherYOLO: a novel method for detecting pheasant feathers in complex cultural imagery for avian conservation monitoring.
```

---

## License

This project is released under the MIT License.

---

## Contribution

Issues and pull requests are welcome. Suggestions for improving model robustness, documentation, and reproducibility are appreciated.

---

## Contact

For questions about the model, dataset access, or collaboration, please contact the corresponding author.

Corresponding author: Xinghu Qin  
Email: qinxh@bjfu.edu.cn

---

# FeatherYOLO 中文说明

## 项目介绍

FeatherYOLO 是一个轻量级目标检测框架，用于识别复杂文化图像中的雉类尾羽。该模型基于 YOLO11n 进行任务化改进，主要面向服饰、表演、网络图像和其他复杂文化场景中细长、纹理丰富、变形、破损或部分遮挡的尾羽目标检测。

FeatherYOLO 主要定位为鸟类衍生材料的图像筛查和检测工具，不应被解释为可直接估计种群水平保护压力、捕猎强度、非法贸易强度或种群下降的独立系统。

---

## 模型特点

- 基于 YOLO11n，并针对雉类尾羽检测进行了任务化改进。
- 适用于检测细长、纹理丰富、变形、破损和部分遮挡的尾羽目标。
- 适用于复杂文化图像中的雉类尾羽检测。
- 模型结构较轻，适合本地推理和原型系统部署。
- 自定义模块包括 HDRAB2、V7DownSampling 和 LTND（LiteTexNet Detect）。

HDRAB2 和 V7DownSampling 的源代码位于：

```text
ultralytics/nn/extra_modules/block.py
```

LTND 检测头的实现位于：

```text
ultralytics/nn/extra_modules/head.py
```

审稿人可以直接在上述文件中检查模型结构修改。

---

## 安装方法

### 环境要求

- Python 3.9+
- PyTorch 2.0+
- 修改版 Ultralytics YOLO 框架，包含额外模块

### 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/tjwtjw666/FeatherYOLO.git
cd FeatherYOLO
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

---

## 使用方法

### 检测

使用训练好的 FeatherYOLO 模型权重进行雉类尾羽检测：

```bash
python detect.py --weights FeatherYOLO.pt --source path/to/images --imgsz 640
```

示例：

```bash
python detect.py --weights FeatherYOLO.pt --source examples/ --imgsz 640
```

输出结果包括检测框、预测类别和置信度分数。

---

### 训练

从模型结构配置文件训练 FeatherYOLO：

```bash
python train.py --model FeatherYOLO.yaml --data feather.v9i.yolov11/data.yaml --epochs 300 --batch 32 --imgsz 640 --optimizer SGD
```

在论文报告的实验中，FeatherYOLO 和主要对比模型均从模型结构配置文件开始训练，未加载预训练权重。

主要训练设置如下：

| 设置 | 数值 |
|---|---|
| 图像尺寸 | 640 × 640 |
| 训练轮数 | 300 |
| 批量大小 | 32 |
| 优化器 | SGD |
| 数据加载 workers | 4 |
| 图像缓存 | 不启用 |
| close_mosaic | 0 |

如果本地 `train.py` 的参数名称不同，请保持上述实验设置，并使用对应的命令格式。

---

### 评估

使用验证集或测试集评估训练好的 FeatherYOLO 模型：

```bash
python val.py --weights FeatherYOLO.pt --data feather.v9i.yolov11/data.yaml --imgsz 640
```

---

### 网络图片爬取与识别示例

本仓库提供了一个基于关键词的网络图片爬取与尾羽识别示例脚本：

```bash
python image_crawler.py
```

**注意：** 该脚本需要：

- 一个 `keywords.xlsx` 文件，其中包含名为 `Keywords` 的工作表；
- `openpyxl` 库用于 Excel 文件操作。

`image_crawler.py` 仅作为低通量探索性筛查的演示脚本。论文中涉及的其他数据收集和处理脚本，由于平台敏感性、版权和合规性考虑，未包含在本公开仓库中。

---

## 数据集信息

本项目使用 MF-2025 雉类尾羽数据集。MF-2025 包含四类雉类尾羽图像标注：

- `Syrmaticus reevesii`
- `Chrysolophus amherstiae`
- `Chrysolophus pictus`
- `Phasianus colchicus`

原始图像集按照约 7:2:1 的比例划分为训练集、验证集和测试集。数据增强仅应用于训练集，用于增加训练样本多样性。训练集扩增后，实验中的有效数据划分如下：

| 数据集 | 图像数 |
|---|---:|
| 训练集 | 2335 |
| 验证集 | 221 |
| 测试集 | 106 |

验证集和测试集未进行数据增强，并用于模型评估。

由于部分图像来源于公开网络平台，涉及伦理和版权因素，完整 MF-2025 数据集可在合理的学术请求下向通讯作者获取。本仓库提供数据集结构、数据配置文件、示例文件和模型使用说明。

---

## 模型文件

- `FeatherYOLO.pt` - 训练好的 FeatherYOLO 模型权重
- `FeatherYOLO.yaml` - FeatherYOLO 模型配置文件

---

## 模型性能

FeatherYOLO 在 MF-2025 数据集上取得了如下总体性能：

| Model | Precision | Recall | mAP@0.5 | Parameters (M) | GFLOPs |
|---|---:|---:|---:|---:|---:|
| FeatherYOLO | 0.766 | 0.649 | 0.692 | 1.938 | 5.7 |

消融实验结果如下：

| Model | Precision | Recall | mAP@0.5 | Parameters (M) | GFLOPs |
|---|---:|---:|---:|---:|---:|
| YOLO11 | 0.808 | 0.608 | 0.651 | 2.582 | 6.3 |
| YOLO11-HDRAB | 0.831 | 0.597 | 0.637 | 3.221 | 8.7 |
| YOLO11-HDRAB2 | 0.773 | 0.619 | 0.675 | 2.610 | 6.6 |
| YOLO11-HDRAB2-V7DS | 0.717 | 0.615 | 0.687 | 2.260 | 6.0 |
| YOLO11-HDRAB2-V7DS-LTND (FeatherYOLO) | 0.766 | 0.649 | 0.692 | 1.938 | 5.7 |

上述结果表明，FeatherYOLO 在复杂文化图像中的雉类尾羽检测任务上取得了较好的检测性能与模型紧凑性平衡。

---

## 网页原型系统

FeatherYOLO 网页原型系统可通过以下地址访问：

```text
https://manqi111-feather.hf.space/
```

该原型系统支持基于浏览器的图像上传和关键词图像探索性识别。该系统主要用于低通量交互式筛查、方法演示和可重复性展示，不应被解释为高并发或大规模自动监测平台。

对于大规模批量处理、重复监测或高并发应用，建议使用本仓库和训练好的模型权重进行本地部署。

---

## 项目结构

```text
FeatherYOLO/
├── FeatherYOLO.pt              # 训练好的 FeatherYOLO 模型权重
├── FeatherYOLO.yaml            # 模型配置文件
├── detect.py                   # 检测脚本
├── train.py                    # 训练脚本
├── val.py                      # 评估脚本
├── image_crawler.py            # 网络图片爬取与识别示例脚本
├── requirements.txt            # Python 依赖
├── feather.v9i.yolov11/        # 数据集结构、data.yaml 和示例文件
│   ├── train/                  # 训练数据结构或示例文件
│   ├── val/                    # 验证数据结构或示例文件
│   ├── test/                   # 测试数据结构或示例文件
│   └── data.yaml               # 数据配置文件
└── ultralytics/                # 修改版 Ultralytics YOLO 框架
    └── nn/
        └── extra_modules/
            ├── block.py        # HDRAB2 和 V7DownSampling
            └── head.py         # LTND 检测头
```

---

## 代码和数据可用性

FeatherYOLO 的源代码、模型配置文件、训练和推理脚本、示例数据以及使用说明均可在本仓库中获取。

完整 MF-2025 数据集可在合理的学术请求下向通讯作者获取，但需遵守相关伦理和版权要求。

FeatherYOLO 网页原型系统可通过以下地址访问：

```text
https://manqi111-feather.hf.space/
```

---

## 引用

如果使用 FeatherYOLO，请引用相关论文：

```text
Tang J, Wang N, Qin X. FeatherYOLO: a novel method for detecting pheasant feathers in complex cultural imagery for avian conservation monitoring.
```

---

## 许可证

本项目基于 MIT License 开源。

---

## 贡献

欢迎提交 Issues 和 Pull Requests，以改进 FeatherYOLO 的模型鲁棒性、文档说明和可重复性。

---

## 联系方式

如有模型使用、数据集获取或合作相关问题，请联系通讯作者。

通讯作者：Xinghu Qin  
邮箱：qinxh@bjfu.edu.cn