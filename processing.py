import numpy as np
import pandas as pd


class DataProcessing:
    def __init__(self, split, feature_split):
        split = split
        feature_split = feature_split
        # train = pd.read_csv("train_data.csv", index_col=0)
        # print(train.tail())
        test = pd.read_csv("preprocessing/test_data.csv", index_col=0)
        # print(test.tail())
        test_stock = pd.read_csv(
            "preprocessing/test_stock.csv", index_col=0)
        # auto_train = pd.read_csv("features/autoencoded_corrected_data.csv", index_col=0)
        auto_train = pd.read_csv(
            "features/autoencoded_data.csv", index_col=0)
        # auto_train.drop([0, 14, 16], axis=1, inplace=True)
        # auto_train.to_csv("autoencoded_corrected_data.csv", index=None)

    def make_train_data(self):
        train_data = np.array(auto_train)[int(feature_split * len(auto_train)) + 1:
                                          int((1 - feature_split) * split * len(auto_train))]
        train_data = pd.DataFrame(train_data, index=None)
        train_data.to_csv("features/autoencoded_train_data.csv")

    def make_test_data(self):
        test_data = np.array(auto_train)[int((1 - feature_split) * split * len(auto_train)
                                             + feature_split * len(auto_train) + 1):]
        test_data = pd.DataFrame(test_data, index=None)
        test_data.to_csv("features/autoencoded_test_data.csv")

    def make_train_y(self):
        train_y = np.array(test)[int(feature_split * len(auto_train)) + 1:
                                 int((1 - feature_split) * split * len(auto_train))]
        train_y = pd.DataFrame(train_y, index=None)
        train_y.to_csv("features/autoencoded_train_y.csv")

    def make_test_y(self):
        test_y = np.array(test)[int((1 - feature_split) * split * len(auto_train)
                                    + feature_split * len(auto_train)) + 1:]
        test_y = pd.DataFrame(test_y)
        test_y.to_csv("features/autoencoded_test_y.csv")

    def make_stock_train_y(self):
        test_y = np.array(test_stock)[int(feature_split * len(auto_train)) + 1:
                                      int((1 - feature_split) * split * len(auto_train))]
        test_y = pd.DataFrame(test_y, index=None)
        test_y.to_csv("features/nn_stock_train_y.csv")

    def make_stock_test_y(self):
        test_y = np.array(test_stock)[int(
            (1 - feature_split) * split * len(auto_train)) + 1:]
        test_y = pd.DataFrame(test_y, index=None)
        test_y.to_csv("features/nn_stock_test_y.csv")


if __name__ == "__main__":
    process = DataProcessing(0.8, 0.25)
    process.make_test_data()
    process.make_train_data()
    process.make_train_y()
    process.make_test_y()