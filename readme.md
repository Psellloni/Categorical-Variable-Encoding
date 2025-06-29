# Regression Model Implementation with Advanced Encoding Techniques

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Sklearn Version](https://img.shields.io/badge/scikit--learn-1.4.2-red)

This repository contains a Python implementation of regression models with categorical encoding techniques, based on concepts from academic research in machine learning and feature engineering.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Results](#results)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## Overview
This project implements and compares various regression techniques (Lasso, Ridge, ElasticNet, Linear Regression) combined with different categorical encoding approaches. The implementation demonstrates how different encoding strategies affect model performance on datasets with categorical features.

Key components:
- Multiple regression model implementations
- Comparison of encoding techniques (Ordinal, Target, etc.)
- Performance evaluation using MAE (Mean Absolute Error)
- Visualization of results

## Features
- **Regression Models**:
  - Linear Regression
  - L1 Regularization (Lasso)
  - L2 Regularization (Ridge)
  - Elastic Net (L1 + L2 regularization)
  
- **Encoding Techniques**:
  - One-hot encoding
  - Ordinal encoding 
  - Sum encoding
  - Helmet encoding
  - Polynomial encoding
  - Backward differrence encoding
  - Dinary encoding
  
- **Evaluation Metrics**:
  - Mean Absolute Error (MAE)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Psellloni/Categorical-Variable-Encoding.git
cd Categorical-Variable-Encoding
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Requirements:
```txt
pandas==2.2.2
matplotlib==3.8.4
scikit-learn==1.4.2
category-encoders==2.6.3
```

## Results
Example output showing model performance comparison:

| Model               | Encoder     | MAE     |
|---------------------|-------------|---------|
| Linear Regression   | Sum         | 636.61  |
| Ridge Regression    | Sum         | 398.65  |
| Lasso Regression    | Sum         | 435.71  |
| ElasticNet          | Sum         | 400.73  |

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

Please ensure your code follows PEP8 guidelines and includes tests where appropriate.

## Citation
If you use this implementation in academic work, please cite both the original article and this repository:

```bibtex
@misc{regression_encoding_2025,
  author = {Lev Ushkov},
  title = {Regression Model Implementation with Advanced Encoding Techniques},
  year = {2025},
  howpublished = {\url{https://github.com/Psellloni/Categorical-Variable-Encoding.git}}
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*This implementation is based on concepts from academic research in machine learning. For theoretical foundations, please refer to the original publication.*