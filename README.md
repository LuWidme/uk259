# üK 259 — Introduction to Machine Learning

A hands-on 5-day course covering machine learning fundamentals — from working with data to neural networks and modern language models. Designed for programming beginners with little math background: **intuition before formulas**.

## How to Use This Course (Google Colab — no installation needed)

All notebooks run in [Google Colab](https://colab.research.google.com), free of charge, directly in your browser. You only need a Google account.

1. Click the **"Open in Colab"** badge at the top of any notebook (links below).
2. Run the **setup cell** at the top of the notebook first — it installs the required packages and downloads the course datasets automatically.
3. Work through the notebook top to bottom. Exercise placeholders look like `= ?` or `# TODO` — fill them in yourself before checking the solutions.

> **Tip:** Save a copy to your own Google Drive (*File → Save a copy in Drive*) so your work persists.

## Course Structure

| Day | Topic | Notebooks |
|-----|-------|-----------|
| 1 | Onboarding & Data | [01 Colab Intro & Setup Check](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/01_Colab_Intro_and_Setup_Check.ipynb) · [02 NumPy & Pandas](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/02_NumPy_and_Pandas.ipynb) · [03 Data Visualization](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/03_Data_Visualization.ipynb) |
| 2 | Preparing Data & First ML | [04 Data Preprocessing](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/04_Data_Preprocessing.ipynb) · [05 Clustering with K-Means](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/05_Clustering_KMeans.ipynb) |
| 3 | Supervised Learning | [06 Classification](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/06_Classification.ipynb) · [07 Regression](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/07_Regression.ipynb) |
| 4 | Neural Networks & Modern ML | [08 Neural Networks](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/08_Neural_Networks.ipynb) · [09 HuggingFace Transformers](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/09_HuggingFace_Transformers.ipynb) |
| 5 | Project | Guided project with curated datasets *(coming with the rework — see project template)* |

### Bonus Material (for fast learners)

Optional, more advanced notebooks in `demos/advanced/`:

| Notebook | Topic |
|----------|-------|
| [Bonus: Advanced Seaborn & Marathon Case Study](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/advanced/Bonus_Seaborn_Advanced.ipynb) | Violin plots, KDE, faceting — plus a 40k-runner case study |
| [Bonus: Support Vector Machines (SVM)](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/advanced/06_5_Support_Vector_Machines.ipynb) | A third classification algorithm — maximum-margin boundaries and kernels |
| [Bonus: PCA — Dimensionality Reduction](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/advanced/Bonus_PCA_Dimensionality_Reduction.ipynb) | Compressing data for visualization |
| [Bonus: PCA from Scratch](https://colab.research.google.com/github/LuWidme/uk259/blob/rework/demos/advanced/Bonus_PCA_from_Scratch.ipynb) | The math behind PCA, step by step |

## Repository Layout

```
uk259/
├── demos/              # Course notebooks (01–09), work through these in order
│   └── advanced/       # Optional bonus notebooks
├── solutions/          # Solutions for the exercises (try first, then peek!)
│   └── advanced/       # Solutions for the bonus notebooks
├── datasets/           # Course datasets (downloaded automatically in Colab)
└── img/                # Images used in the notebooks
```

## Solutions

Every exercise notebook has a matching solutions notebook in `solutions/`. **Try the exercises yourself first** — you learn far more from struggling for 15 minutes than from reading the answer. See [solutions/README.md](solutions/README.md) for guidelines.

## Prerequisites

- Basic programming knowledge (variables, loops, functions — any language)
- No prior machine learning experience required
- No advanced math required — concepts are introduced visually and intuitively

---

## Appendix: Local Setup (optional)

You only need this if you prefer working locally instead of Colab.

**Option A — Conda:**

```bash
git clone https://github.com/LuWidme/uk259
cd uk259
conda env create -f environment.yml
conda activate uk259
jupyter notebook
```

**Option B — pip:**

```bash
git clone https://github.com/LuWidme/uk259
cd uk259
pip install -r requirements.txt
jupyter notebook
```

Note: notebook 08 additionally needs TensorFlow, notebook 09 needs `transformers` and `datasets`. The setup cell in each notebook installs everything it needs.
