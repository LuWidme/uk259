# ML Glossary — üK 259

A plain-English reference for the terms you meet in this course. Each entry gives a
one-line intuition first, then a little more detail. Look here whenever a word in a
notebook is unfamiliar — you do **not** need to memorise these, just know where to find them.

Terms are grouped by topic. Use `Ctrl+F` / `Cmd+F` to jump to a word.

---

## 1. Foundations & workflow

**Machine Learning (ML)** — Teaching a computer to find patterns in data instead of
programming every rule by hand. You show it examples; it learns a rule that works on new examples.

**Model** — The "thing" that has learned a pattern. You give it an input, it gives you a
prediction. Think of it as a function the computer figured out from data.

**Feature** — One input column you use to make a prediction (e.g. a passenger's age, a
house's size). Also called a *variable* or *predictor*.

**Target (label)** — The answer you want to predict (e.g. *survived yes/no*, *house price*).
In supervised learning every training example has a known target.

**Sample (instance / row / observation)** — One example in your dataset: one passenger,
one house, one customer.

**Training** — The process where the model looks at examples and adjusts itself to make
good predictions. "Fitting" means the same thing.

**Prediction (inference)** — Using a trained model to get an answer for a new, unseen input.

**Supervised learning** — Learning from labelled examples (you know the right answer for
each). Used for classification and regression.

**Unsupervised learning** — Learning from data with *no* labels; the model finds structure
on its own (e.g. clustering).

**Generalisation** — How well a model works on new data it has never seen. The whole point
of ML — a model that only works on its training data is useless.

---

## 2. Data preparation

**Preprocessing** — All the cleaning and reshaping you do to raw data before training:
handling gaps, scaling numbers, turning text into numbers.

**Missing value (NaN)** — An empty cell. `NaN` = "Not a Number". Most models can't handle
gaps, so you either remove or fill them.

**Imputation** — Filling missing values with a sensible substitute, usually the column's
mean, median, or most frequent value.

**Outlier** — A value far away from the rest (e.g. a house listed at CHF 50 million). Can
distort a model; sometimes removed, sometimes kept on purpose.

**Feature scaling** — Putting numeric features on a comparable range so that a big-numbered
feature (income) doesn't dominate a small-numbered one (age). Important for KNN, K-Means, neural nets.

**Standardisation (Z-score)** — A scaling method: rescale a column to mean 0 and standard
deviation 1. `StandardScaler` in scikit-learn.

**Normalisation (Min-Max scaling)** — A scaling method: squash a column into the range
[0, 1]. `MinMaxScaler` in scikit-learn.

**Encoding** — Turning categorical (text) values into numbers a model can use.

**Label encoding** — Map each category to an integer (red→0, green→1, blue→2). Good for
*ordered* categories; can mislead models for unordered ones.

**One-hot encoding** — Make one new 0/1 column per category. Avoids implying a false order.
`pd.get_dummies()`.

**Binning (discretisation)** — Grouping a numeric column into buckets (e.g. age → child /
adult / senior).

**Feature engineering** — Creating new, more useful features from existing ones (e.g. price
÷ area = price per square metre).

---

## 3. Core Python / data tools

**NumPy** — Python library for fast numerical work with arrays (grids of numbers). Alias `np`.

**Array (ndarray)** — NumPy's grid of numbers. Like a list, but faster and built for maths.

**Pandas** — Python library for working with tables of data. Alias `pd`.

**DataFrame** — Pandas' table: rows and named columns, like a spreadsheet in code.

**Series** — A single column of a DataFrame.

**scikit-learn (sklearn)** — The main "classic ML" library: ready-made models, scalers,
metrics, and dataset tools.

**Matplotlib / Seaborn** — Plotting libraries. Matplotlib is the engine; Seaborn is a
friendlier layer for statistical charts.

---

## 4. Visualisation

**Histogram** — A bar chart showing how often values fall into ranges; reveals a column's
distribution (where most values sit).

**Scatter plot** — Dots showing the relationship between two numeric columns; reveals trends
and clusters.

**Pair plot** — A grid of scatter plots for every pair of features at once; a fast way to
eyeball a whole dataset.

**Distribution** — The shape of how a column's values are spread (e.g. bell-shaped, skewed).

**Correlation** — How strongly two variables move together. High positive = rise together;
high negative = one rises as the other falls. Correlation is *not* proof of cause.

---

## 5. Clustering (unsupervised)

**Clustering** — Grouping samples that are similar, without any labels. The model decides
the groups itself.

**K-Means** — The most common clustering method. You pick K (number of groups); it finds K
cluster centres and assigns each point to the nearest one.

**Centroid (cluster centre)** — The "average point" at the middle of a cluster.

**Inertia** — How tightly packed the clusters are (sum of squared distances of points to
their centre). Lower = tighter clusters.

**Elbow method** — A way to choose K: plot inertia for several K values and pick the "elbow"
where adding more clusters stops helping much.

**Customer segmentation** — A typical clustering use case: grouping customers by behaviour
to treat each group differently.

---

## 6. Classification (supervised)

**Classification** — Predicting a category/label (spam vs not spam, survived vs not).

**K-Nearest Neighbors (KNN)** — Classify a new point by looking at its K closest known
points and taking the majority vote.

**Decision Tree** — A flowchart of yes/no questions that splits data step by step to reach
a prediction. Easy to read and explain.

**Support Vector Machine (SVM)** — A classifier that finds the boundary best separating
classes. (Bonus/advanced in this course.)

**Decision boundary** — The dividing line a classifier draws between classes.

**Class** — One of the categories you predict (e.g. the digit "7", or "did not survive").

---

## 7. Regression (supervised)

**Regression** — Predicting a *number* (house price, temperature) rather than a category.

**Linear regression** — Fits a straight line (or flat plane) through the data: prediction =
a sum of features each multiplied by a weight, plus an offset.

**Coefficient (weight)** — How much one feature pushes the prediction up or down. Big
positive coefficient = that feature strongly raises the prediction.

**Intercept (bias)** — The baseline prediction when all features are zero.

**Simple vs multiple regression** — Simple uses one feature; multiple uses several at once.

**Residual** — The error for one prediction: actual value minus predicted value. Residual
plots check whether a model is missing a pattern.

**Simpson's paradox** — A trend that appears in groups can reverse when the groups are
merged; a warning to look at data both ways.

---

## 8. Evaluating models

**Train/test split** — Hold back part of the data for testing so you measure performance on
examples the model never trained on. Typical split: 80% train, 20% test.

**Overfitting** — The model memorises the training data (including noise) and does badly on
new data. High training score, low test score.

**Underfitting** — The model is too simple to capture the pattern; it does badly on both
training and test data.

**Accuracy** — Fraction of predictions that are correct. Simple, but misleading when classes
are imbalanced.

**Confusion matrix** — A table of correct vs wrong predictions per class; shows *what kind*
of mistakes the model makes.

**Precision** — Of the items the model labelled positive, how many really were. ("When it
says yes, how often is it right?")

**Recall** — Of all the truly positive items, how many the model caught. ("How many of the
real cases did it find?")

**MAE (Mean Absolute Error)** — Average size of the prediction error, in the target's own
units. Lower is better.

**RMSE (Root Mean Squared Error)** — Like MAE but punishes big errors more. Lower is better.

**R² (R-squared)** — How much of the variation in the target the model explains, from 0 to 1
(higher is better). 1 = perfect, 0 = no better than guessing the average.

**p-value** — In statistics, how likely a result could be due to chance. Small (< 0.05)
usually means a feature is "statistically significant". (Bonus material.)

---

## 9. Neural networks & modern ML

**Neural network** — A model loosely inspired by the brain: layers of simple units
("neurons") that pass numbers forward and learn by adjusting connection strengths.

**Neuron (unit / node)** — One small computing element: it sums its inputs, applies an
activation, and passes the result on.

**Layer** — A row of neurons. Networks stack an input layer, one or more hidden layers, and
an output layer.

**Weight & bias** — The adjustable "knobs" the network tunes during training. More
neurons/layers = more knobs = more capacity to learn (and to overfit).

**Activation function** — A small function (e.g. ReLU) that lets a network learn non-straight
relationships.

**ReLU** — A popular activation: keeps positive values, turns negatives to zero.

**Epoch** — One full pass through the training data. Training usually takes several epochs.

**Loss function** — A number measuring how wrong the model currently is. Training tries to
make it smaller.

**Optimizer** — The method that adjusts the weights to reduce the loss (e.g. *Adam*).

**Keras / TensorFlow** — Libraries for building and training neural networks. Keras is the
friendly front-end on top of TensorFlow.

**MNIST / Fashion-MNIST** — Classic beginner datasets of small images (handwritten digits;
clothing items) used to learn image classification.

**Parameters** — All the weights and biases a model learns. A "101,770-parameter" model has
that many tunable knobs.

---

## 10. Transformers, LLMs & transfer learning

**Hugging Face** — A platform and library (`transformers`) giving easy access to thousands of
pre-trained models and datasets.

**Pipeline** — A one-line Hugging Face helper that bundles a model for a task (sentiment,
classification, text generation) so you can use it without setup.

**Pre-trained model** — A model someone else already trained on huge data; you reuse it
instead of training from scratch.

**Transfer learning** — Taking a pre-trained model and reusing its learned knowledge for your
own task. Saves time, data, and compute.

**Transformer** — The neural-network architecture behind modern language models; good at
handling sequences like text.

**Large Language Model (LLM)** — A very large transformer trained on huge amounts of text
(e.g. GPT). Predicts the next word, which lets it write, summarise, and answer.

**Next-word prediction** — The core trick of an LLM: repeatedly guessing the most likely next
word builds whole sentences.

**Zero-shot classification** — Classifying text into categories you define on the spot,
without training the model on those categories first.

**Sentiment analysis** — Deciding whether a piece of text is positive, negative, or neutral.

**Hallucination** — When a language model states something fluent but false. Always verify
LLM output against trusted sources.

---

## 11. Tools & environment

**Google Colab** — A free, browser-based notebook environment with Python and ML libraries
pre-installed. The default for this course — no local setup needed.

**Jupyter Notebook** — A document mixing runnable code cells and text cells. Colab runs
Jupyter notebooks (`.ipynb` files).

**Cell** — One block in a notebook: either code you can run or markdown text.

**pip** — Python's package installer (`pip install ...`).

**Random seed (random_state)** — A fixed number that makes "random" steps repeatable, so you
and your classmates get the same results.

---

*Missing a term? Add it here — this glossary is meant to grow with the course.*
