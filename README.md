# Image_Classifier_Diabetes
Final project for Spiced Academy.  

Trained a neural network classification model (ResNet152) with transfer learning to identify between a healthy eye or an eye suffering from diabetic retinopathy with over 10,000 images including data augmentation.  This aims to improve the mass screening of populations and eventually decrease medical costs through computer-aided diagnosis. This is crucial as the number of cases and the prevalence of diabetes have steadily increased over the past few decades with approximately 422 million people diagnosed worldwide. Diabetic retinopathy is a complication of diabetes, caused by high blood sugar levels that damage the back of the eye.  It can cause blindness if left undiagnosed and untreated.  It is also the leading cause of vision impairment in the world and is 100% avoidable.

<p float="left" align="center">
<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Diabetes_Plotly_2011.png" width="500" height="400">
<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Diabetes_Plotly_2021.png" width="500" height="400">
</p>

Used Plotly with data pulled from the World Bank (https://databank.worldbank.org/home.aspx)

<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Eye_Fundus.png" width="400" height="200">

I used the unprocessed images found on Kaggle:
    - https://www.kaggle.com/competitions/diabetic-retinopathy-detection
    - https://www.kaggle.com/competitions/aptos2019-blindness-detection
    - https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k

**Method:**
* Created a Deep-Learning Environment for Tensorflow and Keras and transfered the work to Google Colab .
* Used Keras Preprocessing on the images to resize and to augment
* Trained it on a sample of 5000 images of each class (10000 in totals) with only 50% accuracy rate. 

**Currently:**
I have started over and changed the model to use the LazyAdam optimizer and will process the images differently.  I am researching best ways to preprocess the images.  Stay tuned for updates.
