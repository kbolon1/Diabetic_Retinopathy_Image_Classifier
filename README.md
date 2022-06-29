# Image_Classifier_Diabetes
Final project for Spiced Academy.  

The number of cases and the prevalence of diabetes have been steadily increasing over the past few decades with approximately 422 million people diagnosed worldwide. Diabetic retinopathy is a complication of diabetes, caused by high blood sugar levels that damage the back of the eye.  It can cause blindness if left undiagnosed and untreated.  It is also the leading cause of vision impairment in the world and is 100% avoidable.

<p float="left" align="center">
<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Diabetes_Plotly_2011.png" width="500" height="400">
<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Diabetes_Plotly_2021.png" width="500" height="400">
</p>

Used Plotly with data pulled from the World Bank (https://databank.worldbank.org/home.aspx)

Over the years, computer-aided diagnosis have decreased medical costs and improved mass screening of populations.  AI helps doctors and clinicians utilise their time more efficiently by diagnosing through imaging and decreasing the amount time doctors are needed during the diagnosing period and they can spend more time treating people.

**Goal** 
Can I train an unsupervised machine learning model to accurately diagnose a digital image of an eye suffering from diabetic retinopathy?

**Models Used** 
ResNet152 Neural Network model with transfer learning with the following parameters:
    - loss=‘categorical_crossentropy'
    - Optimiser: Adam
    - Mix of Relu and Softmax Activations
    - 2 Classes 'diabetic' or 'healthy'
    - Epochs 300, no early stopping

<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Eye_Fundus.png" width="400" height="200">

I used the unprocessed images found on Kaggle:
    - https://www.kaggle.com/competitions/diabetic-retinopathy-detection
    - https://www.kaggle.com/competitions/aptos2019-blindness-detection
    - https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k

**Method:**
* Created a Deep-Learning Environment for Tensorflow and Keras and transfered the work to Google Colab as the sample sizes were too large for my computer to handle.
* Used Keras Preprocessing on the images to resize and to augment
* Built my own CNN model with 3 Convoluted layers with MaxPooling, a Flattening layer, and 3 Dense Layers with Dropout and Batch Normalization while using a mix of RELU and Sigmoid activations and selected Categorical_crossentropy for loss function.
* Tried a VGG19 model and then a ResNet152 model with transfer learning. Eventually trained it on a sample of 5000 images of each class with only 50% accuracy rate. 

**Currently:**
I have started over and changed the model to use the LazyAdam optimizer and will process the images differently.  I am researching best ways to preprocess the images.  Stay tuned for updates.

