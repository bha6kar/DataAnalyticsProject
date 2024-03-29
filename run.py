# %%
import matplotlib.pyplot as plt
from model_20_encoded import nnmodel

from autoencoder import AutoEncoder
from data_processing import DataProcessing
from data_retriever import DataRetrieverYahoo
from model import NeuralNetwork
from plot_stock_data import Plot_stock_data
from preprocessing import PreProcessing

# %%
SPLIT = 0.8
FEATURE_SPLIT = 0.25
INPUT_DIM = 55
ENCODED_DIM = 20
retriever = DataRetrieverYahoo("MSFT", "2000-01-01", "2019-03-21")
data = retriever.get_stock_data()


# retriever = DataRetrieverYahoo("AAPL", "2000-01-01", "2019-03-21")
# dataA = retriever.get_stock_data()

# retriever = DataRetrieverYahoo("GOOGL", "2000-01-01", "2019-03-21")
# dataG = retriever.get_stock_data()

# retriever = DataRetrieverYahoo("FB", "2000-01-01", "2019-03-21")
# dataFb = retriever.get_stock_data()

# plotting_data = Plot_stock_data(dataFb, "FB")
# plotting_data.pandas_candlestick_ohlc()


# plotting_data.comp_stock(data, dataA, dataFb, dataG)

# %%
preprocess = PreProcessing(SPLIT, FEATURE_SPLIT)
# %%
preprocess.make_wavelet_train()
preprocess.make_test_data()
# %%
autoencoder = AutoEncoder(ENCODED_DIM)
# %%
autoencoder.build_train_model(
    input_shape=INPUT_DIM,
    encoded1_shape=40,
    encoded2_shape=30,
    decoded1_shape=30,
    decoded2_shape=40,
)
# %%

process = DataProcessing(SPLIT, FEATURE_SPLIT)
# %%
process.make_train_data()
# %%
process.make_train_y()
# %%
process.make_test_data()
# %%
process.make_test_y()
# %%
model = NeuralNetwork(ENCODED_DIM)
model.make_train_model()
