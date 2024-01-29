
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



a = load_digits()

df = pd.DataFrame(a.data)

aa = pd.DataFrame(a.target)

df['target'] = a.target

X_train, X_test, Y_train, Y_test = train_test_split(df.drop(['target'], axis='columns'),a.target, test_size=0.2, random_state=100)

rf = RandomForestClassifier(n_estimators=1500)

rf.fit(X_train, Y_train)

predict = rf.predict(X_test)


import streamlit as st
from PIL import Image
import numpy as np


st.write('accuracy: ',accuracy_score(predict, Y_test))

st.title('Blur image classifier')

file_up = st.file_uploader('Upload image', type=['jpg', 'png'])

if file_up is not None:

    image = Image.open(file_up)

    gray_image = image.convert("L")

    resized_image = gray_image.resize((8,8))

    image_array = np.array(resized_image).flatten()


    if image_array is not None:


        image_array = image_array.reshape(1, -1)

        result = rf.predict(image_array)

        st.image(file_up)

        st.write("Prediction result:", result)

