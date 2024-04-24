---
title: Machine Learning
created: Monday 24th April 2023 19:15
aliases:
  - ML
  - ml
tags:
  - ml
  - dl
  - ai
---
**Machine learning** is a subfield of [[Artificial Intelligence]] that uses algorithms trained on data sets to create models that enable machines to perform tasks that would otherwise only be possible for humans, such as categorizing images, analyzing data, or predicting price fluctuations.

At its core, the method simply uses algorithms – essentially lists of rules – adjusted and refined using past data sets to make predictions and categorizations when confronted with new data. For example, a [machine learning algorithm](##Models) may be “trained” on a data set consisting of thousands of images of flowers that are labeled with each of their different flower types so that it can then correctly identify a flower in a new photograph based on the differentiating characteristics it learned from other pictures.  

To ensure such algorithms work effectively, however, they must typically be refined many times until they accumulate a comprehensive list of instructions that allow them to function correctly. Algorithms that have been trained sufficiently eventually become [machine learning models](##Models), which are essentially algorithms that have been trained to perform specific tasks like sorting images, predicting housing prices, or making chess moves. In some cases, algorithms are layered on top of each other to create complex networks that allow them to do increasingly complex, nuanced tasks like generating text and powering chatbots via a method known as “[deep learning](https://www.coursera.org/articles/what-is-deep-learning).”

| Tool/Framework                                          | Description                                                                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [AIStore](https://github.com/NVIDIA/aistore)            | Scalable storage for AI applications                                                                          |
| [WebDataset](https://github.com/webdataset/webdataset)  | A high-performance Python-based I/O system for large                                                          |
| [Deepforge](https://github.com/deepforge-dev/deepforge) | A modern development environment for deep learning                                                            |
| [Havorod](https://github.com/horovod/horovod)           | Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet                               |
| [Lime](https://github.com/marcotcr/lime)                | Explaining the predictions of any machine learning classifier                                                 |
| [MLRun](https://github.com/mlrun/mlrun)                 | Machine Learning automation and tracking                                                                      |
| [Elyra](https://github.com/elyra-ai/elyra)              | Elyra extends JupyterLab with an AI centric approach                                                          |
| [Autogoal](https://github.com/autogoal/autogoal)        | A Python framework for program synthesis with a focus on Automated Machine Learning                           |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed)     | Deep learning optimization library                                                                            |
| [TorchScale](https://github.com/microsoft/torchscale)   | Transformers at any scale                                                                                     |
| [Tiktoken](https://github.com/openai/tiktoken)          | Fast BPE tokeniser for use with OpenAI's models                                                               |
| [Ray](https://github.com/ray-project/ray)               | Ray is a unified framework for scaling AI and Python applications                                             |
| [Aim](https://github.com/aimhubio/aim)                  | An easy-to-use & supercharged open-source experiment tracker                                                  |
| [Meltano](https://github.com/meltano/meltano)           | The declarative code-first data integration engine that powers your wildest data and ML-powered product ideas |
| [Hydra](https://github.com/facebookresearch/hydra)      | Framework for elegantly configuring complex applications                                                      |
| [Evidently](https://github.com/evidentlyai/evidently)   | Evaluate and monitor ML models from validation to production                                                  |
## Types

### Supervised machine learning 

In supervised machine learning, algorithms are trained on _labeled_ data sets that include tags describing each piece of data. In other words, the algorithms are fed data that includes an “answer key” describing how the data should be interpreted. For example, an algorithm may be fed images of flowers that include tags for each flower type so that it will be able to identify the flower better again when fed a new photograph. 

Supervised machine learning is often used to create machine learning models used for prediction and classification purposes. 
### Unsupervised machine learning 

Unsupervised machine learning uses _unlabeled_ data sets to train algorithms. In this process, the algorithm is fed data that doesn't include tags, which requires it to uncover patterns on its own without any outside guidance. For instance, an algorithm may be fed a large amount of unlabeled user data culled from a social media site in order to identify behavioral trends on the platform. 

Unsupervised machine learning is often used by researchers and data scientists to identify patterns within large, unlabeled data sets quickly and efficiently. 

### Semi-supervised machine learning 

Semi-supervised machine learning uses both _unlabeled and labeled_ data sets to train algorithms. Generally, during semi-supervised machine learning, algorithms are first fed a small amount of labeled data to help direct their development and then fed much larger quantities of unlabeled data to complete the model. For example, an algorithm may be fed a smaller quantity of labeled speech data and then trained on a much larger set of unlabeled speech data in order to create a machine learning model capable of speech recognition. 

Semi-supervised machine learning is often employed to train algorithms for classification and prediction purposes in the event that large volumes of labeled data is unavailable. 

### Reinforcement learning 

Reinforcement learning uses _trial and error_ to train algorithms and create models. During the training process, algorithms operate in specific environments and then are provided with feedback following each outcome. Much like how a child learns, the algorithm slowly begins to acquire an understanding of its environment and begins to optimize actions to achieve particular outcomes. For instance, an algorithm may be optimized by playing successive games of chess, which allow it to learn from its past success and failures playing each game.

## Models

![[ml-models.jpg]]

### Regression
#### Linear regression

**Linear regression** is a supervised machine learning technique used for predicting and forecasting values that fall within a continuous range, such as sales numbers or housing prices. It is a technique derived from statistics and is commonly used to establish a relationship between an input variable (X) and an output variable (Y) that can be represented by a straight line.

In simple terms, linear regression takes a set of data points with known input and output values and finds the line that best fits those points. This line, known as the "**regression line**," serves as a predictive model. By using this line, we can estimate or predict the output value (Y) for a given input value (X).

Linear regression is primarily used for **predictive modeling** rather than categorization. It is useful when we want to understand how changes in the input variable affect the output variable. By analyzing the slope and intercept of the regression line, we can gain insights into the relationship between the variables and make predictions based on this understanding.
#### Logistic regression

**Logistic regression**, also known as "logit regression," is a supervised learning algorithm primarily used for binary classification tasks. It is commonly employed when we want to determine whether an input belongs to one class or another, such as deciding whether an image is a cat or not a cat. 

Logistic regression predicts the _probability_ that an input can be categorized into a single primary class. However, in practice, it is commonly used to group outputs into two categories: the primary class and not the primary class. To accomplish this, logistic regression creates a threshold or boundary for binary classification. For example, any output value between 0 and 0.49 might be classified as one group, while values between 0.50 and 1.00 would be classified as the other group. 

Consequently, logistic regression is typically used for binary categorization rather than predictive modeling. It enables us to assign input data to one of two classes based on the probability estimate and a defined threshold. This makes logistic regression a powerful tool for tasks such as image recognition, spam email detection, or medical diagnosis where we need to categorize data into distinct classes.
### Classification
#### Naive Bayes 

**Naive Bayes** is a set of supervised learning algorithms used to create predictive models for binary or multi-classification tasks. It is based on **Bayes' Theorem** and operates on conditional probabilities, which estimate the likelihood of a classification based on the combined factors while assuming independence between them.

Let's consider a program that identifies plants using a Naive Bayes algorithm. The algorithm takes into account specific factors such as perceived size, color, and shape to categorize images of plants. Although each of these factors is considered independently, the algorithm combines them to assess the probability of an object being a particular plant.

Naive Bayes leverages the assumption of independence among the factors, which simplifies the calculations and allows the algorithm to work efficiently with large datasets. It is particularly well-suited for tasks like document classification, email spam filtering, sentiment analysis, and many other applications where the factors can be considered separately but still contribute to the overall classification.
#### Decision tree

A **decision tree** is a supervised learning algorithm used for classification and predictive modeling tasks. It resembles a flowchart, starting with a **root node** that asks a specific question about the data. Based on the answer, the data is directed down different branches to subsequent **internal nodes**, which ask further questions and guide the data to subsequent branches. This process continues until the data reaches an **end node**, also known as a **leaf node**, where no further branching occurs.

Decision tree algorithms are popular in machine learning because they can handle complex datasets with ease and simplicity. The algorithm's structure makes it straightforward to understand and interpret the decision-making process. By asking a sequence of questions and following the corresponding branches, decision trees enable us to classify or predict outcomes based on the data's characteristics.

This simplicity and interpretability make decision trees valuable for various applications in machine learning, especially when dealing with complex datasets.
#### Random forest

A **random forest** algorithm is an ensemble of decision trees used for classification and predictive modeling. Instead of relying on a single decision tree, a random forest combines the predictions from multiple decision trees to make more accurate predictions.

In a random forest, numerous decision tree algorithms (sometimes hundreds or even thousands) are individually trained using different random samples from the training dataset. This sampling method is called "**bagging**." Each decision tree is trained independently on its respective random sample.

Once trained, the random forest takes the same data and feeds it into each decision tree. Each tree produces a prediction, and the random forest tallies the results. The most common prediction among all the decision trees is then selected as the final prediction for the dataset.

Random forests address a common issue called "**overfitting**" that can occur with individual decision trees. Overfitting happens when a decision tree becomes too closely aligned with its training data, making it less accurate when presented with new data.

#### K-nearest neighbor (KNN)

**K-nearest neighbor (KNN)** is a supervised learning algorithm commonly used for classification and predictive modeling tasks. The name "K-nearest neighbor" reflects the algorithm's approach of classifying an output based on its proximity to other data points on a graph. 

Let's say we have a dataset with labeled points, some marked as blue and others as red. When we want to classify a new data point, KNN looks at its nearest neighbors in the graph. The "K" in KNN refers to the number of nearest neighbors considered. For example, if K is set to 5, the algorithm looks at the 5 closest points to the new data point.

Based on the majority of the labels among the K nearest neighbors, the algorithm assigns a classification to the new data point. For instance, if most of the nearest neighbors are blue points, the algorithm classifies the new point as belonging to the blue group.

Additionally, KNN can also be used for prediction tasks. Instead of assigning a class label, KNN can estimate the value of an unknown data point based on the average or median of its K nearest neighbors.
#### Support vector machine (SVM)

A **support vector machine (SVM)** is a supervised learning algorithm commonly used for classification and predictive modeling tasks. SVM algorithms are popular because they are reliable and can work well even with a small amount of data. SVM algorithms work by creating a decision boundary called a **hyperplane**. In two-dimensional space, this hyperplane is like a line that separates two sets of labeled data. 

The goal of SVM is to find the best possible decision boundary by maximizing the margin between the two sets of labeled data. It looks for the widest gap or space between the classes. Any new data point that falls on either side of this decision boundary is classified based on the labels in the training dataset.

It's important to note that hyperplanes can take on different shapes when plotted in three-dimensional space, allowing SVM to handle more complex patterns and relationships in the data.

##### Linear support vector classifier

A Linear SVC uses a boundary of one-degree (linear / straight line) to classify data. It has much less complexity than a non-linear classifier and is only appropriate for small datasets. More complex datasets will require a non linear classifier.

##### NuSVC

NuSVC uses Nu parameters which is for regularization. Nu is the upper bound on the expected classification error. If the value of Nu us 10% then 10% of the data will be misclassified.
### Clustering

#### K-means

**K-means** is an unsupervised algorithm commonly used for clustering and pattern recognition tasks. It aims to group data points based on their proximity to one another. Similar to K-nearest neighbor (KNN), K-means clustering utilizes the concept of proximity to identify patterns in data.

Each of the clusters is defined by a **centroid**, a real or imaginary center point for the cluster. K-means is useful on large data sets, especially for clustering, though it can falter when handling outliers.

Clustering algorithms are particularly useful for large datasets and can provide insights into the inherent structure of the data by grouping similar points together. It has applications in various fields such as customer segmentation, image compression, and anomaly detection.
### Gradient boosting

**Gradient boosting** algorithms employ an ensemble method, which means they create a series of "weak" models that are iteratively improved upon to form a strong predictive model. The iterative process gradually reduces the errors made by the models, leading to the generation of an optimal and accurate final model.

The algorithm starts with a simple, naive model that may make basic assumptions, such as classifying data based on whether it is above or below the mean. This initial model serves as a starting point.

In each iteration, the algorithm builds a new model that focuses on correcting the mistakes made by the previous models. It identifies the patterns or relationships that the previous models struggled to capture and incorporates them into the new model.

Gradient boosting is effective in handling complex problems and large datasets. It can capture intricate patterns and dependencies that may be missed by a single model. By combining the predictions from multiple models, gradient boosting produces a powerful predictive model.
## Notebooks

Computation notebooks have been used as electronic lab notebooks to document procedures, data, calculations, and findings. [[Jupyter]] notebooks provide an interactive computational environment for developing data science applications.

Jupyter notebooks combine software code, computational output, explanatory text, and rich content in a single document. Notebooks allow in-browser editing and execution of code and display computation results. A notebook is saved with an `.ipynb` extension. The Jupyter Notebook project supports dozens of programming languages, its name reflecting support for Julia (Ju), Python (Py), and R.

# MLOps

- [MLOps: Task and Workflow Orchestration Tools on Kubernetes](https://achernov.medium.com/mlops-task-and-workflow-orchestration-tools-on-kubernetes-adba3020d2bc)
- [ClearML Agent](https://github.com/allegroai/clearml-agent) - ClearML Agent - ML-Ops made easy
# CD4ML

<iframe width="560" height="315" src="https://www.youtube.com/embed/UzVa5azAHkc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- [Continuous Delivery for Machine Learning](https://martinfowler.com/articles/cd4ml.html)
- [A CD4ML Example Setup on AWS S3, GitLab with DVC](https://github.com/sbalnojan/cd4ml-example)
- [Continuous Intelligence and CD4ML Workshop](https://github.com/ThoughtWorksInc/cd4ml-workshop)
- [How to Version Control your Machine Learning task — I](https://towardsdatascience.com/how-to-version-control-your-machine-learning-task-cad74dce44c4)

# Deploy

- [Serving ML Models in Production with FastAPI and Celery](https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db)

# Integrations

- [Keeping your ML model in shape with Kafka, Airflow and MLFlow](https://medium.com/vantageai/keeping-your-ml-model-in-shape-with-kafka-airflow-and-mlflow-143d20024ba6)
- [Introducing Elyra pipelines with custom component support](https://medium.com/ibm-data-ai/introducing-elyra-pipelines-with-custom-component-support-ae6b616910b5)
- [Automate your machine learning workflow tasks using Elyra and Apache Airflow](https://medium.com/ibm-data-ai/automate-your-machine-learning-workflow-tasks-using-elyra-and-apache-airflow-adf297adc455)
- [Elyra 3.3: Pipelines, custom components, and catalogs](https://medium.com/ibm-data-ai/elyra-3-3-pipelines-custom-components-and-catalogs-74cf198fdf48)

# Models

- [DiT (Document Image Transformer) is a self-supervised pre-trained Document Image Transformer model](https://github.com/microsoft/unilm/tree/master/dit)

## Hyperparameter tuning

- [A Practical Introduction to Grid Search, Random Search, and Bayes Search](https://towardsdatascience.com/a-practical-introduction-to-grid-search-random-search-and-bayes-search-d5580b1d941d)
## Pytorch

- [Some Techniques To Make Your PyTorch Models Train (Much) Faster](https://sebastianraschka.com/blog/2023/pytorch-faster.html)
- [Efficient PyTorch I/O library for Large Datasets, Many Files, Many GPUs](https://pytorch.org/blog/efficient-pytorch-io-library-for-large-datasets-many-files-many-gpus/)