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
