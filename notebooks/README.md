# Doppler Analysis Notebooks

This directory contains Jupyter notebooks for analyzing Doppler radar data.

## Setup

1. Install required dependencies:
```bash
pip install -r ../requirements.txt
```

2. Launch Jupyter:
```bash
jupyter notebook
```

3. Open `doppler_analysis.ipynb`

## Notebooks

### doppler_analysis.ipynb

Comprehensive analysis of Doppler data for water flow detection. This notebook includes:

- **Data Loading & Exploration**: Parse and visualize the CSV data structure
- **Signal Processing**: Time domain analysis, FFT, filtering, and preprocessing
- **Feature Engineering**: Extract statistical and spectral features
- **Machine Learning**: Compare different ML approaches (Random Forest, Neural Networks)
- **Visualization**: Create comprehensive visualizations of results
- **Conclusions**: Provide recommendations for the best path forward

## Data

The notebook analyzes `doppler_data_20251031_122655.csv` which contains:
- First row: Flow rate labels (GPM)
- Subsequent rows: Time-series Doppler measurements

## Output

The notebook generates:
- Multiple visualizations of signal characteristics
- Feature correlation analysis
- ML model performance metrics
- Feature importance rankings
- Saved results in `analysis_results/` directory

## Requirements

See `../requirements.txt` for the complete list of dependencies.
