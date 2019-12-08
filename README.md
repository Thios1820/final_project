# final_project
CEBD 1160-Final Project
### Research Question
Compute Diagnosis data from patients and analyse the disease evolution depending on the gender in regard to the dataset criteria.

### Introduction

Using the diabetes dataset from the "Least Angle Regression," Annals of Statistics (with discussion), 407-499 of authors Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani (2004), we will be analysing a sample of 442 records of diabetes patient. The variables being studied are the age, sex, body mass index, average blood pressure, and six blood serum measurements were obtained for each of the patients.
Throughout this report, we will be drawing a comparison between male and female using  linear regression based on the age and the blood serums.


### Analysis

The first exploration we did was to compare the different blood serums based on the age for the female and male data.

#### Male 

After comparing the different serum samples against the age we were able to obtained the following graphs:

![Serum sample Male](IMG/Diabetes_M.png)

When observing the graph of the male, we can tell that the graph reflects a steady evolution.
We noted that the number of serums slightly increase overtime without an important variation being drawn between them.

#### Female

The female graph displays a similar steadiness between the serums. However, the range between each serum is greater than of the male graph.

![Serum sample Female](IMG/Diabetes_Female.png)

The above graph depicts the observations we just mentioned.


#### Linear regression

We did the linear regression on the S1 serum. 
Before the age 50, the numbers are lower for the male , while the female are more important after 50.
For the next graph, the female variation is much lower than the one from the male. 
And the different axes show how the male trend stays flat, while for the female it decreases as they age.

![Serum sample Female](IMG/S1_Male_Female_regression.png)

![Serum sample Female](IMG/S4_Male_Female_regression.png)

#### Observation on BMI
We have generated the same graph as above using the BMI values instead of the Age ones. 
We noted that the serums evolution was pretty similar for both criteria.
This confirms the hypothesis according to which BMI and Age are almost proportional.
We obtained the following graph that depicts our observation:

![BMI_Male](IMG/BMI_Male.png)

![BMI_Female](IMG/BMI_Female.png)

#### Disease progression after 1 year

It is apparent that for the male, the disease progression has much lower numbers than of the females.

![Disease_progression_Male](IMG/Disease_progression_Male.png)

![Disease_progression_Female](IMG/Disease_progression_Female.png)

We ran a linear regression after one year based on the Age and this is the graph obtained:

![DP_regression](IMG/DP_regression.png)

The disease progression for male is higher at a young age but gets slower for the females after they reach 50 years.
We observe the same thing by computing the same data for blood pressure.

We can say with confidence that the disease stays the same independently of the criteria that is studied. 



### Conclusion

After analyzing the data, we can conclude that S4 and S5 are the lowest and have almost the same numbers.
The trend is similar for all the other serums but at different rates. S1 being the highest and S3 being the lowest of the four.
However, the real change is observed when looking at the disease progression. 
As a matter of fact, computing linear regression on the disease progression according to the age helped us conclude on the following:
- At a young age, male have usually a higher numbers. But this change when comparing males and females over 50 years, where we see that females having higher numbers than males.
- We also observed the same trend when running the linear regression against BMI or BP.

Now the question is know what exactly caused these sudden changes?
Does it lie on the different aspects of the human body?