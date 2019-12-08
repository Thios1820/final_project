import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

xm = []
ym = []
zm = []
am = []
bm = []
cm = []
dm = []
dp_m = []

xf = []
yf = []
zf = []
af = []
bf = []
cf = []
df = []
dp_f = []

with open('diabetes.data','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    x = []
    y = []
    for row in plots:
        if row[1] == '1':
            xm.append(float(row[2]))
            ym.append(float(row[4]))
            zm.append(float(row[5]))
            am.append(float(row[6]))
            bm.append(float(row[7]))
            cm.append(float(row[8]))
            dm.append(float(row[9]))
            dp_m.append(float(row[10]))
        else:
            xf.append(float(row[2]))
            yf.append(float(row[4]))
            zf.append(float(row[5]))
            af.append(float(row[6]))
            bf.append(float(row[7]))
            cf.append(float(row[8]))
            df.append(float(row[9]))
            dp_f.append(float(row[10]))


# Sort male
xyzabcd_m = zip(xm, ym, zm, am, bm, cm, dm, dp_m)
xyzabcd_m = sorted(xyzabcd_m)

xm = [x[0] for x in xyzabcd_m]
ym = [x[1] for x in xyzabcd_m]
zm = [x[2] for x in xyzabcd_m]
am = [x[3] for x in xyzabcd_m]
bm = [x[4] for x in xyzabcd_m]
cm = [x[5] for x in xyzabcd_m]
dm = [x[6] for x in xyzabcd_m]
dp_m = [x[7] for x in xyzabcd_m]


# Sort female
xyzabcd_f = zip(xf, yf, zf, af, bf, cf, df, dp_f)
xyzabcd_f = sorted(xyzabcd_f)

xf = [x[0] for x in xyzabcd_f]
yf = [x[1] for x in xyzabcd_f]
zf = [x[2] for x in xyzabcd_f]
af = [x[3] for x in xyzabcd_f]
bf = [x[4] for x in xyzabcd_f]
cf = [x[5] for x in xyzabcd_f]
df = [x[6] for x in xyzabcd_f]
dp_f = [x[6] for x in xyzabcd_f]

plt.figure(1)
plt.plot(xm,ym, label='BMI S1')
plt.plot(xm,zm, label='BMI S2')
plt.plot(xm,am, label='BMI S3')
plt.plot(xm,bm, label='BMI S4')
plt.plot(xm,cm, label='BMI S5')
plt.plot(xm,dm, label='BMI S6')

plt.title('Graph Male')
plt.legend()
# plt.show()


plt.figure(2)
plt.plot(xf,yf, label='BMI S1')
plt.plot(xf,zf, label='BMI S2')
plt.plot(xf,af, label='BMI S3')
plt.plot(xf,bf, label='BMI S4')
plt.plot(xf,cf, label='BMI S5')
plt.plot(xf,df, label='BMI S6')

plt.title('Graph Female')
plt.legend()


# disease progression
plt.figure(4)
plt.plot(xm, dp_m, label='Y=Disease progression X=BMI')
plt.title('Disease Progression Male')
plt.legend()

## REGRESSION S1 BMI

plt.figure(3)
X = np.array(xm).reshape(-1, 1)
Y = np.array(ym).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='blue')


X = np.array(xf).reshape(-1, 1)
Y = np.array(yf).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='pink')
plt.title('Graph regression Male and Female on S1')
plt.legend()


plt.show()