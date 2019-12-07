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

xf = []
yf = []
zf = []
af = []
bf = []
cf = []
df = []

with open('diabetes.data','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    x = []
    y = []
    for row in plots:
        if row[1] == '1':
            xm.append(float(row[0]))
            ym.append(float(row[4]))
            zm.append(float(row[5]))
            am.append(float(row[6]))
            bm.append(float(row[7]))
            cm.append(float(row[8]))
            dm.append(float(row[9]))
        else:
            xf.append(float(row[0]))
            yf.append(float(row[4]))
            zf.append(float(row[5]))
            af.append(float(row[6]))
            bf.append(float(row[7]))
            cf.append(float(row[8]))
            df.append(float(row[9]))


# Sort male
xyzabcd_m = zip(xm, ym, zm, am, bm, cm, dm)
xyzabcd_m = sorted(xyzabcd_m)

xm = [x[0] for x in xyzabcd_m]
ym = [x[1] for x in xyzabcd_m]
zm = [x[2] for x in xyzabcd_m]
am = [x[3] for x in xyzabcd_m]
bm = [x[4] for x in xyzabcd_m]
cm = [x[5] for x in xyzabcd_m]
dm = [x[6] for x in xyzabcd_m]


# Sort female
xyzabcd_f = zip(xf, yf, zf, af, bf, cf, df)
xyzabcd_f = sorted(xyzabcd_f)

xf = [x[0] for x in xyzabcd_f]
yf = [x[1] for x in xyzabcd_f]
zf = [x[2] for x in xyzabcd_f]
af = [x[3] for x in xyzabcd_f]
bf = [x[4] for x in xyzabcd_f]
cf = [x[5] for x in xyzabcd_f]
df = [x[6] for x in xyzabcd_f]

plt.figure(1)
plt.plot(xm,ym, label='Diabetes S1')
plt.plot(xm,zm, label='Diabetes S2')
plt.plot(xm,am, label='Diabetes S3')
plt.plot(xm,bm, label='Diabetes S4')
plt.plot(xm,cm, label='Diabetes S5')
plt.plot(xm,dm, label='Diabetes S6')

plt.title('Graph Male')
plt.legend()
# plt.show()


plt.figure(2)
plt.plot(xf,yf, label='Diabetes S1')
plt.plot(xf,zf, label='Diabetes S2')
plt.plot(xf,af, label='Diabetes S3')
plt.plot(xf,bf, label='Diabetes S4')
plt.plot(xf,cf, label='Diabetes S5')
plt.plot(xf,df, label='Diabetes S6')

plt.title('Graph Female')
plt.legend()




# REGRESSION ###############
plt.figure(3)
X = np.array(xm).reshape(-1, 1)
Y = np.array(ym).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='blue')


plt.figure(3)
X = np.array(xf).reshape(-1, 1)
Y = np.array(yf).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='pink')
plt.title('Graph regression Male and Female on S1')
plt.legend()



# REGRESSION ###########################
plt.figure(4)
Xm = np.array(xm).reshape(-1, 1)
Ym = np.array(am).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(Xm, Ym)  # perform linear regression
Ym_pred = linear_regressor.predict(Xm)  # make predictions

plt.scatter(Xm, Ym)
plt.plot(Xm, Ym_pred, color='blue')


plt.figure(4)
Xf = np.array(xf).reshape(-1, 1)
Bf = np.array(af).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(Xf, Bf)  # perform linear regression
B_pred = linear_regressor.predict(Xf)  # make predictions

plt.scatter(Xf, Bf)
plt.plot(Xf, B_pred, color='pink')






plt.title('Graph regression Male and Female on S4')
plt.legend()


plt.show()