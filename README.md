# üK 259 Machine Learning

A comprehensive 5-day course covering fundamental machine learning concepts from data analysis to neural networks.

## Course Overview

- **Day 1:** Python fundamentals (NumPy, Pandas)
- **Day 2:** Unsupervised ML (Clustering, Dimensionality Reduction)
- **Day 3:** Supervised ML (Classification, Regression)
- **Day 4:** Neural Networks (TensorFlow/Keras)
- **Day 5:** Project work with real datasets

## Prerequisites

- Basic programming knowledge
- Understanding of high school mathematics
- No prior machine learning experience required

---

## Setup Instructions

### Option 1: Using Conda (Recommended for Beginners)

**Step 1:** Install Miniconda (lighter than Anaconda)
- Download from: https://docs.conda.io/en/latest/miniconda.html
- Follow the installer instructions
- **No special path requirements needed**

**Step 2:** Clone this repository
```bash
git clone https://github.com/LuWidme/uk259
cd uk259
```

**Step 3:** Create the environment
```bash
conda env create -f environment.yml
```

**Step 4:** Activate the environment
```bash
conda activate uk259
```

**Step 5:** Verify installation (run the verification notebook)
```bash
jupyter notebook demos/01_setup_verification.ipynb
```

### Option 2: Using pip + venv (Alternative Method)

**Step 1:** Clone the repository
```bash
git clone https://github.com/LuWidme/uk259
cd uk259
```

**Step 2:** Create virtual environment
```bash
# Windows
python -m venv uk259_env
uk259_env\Scripts\activate

# macOS/Linux
python3 -m venv uk259_env
source uk259_env/bin/activate
```

**Step 3:** Install dependencies
```bash
pip install -r requirements.txt
```

**Note:** You may need to install graphviz separately:
- **Windows:** `choco install graphviz` (requires Chocolatey)
- **macOS:** `brew install graphviz`
- **Linux:** `sudo apt-get install graphviz`

**Step 4:** Verify installation
```bash
jupyter notebook demos/01_setup_verification.ipynb
```

### Option 3: Using Docker (Advanced)

**Step 1:** Create a Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
```

**Step 2:** Build and run
```bash
docker build -t uk259-ml .
docker run -p 8888:8888 -v ${PWD}:/workspace uk259-ml
```

---

## Getting Started

### Launch Jupyter

**Option A: JupyterLab (Recommended)**
```bash
jupyter-lab
```

**Option B: Classic Notebook**
```bash
jupyter notebook
```

**Option C: PyCharm**
1. Open PyCharm and select "Open" from the welcome screen
2. Navigate to the `uk259` folder and open it
3. PyCharm should automatically detect the conda environment
4. If not, go to: **File → Settings → Project → Python Interpreter**
5. Click the gear icon → **Add Interpreter → Conda Environment**
6. Select **Existing environment** and choose `uk259`
7. Open any `.ipynb` file - PyCharm has built-in Jupyter notebook support

**Tip:** PyCharm Professional has better Jupyter support. Community Edition works but with limited features.

### Start with the Introduction

Open and run: `demos/00_course_introduction.ipynb`

This notebook covers the fundamentals of NumPy and Pandas that you'll need for the rest of the course.

---

## Troubleshooting

### Common Issues

**Issue:** `conda: command not found`
- **Solution:** Restart your terminal after installing Miniconda, or add conda to PATH

**Issue:** `No module named 'tensorflow'`
- **Solution:** Ensure you've activated the environment: `conda activate uk259`

**Issue:** TensorFlow GPU not working
- **Solution:** This course uses CPU version. For GPU, see [TensorFlow GPU installation](https://www.tensorflow.org/install/gpu)

**Issue:** Kernel not showing in Jupyter/PyCharm
- **Solution:** Run `python -m ipykernel install --user --name uk259 --display-name "Python (uk259)"`
- **In PyCharm:** Go to Settings → Project → Python Interpreter and select the uk259 conda environment

**Issue:** ImportError with graphviz
- **Solution:** Install system graphviz package (see Option 2, Step 3 above)

### Still Having Problems?

1. Check that Python version is 3.11+: `python --version`
2. Verify packages installed: `pip list` or `conda list`
3. Run the verification notebook: `demos/00_setup_verification.ipynb`
4. Check [Issues](https://github.com/LuWidme/uk259/issues) for similar problems

---

## Course Structure

```
uk259/
├── demos/              # Instructional notebooks
│   ├── 00_setup_verification.ipynb
│   ├── 00_course_introduction.ipynb  # START HERE
│   ├── 01_NumPyIntro.ipynb
│   ├── 02_PandasIntro.ipynb
│   ├── 03_Data_Preprocessing.ipynb
│   ├── 04_Clustering_with_KMeans.ipynb
│   ├── 05_SupervisedML_Classification.ipynb
│   ├── 05_SupervisedML_LinearRegression.ipynb
│   ├── 06_NeuralNetworks.ipynb
│   └── ...
├── solutions/          # Exercise solutions
│   └── 00_course_introduction_solutions.ipynb
├── datasets/           # Sample datasets
├── img/                # Images for notebooks
├── environment.yml     # Conda environment
├── requirements.txt    # Pip requirements
└── README.md          # This file
```

---

## Working with Exercises

Many notebooks include hands-on exercises to practice your skills. Here's how to approach them:

1. **Try the exercises yourself first** - The best way to learn is by doing
2. **Exercises use placeholder syntax** - You'll see `variable = ?` which will cause errors until you write the correct code
3. **Read the hints** - Each task includes hints to guide you
4. **Check solutions when needed** - Solutions are in the `solutions/` folder
5. **Understand, don't copy** - Solutions include explanations to help you learn

**Important:** Solutions are learning tools, not answer keys. Try to solve exercises independently before checking solutions!

---

## Additional Resources

- **ML Glossary:** See `ML_GLOSSARY.md` for term definitions
- **Course Feedback:** See `COURSE_FEEDBACK.md` for detailed analysis
- **Datasets:** See `Showcase Datasets.ipynb` for available datasets
- **Exercise Solutions:** Check the `solutions/` folder after attempting exercises

### External Learning Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [HuggingFace Course](https://huggingface.co/learn)
- [3Blue1Brown Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk)

---

## Contributing

Found an issue or want to improve the course? Please open an issue or submit a pull request!

## License

This course material is provided for educational purposes.
