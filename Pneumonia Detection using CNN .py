#!/usr/bin/env python
# coding: utf-8
# testing this code
#Devansh Soni
import os
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# In[2]:


model= Sequential()
model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(64,64,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


# In[3]:


model


# In[4]:


model.summary()


# In[5]:


from keras_preprocessing.image import ImageDataGenerator


# In[9]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
training_set = train_datagen.flow_from_directory(
        '/model_files/chest-xray-pneumonia/chest_xray/chest_xray/train/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')


# In[10]:


test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
        '/model_files/chest-xray-pneumonia/chest_xray/chest_xray/test/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')


# In[36]:
model.fit(
        training_set,
        steps_per_epoch=100,
        epochs=1,
        validation_data=test_set,
        validation_steps=200)

# In[ ]:





# In[14]:


# from keras.preprocessing import image


# # In[15]:


# test_image = image.load_img('./chest-xray-pneumonia/chest_xray/chest_xray/test/PNEUMONIA/person100_bacteria_481.jpeg', 
#                target_size=(64,64))
# test_image2=image.load_img('./chest-xray-pneumonia/chest_xray/chest_xray/test/NORMAL/IM-0027-0001.jpeg', 
#                target_size=(64,64))
# print(test_image)
# print(type(test_image))
# converted_image=image.img_to_array(test_image)
# converted_image2=image.img_to_array(test_image2)
# print(converted_image.shape)
# print(type(converted_image))
# converted_image = np.expand_dims(converted_image,axis=0)
# converted_image2 = np.expand_dims(converted_image2,axis=0)
# print(converted_image.shape)
# result=model.predict(converted_image)
# result2 = model.predict(converted_image2)
# print(training_set.class_indices)
# print(result)
# print(result2)
# # from keras.models import save_model
# # save_model(model,'./pneumonia_model.h5')


# # In[16]:


# from keras.models import load_model


# # In[17]:


# model = load_model('./pneumonia_model.h5')


# # In[18]:


# print(model.predict(converted_image))
# print(model.predict(converted_image2))


# # In[ ]:




