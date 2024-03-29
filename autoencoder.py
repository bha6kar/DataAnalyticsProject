import numpy as np
import pandas as pd
from keras import regularizers
from keras.layers import Dense, Input
from keras.models import Model


class AutoEncoder:
    def __init__(self, encoding_dim):
        self.encoding_dim = encoding_dim

    def build_train_model(
        self,
        input_shape,
        encoded1_shape,
        encoded2_shape,
        decoded1_shape,
        decoded2_shape,
        epochs=1000,
    ):
        input_data = Input(shape=(1, input_shape))

        encoded1 = Dense(
            encoded1_shape, activation="relu", activity_regularizer=regularizers.l2(0)
        )(input_data)
        encoded2 = Dense(
            encoded2_shape, activation="relu", activity_regularizer=regularizers.l2(0)
        )(encoded1)
        encoded3 = Dense(
            self.encoding_dim,
            activation="relu",
            activity_regularizer=regularizers.l2(0),
        )(encoded2)
        decoded1 = Dense(
            decoded1_shape, activation="relu", activity_regularizer=regularizers.l2(0)
        )(encoded3)
        decoded2 = Dense(
            decoded2_shape, activation="relu", activity_regularizer=regularizers.l2(0)
        )(decoded1)
        decoded = Dense(
            input_shape, activation="sigmoid", activity_regularizer=regularizers.l2(0)
        )(decoded2)

        autoencoder = Model(inputs=input_data, outputs=decoded)

        encoder = Model(input_data, encoded3)

        autoencoder.compile(loss="mean_squared_error", optimizer="adam")

        train = pd.read_csv("preprocessing/rbm_train.csv", index_col=0)
        ntrain = np.array(train)
        train_data = np.reshape(ntrain, (len(ntrain), 1, input_shape))

        autoencoder.fit(train_data, train_data, epochs=epochs)

        encoder.save("models/encoder.h5")

        test = pd.read_csv("preprocessing/rbm_test.csv", index_col=0)
        ntest = np.array(test)
        test_data = np.reshape(ntest, (len(ntest), 1, 55))

        print(
            "Encoder model mse: {}".format(autoencoder.evaluate(test_data, test_data))
        )

        log_train = pd.read_csv("preprocessing/log_train.csv", index_col=0)
        coded_train = []
        for i in range(len(log_train)):
            data = np.array(log_train.iloc[i, :])
            values = np.reshape(data, (1, 1, 55))
            coded = encoder.predict(values)
            shaped = np.reshape(coded, (self.encoding_dim,))
            coded_train.append(shaped)

        train_coded = pd.DataFrame(coded_train)
        train_coded.to_csv("features/autoencoded_data.csv")
