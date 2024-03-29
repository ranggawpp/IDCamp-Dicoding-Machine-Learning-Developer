# -*- coding: utf-8 -*-
"""ImageClassification_ModelDeployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BmG8FRv35vJklX_B3iw7bAZJNBkfJdTV

# Projek Akhir Dicoding
## Belajar Machine Learning Untuk Pemula


---
##### Nama: Rangga Wibisana Putra Pamungkas
---
Projek akhir dari Belajar Pengembangan Machine Learning ini adalah membuat sebuah model yang akan mengklasifikasikan dan mengenali gambar buah-buahan yang terdiri dari ['guava', 'cantaloupe', 'waterapple', 'pomelo', 'mango', 'bilimbi', 'orange', 'banana', 'coconut', 'pineapple', 'watermelon', 'papaya', 'melon']. Model ini dibuat dengan menggunakan program jaringan saraf tiruan dengan menggunakan library TensorFlow. Model yang telah dibuat kemudian disimpan dalam bentuk TFlite.

# Loading Dataset
"""

# Menghubungkan Drive dengan Colab
from google.colab import drive
drive.mount('/content/drive')

import os
os.environ['KAGGLE_CONFIG_DIR'] = "/content/drive/MyDrive/Kaggle"
os.chdir('/content/drive/MyDrive/Kaggle')
!kaggle datasets download -d yudhaislamisulistya/plants-type-datasets

os.chdir('/content')
!mkdir plants
!unzip -qq /content/drive/MyDrive/Kaggle/plants-type-datasets.zip  -d plants
!ls plants

# mengecek directory dataset hasil dari ekstrak file
import os
os.listdir('/content/plants/split_ttv_dataset_type_of_plants')

train_dir = os.path.join('/content/plants/split_ttv_dataset_type_of_plants/Train_Set_Folder')
os.listdir(train_dir)

import shutil

ignore_plants = ['spinach', 'cassava', 'soybeans', 'cucumber', 'eggplant', 'peper chili', 'sweet potatoes', 'paddy', 'curcuma', 'tobacco', 'galangal', 'kale', 'corn', 'longbeans', 'ginger', 'aloevera', 'shallot']

for x in ignore_plants:
  path = os.path.join(train_dir, x)
  shutil.rmtree(path)

list_plants = os.listdir(train_dir)
print(list_plants)

"""# Data Preprocessing"""

from PIL import Image
total = 0

for x in list_plants:
  dir = os.path.join(train_dir, x)
  y = len(os.listdir(dir))
  print(x+':', y)
  total = total + y

  img_name = os.listdir(dir)
  for z in range(4):
    img_path = os.path.join(dir, img_name[z])
    img = Image.open(img_path)
    print('-',img.size)
  print('---------------')

print('\nTotal :', total)

import os
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have the list of plants in 'list_plants'
plants_sorted = sorted(list_plants)

fig, ax = plt.subplots(4, 4, figsize=(18, 15))  # Create a 4x4 grid for 16 plots
fig.suptitle("Randomly Displayed Images from 13 Plants", fontsize=24)

# Iterate through plants and display random images
for i in range(4):
    for j in range(4):
        try:
            plant_selected = plants_sorted[i * 4 + j]  # Access plants in order
        except IndexError:  # Handle the last plant
            if i == 3 and j == 3:
                plant_selected = plants_sorted[-1]  # Get the last plant
            else:
                break

        if plant_selected == '.TEMP':
            continue

        plant_images = os.listdir(os.path.join(train_dir, plant_selected))
        random_image = np.random.choice(plant_images)
        img = plt.imread(os.path.join(train_dir, plant_selected, random_image))

        ax[i][j].imshow(img)
        ax[i][j].set_title(plant_selected, pad=10, fontsize=16)  # Adjust fontsize as needed
        ax[i][j].axis('off')  # Remove ticks for cleaner display

# Hide empty plots in the last row
for i in range(4):
    ax[3, i].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust spacing and title position
