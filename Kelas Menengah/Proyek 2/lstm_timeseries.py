# -*- coding: utf-8 -*-
"""LSTM_Timeseries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PSr4V2PYwazCs8CVNNbJwLqdxu-k_C4s

# Projek Dicoding
## Belajar Pengembangan Machine Learning
### Time Series


---
##### Nama: Rangga Wibisana Putra Pamungkas
---
Projek Kedua Dicoding dari Belajar Pengembangan Machine Learning adalah membuat sebuah model  yang dapat memprediksi temperature dari data temperature di kota Washington menggunakan Long Short-Term Memory (LSTM) Layer.

# 1. Loading the Dataset
"""

# Menghubungkan Drive dengan Colab
from google.colab import drive
drive.mount('/content/drive')

# Load dataset sebagai dataframe
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/city_temperature.csv', low_memory=False)

# Melihat sampel teratas dataframe
df.head()

# Melihat info dari data set dan mengecek nilai null
df.info()
df.isnull().sum()

"""# Data Preprocessing"""

# Mengimpor paket yang diperlukan
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from keras.layers import Dense, LSTM
from keras.callbacks import ReduceLROnPlateau, Callback

# Mengambil hanya data dari kota Washington
df = df[df["City"] == "Washington"]
df.tail()

# Menggabungkan kolom Year-Month-Day menjadi satu kolom Dates
df['Dates'] = df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-' + df['Day'].astype(str)

# Menghapus kolom Year-Month-Day sebelumnya
df = df.drop(columns=["Year", "Month", "Day"], errors='ignore')

# Drop the old index
df = df.reset_index(drop=True)
df.tail()

# Menampilkan plot dari data
dates = df['Dates'].values
temp  = df['AvgTemperature'].values


plt.figure(figsize=(15,5))
plt.plot(dates, temp)
plt.title('Temperature average',
          fontsize=20);

"""# Encoding Labels and Making Train-Test Splits"""

# Mengubah data menjadi format yang dapat diterima oleh model
def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
  series = tf.expand_dims(series, axis=-1)
  ds = tf.data.Dataset.from_tensor_slices(series)
  ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
  ds = ds.flat_map(lambda w: w.batch(window_size + 1))
  ds = ds.shuffle(shuffle_buffer)
  ds = ds.map(lambda w: (w[:-1], w[-1:]))
  return ds.batch(batch_size).prefetch(1)

# Split data menjadi train dan test
dates_train, dates_test, temp_train, temp_test = train_test_split(
    dates, temp, test_size=0.2, shuffle=False)

train_set = windowed_dataset(temp_train, window_size=60,
                             batch_size=100, shuffle_buffer=1000)
test_set = windowed_dataset(temp_test, window_size=60,
                            batch_size=100, shuffle_buffer=1000)

print('train_set: ', len(dates_train))
print('test_set: ', len(dates_test))

"""# Building the Model"""

# model initialization
model = tf.keras.models.Sequential([
  tf.keras.layers.LSTM(60, return_sequences=True),
  tf.keras.layers.LSTM(60),
  tf.keras.layers.Dense(30, activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1),
])

# compile model
optimizer = tf.keras.optimizers.SGD(learning_rate=1.0000e-04, momentum=0.9)
model.compile(
  loss = tf.keras.losses.Huber(),
  optimizer = optimizer,
  metrics = ['mae'],
)

# Hitung MAE
mae = (df['AvgTemperature'].max() - df['AvgTemperature'].min()) * 0.1
print('MAE: %2.2f' % mae)

# Callback untuk mengurangi learning rate jika tidak ada peningkatan pada mae
reduce_lr = ReduceLROnPlateau(
    monitor="mae",
    patience=2,
    verbose=1,
    factor=0.5,
    min_lr=0.00001,
)


# Custom callback untuk menghentikan pelatihan jika mae mencapai < 10% skala data
class MyEarlyStop(Callback):
    def on_epoch_end(self, epoch, logs=None):
        if (logs.get('mae')<mae and logs.get('val_mae')<mae):
            print(
                '\nFor Epoch',
                epoch+1,
                'MAE has reached < 10% of the data scales',
                '\nMAE = %2.2f' % (logs['mae']),
                ', Val MAE = %2.2f' % (logs['val_mae']),
                ', training has been stopped.'
            )
            self.model.stop_training = True

"""# Model Training and Evaluation"""

# Pelatihan
history = model.fit(
  train_set,
  epochs=100,
  validation_data = test_set,
  callbacks = [reduce_lr, MyEarlyStop()],
  verbose=1
)

# Menampilkan plot accuracy dan loss
fig, ax = plt.subplots(1,2)
train_mae = history.history['mae']
train_loss = history.history['loss']
val_mae = history.history['val_mae']
val_loss = history.history['val_loss']
fig.set_size_inches(20,10)

# Plot accuracy dan loss dari training
ax[0].plot(train_mae , 'go-' , label = 'Training MAE')
ax[0].plot(val_mae , 'ro-' , label = 'Testing MAE')
ax[0].set_title('Training & Testing MAE')
ax[0].legend()
ax[0].set_xlabel("Epochs")
ax[0].set_ylabel("MAE")

# Plot accuracy dan loss dari testing
ax[1].plot(train_loss , 'go-' , label = 'Training Loss')
ax[1].plot(val_loss , 'ro-' , label = 'Testing Loss')
ax[1].set_title('Training & Testing Loss')
ax[1].legend()
ax[1].set_xlabel("Epochs")
ax[1].set_ylabel("Loss")
plt.show()