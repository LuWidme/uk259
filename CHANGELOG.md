# Changelog — üK 259 Machine Learning Rework

All notable changes to the course material, organized by work package (WP). The
rework restructured the course around Google Colab (zero local install), an
English-only, intuition-first curriculum for programming beginners with little
math, and a guided Day‑5 project.

## WP8 — QA & Finalization (2026-06-16)

- **Full structural validation** of all 28 notebooks: every notebook is
  `nbformat`-valid; no unintended empty `#` headings; every code cell AST-parses
  except the deliberate exercise placeholders (`= ?`, `?`, `# TODO`) and `%pip`
  setup magic.
- **Offline end-to-end execution** of the 9 self-contained solution notebooks
  (sklearn / pandas / numpy / matplotlib + bundled CSVs) — all pass:

  | Solution notebook | Result | Runtime |
  |---|---|---|
  | 01 Colab Intro & Setup Check | ✅ pass | 1.4 s |
  | 02 NumPy & Pandas | ✅ pass | 5.3 s |
  | 04 Data Preprocessing | ✅ pass | 4.8 s |
  | 05 Clustering K-Means | ✅ pass | 5.9 s |
  | 06 Classification | ✅ pass | 5.4 s |
  | 10 Project Example (Breast Cancer) | ✅ pass | 6.3 s |
  | advanced/06_5 Support Vector Machines | ✅ pass | 3.5 s |
  | advanced/Bonus PCA — Dimensionality Reduction | ✅ pass | 7.0 s |
  | advanced/Bonus PCA from Scratch | ✅ pass | 7.2 s |

  Deferred to a live Colab session (require network/runtime the QA sandbox
  blocks): **03** and **07** (seaborn `load_dataset` for penguins/diamonds),
  **08** (TensorFlow / Fashion-MNIST), **09** (HuggingFace model downloads).
  All four are `nbformat`-valid and AST-clean.
- **Consistency fixes (branch references):**
  - `04_Data_Preprocessing.ipynb`: dataset load no longer fetches the `main`
    branch over the network — it now reads the locally-downloaded
    `../datasets/melb_data.csv`, matching every other notebook.
  - `07_Regression.ipynb`: header image URL repointed from `blob/main/` to
    `blob/rework/`.
- **Links & images checked:** all relative README links resolve; all referenced
  `img/` files exist; all Colab badges point to `LuWidme/uk259@rework` with the
  correct per-notebook path.
- **Docs finalized:** README repository layout updated to `01–10`; added a
  Glossary section linking `ML_GLOSSARY.md`.

## WP7 — Solutions & Glossary (2026-06-16)

- New `ML_GLOSSARY.md` (English terms, plain-English intuition first, 11 topic
  groups covering every term in the notebooks).
- Time-budget line (⏱️ + day + hint) added to the first markdown cell of all 10
  demo notebooks.
- All solution notebooks aligned 1:1 to the new structure/numbering and
  regenerated; new solutions for 01, 03, and the SVM advanced notebook;
  `solutions/README.md` updated; Breast Cancer project reference solution added.

## WP6 — Day 5 Project Package (2026-06-16)

- New `demos/10_Project_Template.ipynb` (full-day guided project, 6 milestones,
  embedded rubric, 5-minute presentation guideline, day schedule, instructor
  notes).
- Curated dataset catalog (Titanic, Palmer Penguins, Breast Cancer Wisconsin,
  Diamonds, California Housing) covering classification, regression and
  clustering — all zero-dependency in Colab.
- New `demos/PROJECT_RUBRIC.md` (printable rubric + presentation checklist).

## WP5 — Day 4: Neural Networks & Modern ML (2026-06-16)

- `08`: added a TensorFlow Playground hands-on intro; reframed parameter math as
  intuition ("tunable knobs") rather than hand calculation; kept Fashion-MNIST.
- `09`: new "GPT & Co. — LLMs in Context" part; verified contiguous Part 1–7
  numbering; new solutions notebook for all three exercises (CPU-friendly models).

## WP4 — Day 3: Supervised Learning (2026-06-16)

- `06`: SVM moved to `advanced/06_5_Support_Vector_Machines.ipynb`; new
  "Evaluating a Classifier" part (train/test split, accuracy, confusion matrix,
  precision/recall intuition); model comparison reduced to KNN + Decision Tree;
  Titanic exercise as the through-line.
- `07`: completed Simpson's-paradox demo, added a multiple-regression part with
  scikit-learn, moved statsmodels/OLS to an optional bonus.

## WP3 — Day 2: Preprocessing & Clustering (2026-06-16)

- `04`: trimmed from 11 to 6 core exercises (missing values, scaling, encoding);
  remaining topics moved to a bonus section.
- `05`: rebuilt K-Means with the sklearn path first, elbow method, customer
  segmentation as the main exercise; from-scratch implementation moved to bonus.
- PCA kept out of the core program (advanced/bonus only) — no eigenvector /
  covariance vocabulary in the core.

## WP2 — Day 1: Onboarding & Data (2026-06-12)

- `01` rebuilt as a Colab intro (run cells, copy to Drive, setup check, Python
  warm-up).
- `02` trimmed from 12 to 8 core tasks + bonus section, all tasks with hints.
- `03` new lean visualization notebook (histogram / scatter / pairplot); the full
  Seaborn chapter moved to `advanced/Bonus_Seaborn_Advanced.ipynb`.

## WP1 — Repo Hygiene & Colab Foundation (2026-06-12)

- New numbering (PCA → advanced/, Seaborn viz → core 03); notebook JSON
  normalized (nbformat 4.5); Open-in-Colab badges + setup cells (pip install &
  dataset download via `raw.githubusercontent.com`, `rework` branch) added to all
  notebooks; README rewritten (English, Colab-first, local setup as an appendix).
