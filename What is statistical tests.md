## **What does a statistical test do ?**
>A statistical test provides a mechanism for making quantitative decisions about a process or processes. The intent is to determine whether there is enough evidence to "reject" a conjecture or hypothesis about the process. The conjecture is called the null hypothesis.
Statistical assumptions

### **Statistical tests make some common assumptions about the data they are testing:**

**- Independence of observations** 
    -The observations/variables you include in your test are not related (for example, multiple measurements of a single test subject are not independent, while measurements of multiple different test subjects are independent).
    
**- Homogeneity of variance:**
    the variance within each group being compared is similar among all groups. If one group has much more variation than others, it will limit the test’s effectiveness.
    
**- Normality of data:** 
    the data follows a normal distribution (a.k.a. a bell curve). This assumption applies only to quantitative data.
### **Types of variables :**
#### **1 -Quantitative variables represent amounts of things (e.g. the number of trees in a forest). Types of quantitative variables include:**

**-Continuous :**
    represent measures and can usually be divided into units smaller than one (e.g. 0.75 grams).
    
**-Discrete:** 
    represent counts and usually can’t be divided into units smaller than one (e.g. 1 tree).
#### **2 -Categorical variables represent groupings of things (e.g. the different tree species in a forest). Types of categorical variables include:**
**-Ordinal:** represent data with an order (e.g. rankings).

**-Nominal:** represent group names (e.g. brands or species names).

**-Binary:** represent data with a yes/no or 1/0 outcome (e.g. win or lose).
### **Choosing a parametric test :**
   #### 1 -Regression tests:
       Regression tests look for cause-and-effect relationships. They can be used to estimate the effect of one or more 
        continuous variables on another variable.
            1-Simple linear regression
                ex:What is the effect of income on longevity?
            2-Multiple linear regression
                ex:What is the effect of income and minutes of exercise per day on longevity?
            3-Logistic regression
                ex:What is the effect of drug dosage on the survival of a test subject?
#### 2-Comparison tests:
    Comparison tests look for differences among group means. They can be used to test the effect of a categorical variable on 
    the mean value of some other characteristic.
        1-Paired t-test
           ex: What is the effect of two different test prep programs on the average exam scores for students from the same 
           class?
        2-Independent t-test
           ex:What is the difference in average exam scores for students from two different schools?
        3-ANOVA
           ex: What is the difference in average pain levels among post-surgical patients given three different painkillers?
        4- MANOVA
           ex: What is the effect of flower species on petal length, petal width, and stem length?

#### 3-Correlation tests
    Correlation tests check whether variables are related without hypothesizing a cause-and-effect relationship.  
        1-Pearson’s r
         ex:How are latitude and temperature related?


```python

```
