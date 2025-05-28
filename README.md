
## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)


## Introduction

The Internet has become an essential part of our daily lives, but it has also opened the door to various anonymous cyber threats, including phishing. Phishers often use social engineering tactics or fake websites to trick users into revealing sensitive information like account IDs, usernames, and passwords. While numerous techniques have been developed to detect such attacks, cybercriminals continue to adapt and bypass these defenses. Machine learning has emerged as one of the most effective approaches to combat phishing, as these attacks tend to share identifiable patterns that machine learning models can detect


## Installation
pip install -r requirements.txt
```

## Directory Tree 
```
├── pickle
│   ├── model.pkl
├── static
│   ├── styles.css
├── templates
│   ├── index.html
├── Phishing URL Detection.ipynb
├── Procfile
├── README.md
├── app.py
├── feature.py
├── phishing.csv
├── requirements.txt

## Result

Accuracy of various model used for URL detection
<br>

<br>

||ML Model|	Accuracy|  	f1_score|	Recall|	Precision|
|---|---|---|---|---|---|
0|	Gradient Boosting Classifier|	0.974|	0.977|	0.994|	0.986|
1|	CatBoost Classifier|	        0.972|	0.975|	0.994|	0.989|
2|	XGBoost Classifier| 	        0.969|	0.973|	0.993|	0.984|
3|	Multi-layer Perceptron|	        0.969|	0.973|	0.995|	0.981|
4|	Random Forest|	                0.967|	0.971|	0.993|	0.990|
5|	Support Vector Machine|	        0.964|	0.968|	0.980|	0.965|
6|	Decision Tree|      	        0.960|	0.964|	0.991|	0.993|
7|	K-Nearest Neighbors|        	0.956|	0.961|	0.991|	0.989|
8|	Logistic Regression|        	0.934|	0.941|	0.943|	0.927|
9|	Naive Bayes Classifier|     	0.605|	0.454|	0.292|	0.997|





## Conclusion
1. This project provided a hands-on opportunity to experiment with multiple machine learning algorithms, carry out exploratory data analysis on a phishing dataset, and gain a deeper understanding of the significant features involved in detecting phishing URLs.

2. Working through this notebook enhanced my understanding of how different features impact model performance and how hyperparameter tuning can optimize results.

3. The analysis revealed that features such as "HTTPS", "AnchorURL", and "WebsiteTraffic" play a crucial role in determining whether a URL is malicious or legitimate.

4. Among all the models tested, the Gradient Boosting Classifier demonstrated the highest accuracy, correctly identifying phishing URLs with 97.4% accuracy, thereby significantly reducing the likelihood of malicious links being misclassified.

