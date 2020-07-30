# Detection-of-Alzheimer-s-Disease-using-Deep-Learning-Algorithm

Alzheimer’s disease is a neurological disorder that causes memory loss and dementia. It is mainly observed in elderly individuals over the age of 60. It causes the brain cells to die and spread the damage throughout. Its symptoms usually start slowly and are mild. There are many ways to diagnose and detect it. MRI scans, PET scans and MMSE (Mini-Mental State Examination) expressed in terms of CDR (Clinical Dementia Rating) standards are a few. Though the above methods help in predicting the disease accurately, identifying distinctions between Alzheimer’s brain and normal brain in elderly individuals (over the age of 75) is diﬃcult. This is because they share similar brain patterns and image intensities.

 Early diagnosis of Alzheimer's makes individuals eligible for a wider variety of clinical trials. The objective of this project is to develop a system for detecting Alzheimer’s Disease (AD) using the methodology of Deep Learning. This is to accomplish the aim of reducing human (Doctor) eﬀorts for detecting the disease by developing a reliable system.

 The implementation of this project includes image processing followed by using the pre-processed images to train a deep learning model. The deep learning model uses Convolutional Neural Networks algorithm. This model is Sequential in nature and classiﬁes the data into two categories, namely CN (Cognitively Normal) and AD (Alzheimer’s Disease).

Data set for this project was obtained from ADNI ( Alzheimer’s Disease Neuroimaging Initiative).

 Pre-processing involved separating the brain tissues in MRI scans. The effect of Alzheimer's Disease on a brain can be understood by observing its grey matter(that shrinks as an effect of the disease). Hence, grey matter from the MRI was extracted. This was done using MATLAB (for the middle most slice of each MRI scan). 
