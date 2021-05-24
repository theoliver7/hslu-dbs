import numpy as np
from matplotlib import pyplot as plt
from pydrill.client import PyDrill
from pydrill.exceptions import ImproperlyConfigured
from sklearn import linear_model
from sklearn import metrics

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

results = drill.query('select * from dfs.tmp.joinedViewGamesFrPu3', timeout=100)

df = results.to_dataframe()
df = df.sort_values(by="publisherName")
print(df)
x_values = df['averageUserScore'].values[:, np.newaxis]
y_values = df['sumGamesSales'].values[:, np.newaxis]
annotation = df['publisherName'].values[:, np.newaxis]



x_values = np.float32(x_values)
y_values = np.float32(y_values)


body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

prediction = body_reg.predict(np.sort(x_values, axis=0))



colors = ["tab:blue", "tab:purple", "tab:green", "tab:pink", "tab:brown", "tab:cyan", "tab:orange"]
colorIdx = 0
publisher = annotation[0]
tmp_x_values = list()
tmp_y_values = list()
for idx, x in enumerate(x_values):
    if annotation[idx] == publisher:
        tmp_x_values.append(x_values[idx])
        tmp_y_values.append(y_values[idx])
    else:
        plt.scatter(tmp_x_values, tmp_y_values, c=colors[colorIdx], label=publisher[0])

        tmp_x_values = list()
        tmp_y_values = list()
        tmp_x_values.append(x_values[idx])
        tmp_y_values.append(y_values[idx])

        publisher = annotation[idx+1]
        colorIdx += 1
plt.scatter(tmp_x_values, tmp_y_values, c=colors[colorIdx], label=annotation[-1][0])

ax = plt.plot(np.sort(x_values, axis=0), prediction, label="Linear regression(OLS)")


plt.title('Influence of user score on sales')
plt.ylabel('Sum of Game sales(in Mio$)')
plt.xlabel('Average User Score(0-10)')


plt.legend(loc="upper right")
plt.show()


print('Mean Absolute Error:', metrics.mean_absolute_error(y_values, prediction))
print('Mean Squared Error:', metrics.mean_squared_error(y_values, prediction))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_values, prediction)))
