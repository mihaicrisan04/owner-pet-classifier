# Real-Time Owner and Pet Classification System

A privacy-focused AI system that uses webcam input to classify individuals as "Owner," "Owner's Pet," "Another Person," or "Nobody" in real-time.

## Overview

This project implements a real-time classification system that:
- Identifies the owner and their specific pet using computer vision
- Processes all data locally to ensure privacy
- Requires explicit consent before processing
- Provides clear feedback about classifications
- Implements robust privacy measures

## Features

- Real-time webcam processing
- Local processing (no data leaves your device)
- Explicit consent management
- Privacy-preserving design
- Clear user interface
- Easy enrollment process
- GPU acceleration with CUDA support

## System Requirements

### Hardware Requirements
- NVIDIA GPU with CUDA support (recommended for training)
- Webcam
- Minimum 8GB RAM
- 2GB free disk space

### Software Requirements
- Python 3.9+
- CUDA Toolkit 11.8 or later (for GPU acceleration)
- cuDNN (for GPU acceleration)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/owner-pet-classifier.git
cd owner-pet-classifier
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies: (this project is using CUDA)
```bash
pip install -r requirements.txt
```

### CUDA Installation (Optional but Recommended)
If you have an NVIDIA GPU and want to use CUDA acceleration:

1. Install CUDA Toolkit from NVIDIA's website
2. Install cuDNN
3. Verify CUDA installation:
```bash
nvidia-smi
```

### Running Without CUDA
If you don't have an NVIDIA GPU or prefer not to use CUDA:

1. Install PyTorch CPU version:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

2. Note that training and inference will be significantly slower without CUDA
3. For real-time processing, consider reducing the frame rate or processing resolution

## Usage

1. Run the application:
```bash
python main.py
```

2. Follow the on-screen instructions to:
   - Review and accept the privacy policy
   - Enroll yourself and your pet
   - Start real-time classification

## Project Structure

```
owner-pet-classifier/
├── README.md
├── PLAN.md
├── requirements.txt
├── main.py
├── config/
│   └── settings.py
├── data/
│   ├── owner_enrollment/
│   ├── pet_enrollment/
│   └── test_data/
├── models/
│   └── __init__.py
├── utils/
│   └── __init__.py
├── gui/
│   └── __init__.py
└── ethical_guidelines.md
```

## Ethical Considerations

This project prioritizes:
- User privacy and data security
- Explicit consent
- Transparency in operations
- Local data processing
- Clear data retention policies

For detailed ethical guidelines, see [ethical_guidelines.md](ethical_guidelines.md).

## Development

For development setup and contribution guidelines, see [PLAN.md](PLAN.md).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
