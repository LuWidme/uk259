import matplotlib.pyplot as plt
import pandas as pd

from sklearn import tree
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #
    # df = pd.read_csv("melb_data.csv")
    # X = df[["Rooms", "Price", "Landsize"]]
    # X_train = X.iloc[2:, :]
    # X_test = X.iloc[:2, :]
    # y = df["Bathroom"].iloc[2:, ]
    #
    # model = tree.DecisionTreeClassifier()
    #
    # model.fit(X_train, y)


    from matplotlib import pyplot as plt
    from sklearn import datasets
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree
    import seaborn as sns
    # Prepare the data data
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    # Fit the classifier with default hyper-parameters
    clf = DecisionTreeClassifier(random_state=1234)
    model = clf.fit(X, y)

    iris=sns.load_dataset("iris")
    sns.pairplot(iris, hue="Species")

    # fig = plt.figure(figsize=(25, 20))
    # _ = tree.plot_tree(model,
    #                    # feature_names=X_train,
    #                    # class_names=X_train.target_names,
    #                    filled=True)    # graph.render("model")
    # fig.savefig("decistion_tree.png")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
