# preprocessing.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pywt


class PreProcessing:
    def __init__(self, split, feature_split, stock_data=pd.read_csv("stock_data.csv")):
        self.split = split
        self.feature_split = feature_split
        self.stock_data = stock_data

    # wavelet transform and create autoencoder data
    def make_wavelet_train(self):
        train_data = []
        test_data = []
        log_train_data = []
        for i in range((len(self.stock_data) // 10) * 10 - 11):
            train = []
            log_ret = []
            for j in range(1, 6):
                x = np.array(self.stock_data.iloc[i : i + 11, j])
                (ca, cd) = pywt.dwt(x, "haar")
                cat = pywt.threshold(ca, np.std(ca), mode="soft")
                cdt = pywt.threshold(cd, np.std(cd), mode="soft")
                tx = pywt.idwt(cat, cdt, "haar")
                log = np.diff(np.log(tx)) * 100
                macd = np.mean(x[5:]) - np.mean(x)
                sd = np.std(x)
                log_ret = np.append(log_ret, log)
                x_tech = np.append(macd * 10, sd)
                train = np.append(train, x_tech)
            log_train_data.append(log_ret)

        log_train = pd.DataFrame(log_train_data, index=None)
        log_train.to_csv("preprocessing/log_train.csv")

        rbm_train = pd.DataFrame(
            log_train_data[
                0 : int(self.split * self.feature_split * len(log_train_data))
            ],
            index=None,
        )
        rbm_train.to_csv("preprocessing/rbm_train.csv")
        rbm_test = pd.DataFrame(
            log_train_data[
                int(self.split * self.feature_split * len(log_train_data))
                + 1 : int(self.feature_split * len(log_train_data))
            ]
        )
        rbm_test.to_csv("preprocessing/rbm_test.csv")
        for i in range((len(self.stock_data) // 10) * 10 - 11):
            y = 100 * np.log(
                self.stock_data.iloc[i + 11, 5] / self.stock_data.iloc[i + 10, 5]
            )
            test_data.append(y)
        test = pd.DataFrame(test_data)
        test.to_csv("preprocessing/test_data.csv")

    def make_test_data(self):
        test_stock = []

        for i in range((len(self.stock_data) // 10) * 10 - 11):
            l = self.stock_data.iloc[i + 11, 5]
            test_stock.append(l)
            test = pd.DataFrame(test_stock)
            test.to_csv("preprocessing/test_stock.csv")

        stock_test_data = np.array(test_stock)[
            int(
                self.feature_split * len(test_stock)
                + self.split * (1 - self.feature_split) * len(test_stock)
            ) :
        ]
        stock = pd.DataFrame(stock_test_data, index=None)
        stock.to_csv("stock_data_test.csv")
