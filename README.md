# Diabetic_Retinopathy_Image_Classifier
Final project for Spiced Academy.  Trained a ResNet152 model to differentiate between severity of the condition

# [Final Project: Image Classification Using Transfer Learning on ResNet152 Model]

Goal: to train a model to distinguish between the stages of diabetic retinopathy (blindness caused by high blood sugar levels). 

0 - No DR
1 - Mild
2 - Moderate
3 - Severe
4 - Proliferative DR

![](https://github.com/kbolon1/Portfolio/blob/main/images/Eye_Fundus.png)

I used the unprocessed images found on Kaggle:
    https://www.kaggle.com/competitions/diabetic-retinopathy-detection

* Used Plotly to show the prevalence of diabetes with data pulled from the World Bank (https://databank.worldbank.org/home.aspx)
![](https://github.com/kbolon1/Portfolio/blob/main/images/Diabetes_Plotly_2011.png)
![](https://github.com/kbolon1/Portfolio/blob/main/images/Diabetes_Plotly_2021.png)
* Created a Deep-Learning Environment for Tensorflow and Keras at the beginning and then moved to Google Colab as the sample size were large
* Used Keras Preprocessing on the images to resize and to augment
* Built my own CNN model with 3 Convoluted layers with MaxPooling, a Flattening layer, and 3 Dense Layers with Dropout and Batch Normalization while using a mix of RELU and Sigmoid activations and selected Categorical_crossentropy for loss function.
* Tried a VGG19 model and then a ResNet152 model with transfer learning. Eventually trained it on a sample of 5000 images of each class with only 50% accuracy rate. I am still working on improving this.