plt.show()

# data pre processing dengan image augmentation menggunakan ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,            # Apply shear transformations
    zoom_range=0.2,             # Randomly zoom in by up to 20%
    horizontal_flip=True,       # Randomly flip images horizontally
    fill_mode='wrap',           # Fill in newly created pixels using the nearest-neighbor method
    validation_split=0.2        # Reserve 20% of the data for validation
)

train_generator = train_datagen.flow_from_directory(
    train_dir,  # Specify the path to your training dataset
    target_size=(150, 150),      # Resize images to the desired dimensions
    batch_size=256,               # Batch size for training
    class_mode='categorical',    # Use categorical labels for multi-class classification
    subset='training'            # Specify 'training' subset for training data
)

validation_generator = train_datagen.flow_from_directory(
    train_dir,  # Specify the path to your training dataset
    target_size=(150, 150),      # Resize images to the desired dimensions
    batch_size=256,               # Batch size for validation
    class_mode='categorical',    # Use categorical labels for multi-class classification
    subset='validation'          # Specify 'validation' subset for validation data
)

"""# Building CNN Model"""

tf.device('/physical_device:GPU:0')

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(13, activation='softmax')
])

model.summary()

from keras.callbacks import ReduceLROnPlateau, Callback
# Callback untuk mengurangi learning rate jika tidak ada peningkatan pada akurasi
reduce_lr = ReduceLROnPlateau(
    monitor="accuracy",
    patience=2,
    verbose=1,
    factor=0.5,
    min_lr=0.00001,
)


# Custom callback untuk menghentikan pelatihan jika akurasi mencapai lebih dari 90%
class MyEarlyStop(Callback):
    def on_epoch_end(self, epoch, logs=None):
        if (logs.get('accuracy') >= 0.92 and logs.get('val_accuracy')>=0.92):
            print(
                '\nFor Epoch',
                epoch+1,
                '\nAccuracy has reached = %2.2f%%' % (logs['accuracy'] * 100),
                ', Val Accuracy = %2.2f%%' % (logs['val_accuracy'] * 100),
                ', training has been stopped.'
            )
            self.model.stop_training = True

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

"""# Model Training and Evaluation"""

history = model.fit(
    train_generator,
    steps_per_epoch = train_generator.samples // 256,
    epochs = 60,
    validation_data = validation_generator,
    validation_steps = validation_generator.samples // 256,
    verbose = 1,
    callbacks=[reduce_lr, MyEarlyStop()])

# Menampilkan plot accuracy dan loss
fig, ax = plt.subplots(1,2)
train_acc = history.history['accuracy']
train_loss = history.history['loss']
val_acc = history.history['val_accuracy']
val_loss = history.history['val_loss']
fig.set_size_inches(20,10)

# Plot accuracy dan loss dari training
ax[0].plot(train_acc , 'go-' , label = 'Training Accuracy')
ax[0].plot(val_acc , 'ro-' , label = 'Testing Accuracy')
ax[0].set_title('Training & Testing Accuracy')
ax[0].legend()
ax[0].set_xlabel("Epochs")
ax[0].set_ylabel("Accuracy")

# Plot accuracy dan loss dari testing
ax[1].plot(train_loss , 'go-' , label = 'Training Loss')
ax[1].plot(val_loss , 'ro-' , label = 'Testing Loss')
ax[1].set_title('Training & Testing Loss')
ax[1].legend()
ax[1].set_xlabel("Epochs")
ax[1].set_ylabel("Loss")
plt.show()

"""# Saving Model"""

import pathlib
# Menyimpan model dalam format SavedModel
export_dir = '/content/drive/MyDrive/Kaggle/'
tf.saved_model.save(model, export_dir)

# Convert SavedModel menjadi vegs.tflite
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()

tflite_model_file = pathlib.Path('plants.tflite')
tflite_model_file.write_bytes(tflite_model)