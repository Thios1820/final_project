import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

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
            xm.append(float(row[3]))
            ym.append(float(row[4]))
            zm.append(float(row[5]))
            am.append(float(row[6]))
            bm.append(float(row[7]))
            cm.append(float(row[8]))
            dm.append(float(row[9]))
            dp_m.append(float(row[10]))
        else:
            xf.append(float(row[3]))
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
dp_f = [x[7] for x in xyzabcd_f]

plt.figure(1)
plt.plot(xm,ym, label='Diabetes S1')
plt.plot(xm,zm, label='Diabetes S2')
plt.plot(xm,am, label='Diabetes S3')
plt.plot(xm,bm, label='Diabetes S4')
plt.plot(xm,cm, label='Diabetes S5')
plt.plot(xm,dm, label='Diabetes S6')
plt.plot(xm,dp_m, label='Progression')

plt.title('Graph Male')
plt.legend()

plt.figure(2)
plt.plot(xf,yf, label='Diabetes S1')
plt.plot(xf,zf, label='Diabetes S2')
plt.plot(xf,af, label='Diabetes S3')
plt.plot(xf,bf, label='Diabetes S4')
plt.plot(xf,cf, label='Diabetes S5')
plt.plot(xf,df, label='Diabetes S6')
plt.plot(xf,dp_f, label='Progression')

plt.title('Graph Female')
plt.legend()


# regression bp x dp
plt.figure(4)
Xm = np.array(xm).reshape(-1, 1)
Ym = np.array(dp_m).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(Xm, Ym)  # perform linear regression
Ym_pred = linear_regressor.predict(Xm)  # make predictions

plt.scatter(Xm, Ym)
plt.plot(Xm, Ym_pred, color='blue', label="LR DP Male")


plt.figure(4)
Xf = np.array(xf).reshape(-1, 1)
Bf = np.array(dp_f).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(Xf, Bf)  # perform linear regression
B_pred = linear_regressor.predict(Xf)  # make predictions

plt.scatter(Xf, Bf)
plt.plot(Xf, B_pred, color='pink', label="LR DP Female")

plt.show()
