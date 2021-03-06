# Metric
 Classes of validation metric for classification and regression
 
 ## Classification
In classification, a model predicts the actual condiction. 
In general, the models' performances are evaluated comparing the actual condition with the predicted condition. 
The labels in supervised learning are typically assigned by experts in the corresponding domain. 
Multiclass classification is referred to binary classification with, for example, one-hot encoding. 
Therefore, the metrics are implemented only for binary classification.
The definition of the True positive (TP), False negative (FN), False positive (FP), and True negative (TN) are given in the confusion matrix in **table 1**
 
|                      |         | **Predicted condition**|**Predicted condition**|
|----------------------|---------|:-------------------------:|:---------------------:|
|                      |         | Class 1                 | Class 2             |
| **Actual condition** | Class 1 | True positive ($TP$)      | False negative ($FN$) |
|**Actual condition**           | Class 2 | False positive ($FP$)     | True negative ($TN$)  |

**Table 1**: Confusion matrix for binary classification.\
<br>

The fraction of correct predicted examples and the sum of total examples is called Accuray:

 \$$ 
  \text{Accuracy}=\frac{TP+TN}{TP+FN+FP+TN}
 $$
 
 The Accuracy is suitable for balanced data sets.
 For imbalanced sets, where the data set consists of more examples for one class, Accuracy potentially leads to wrong performance evaluation of the model.\
 The **Sensitivity** is defined as the ratio of the $TP$ to the sum of actual true examples:

 \$$
 \text{Sensitivity}=\frac{TP}{TP+FN}
 $$
 
 Fokosing on the $TN$, the **Selectivity** enbodies the ratio of the $TN$ and the actual true negative values:
 
 \$$
 \text{Selectivity} = \frac{TN}{FP+TN}
 $$

The **Accuracy** is reformulated with the **Sensitivity** and the **Selectivity**:

\$$
	\frac{TP+TN}{TP+FN+FP+TN}=\frac{\frac{TP}{TP+FN}}{1+\frac{FP+TN}{TP+FN}}+\frac{\frac{TN}{FP+TN}}{1+\frac{1}{\frac{FP+TN}{TP+FN}}}
$$

In case of an imbalanced dataset, to limitting cases occur:
| Class 1 >> Class 2 |$\frac{FP+TN}{TP+FN}\to 0 $   |
|--------------------|---|
| Class 2 >> Class 1 |  $\frac{FP+TN}{TP+FN}\to \infty $ |

In case **Class 1 >> Class 2**, the **Accuracy** is equivalient to the **Sensitivity**. Hence, when reporting the **Accuracy**, the **Sensitivity** is measured:

\$$
\underset{\frac{FP+TN}{TP+FN}\to 0}{\mathop{\lim }} \left( \frac{\frac{TP}{TP+FN}}{1+\frac{FP+TN}{TP+FN}}+\frac{\frac{TN}{FP+TN}}{1+\frac{1}{\frac{FP+TN}{TP+FN}}} \right)=\frac{TP}{TP+FN}\equiv \text{Sensitivity}
$$

In case **Class 2 >> Class 1**, the **Accuracy** is equivalient to the **Selectivity**. Hence, when reporting the **Accuracy**, the **Selectivity** is measured:

\$$
\underset{\frac{FP+TN}{TP+FN}\to \infty }{\mathop{\lim }}\left( \frac{\frac{TP}{TP+FN}}{1+\frac{FP+TN}{TP+FN}}+\frac{\frac{TN}{FP+TN}}{1+\frac{1}{\frac{FP+TN}{TP+FN}}} \right)=\frac{TN}{FP+TN}\equiv \text{Selectivity}
$$

In image segmentation the case **Class 2 >> Class 1** often exists. Typically, pixels of **Class 2** are classified as background and pixels of **Class 1** enbody the interessted regions. 
The Jaccard Index, or Intersection over Union (IoU), is often used for binary problems in Computer Vision (CV) [1]. The IoU is suitable for backpropagation, since the aproximation of the IoU is differentiable [1]. 
The IoU is defined as:

\$$
IoU\_1 \equiv \frac{{{\left. \text{Class 1} \right|}\_{\text{Actual Condition}}}\bigcap {{\left. \text{Class 1} \right|}\_{\text{Predicted Condition}}}}{{{\left. \text{Class 1} \right|}\_{\text{Actual Condition}}}\bigcup {{\left. \text{Class 1} \right|}\_{\text{Predicted Condition}}}}
$$

Therefore, the for **Class 1** $IoU\_1$ is defined:

\$$
IoU_{1}=\frac{TP}{TP+FP+FN}
$$

The $IoU$ measures the relative global overlapping area. 
In case the describing of the borders of the elements are in focus, metrics based on the distance are more appropriate.

\[1] Floris van Beers, Using intersection over union loss to improve binary image segmentation, Bachelor's Thesis, 2018



