from flask import Flask
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np

app = Flask(__name__)


class MySQLConnector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        self.server = server if server else "localhost"
        self.port = port if port else 3306
        self.database = database if database else "salesdatabase"
        self.username = username if username else "root"
        self.password = password if password else "1234"

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password
            )
            if conn.is_connected():
                print("Kết nối MySQL thành công!")
            return conn
        except mysql.connector.Error as e:
            print(f"Lỗi kết nối MySQL: {e}")
            return None


def queryDataset(conn, sql):
    if conn is None:
        print("Không có kết nối đến MySQL")
        return None
    cursor = conn.cursor()
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
    cursor.close()
    return df


# Khởi tạo đối tượng MySQLConnector và kết nối
db = MySQLConnector()
conn = db.connect()

sql1 = "SELECT * FROM customer"
df1 = queryDataset(conn, sql1)
print(df1)

sql2="select distinct customer.CustomerId, Age, Annual_Income, Spending_Score " \
     "from customer, customer_spend_score " \
     "where customer.CustomerId=customer_spend_score.CustomerID"

df2=queryDataset(conn,sql2)
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']

print(df2)

print(df2.head())

print(df2.describe())

def showHistogram(df,columns):
    plt.figure(1, figsize=(7,8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(3, 1, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.distplot(df[column], bins=32)
        plt.title(f'Histogram of {column}')
    plt.show()

showHistogram(df2,df2.columns[1:])

def elbowMethod(df,columnsForElbow):
    X = df.loc[:, columnsForElbow].values
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters = n,
                       init = 'k-means++',
                       max_iter = 500,
                       random_state = 42)
        model.fit(X)
        inertia.append(model.inertia_)

    plt.figure(1, figsize = (15,6))
    plt.plot(np.arange(1, 11), inertia, 'o')
    plt.plot(np.arange(1, 11), inertia, '-.', alpha = 0.5)
    plt.xlabel('Number of Clusters'), plt.ylabel('Cluster sum of squared distances')
    plt.show()

columns=['Age' , 'Spending Score']
elbowMethod(df2,columns)

def runKMeans(X,cluster):
    model = KMeans(n_clusters = cluster,
                   init = 'k-means++',
                   max_iter = 500,
                   random_state = 42)

    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)
    return y_kmeans,centroids,labels

X = df2.loc[:, columns].values
cluster=4
colors=["red","green","blue","purple","black","pink","orange"]

y_kmeans,centroids,labels=runKMeans(X,cluster)
print(y_kmeans)
print(centroids)
print(labels)

df2["cluster"]=labels

def visualizeKMeans(X,y_kmeans,cluster,title,xlabel,ylabel,colors):
    plt.figure(figsize=(10, 10))
    for i in range(cluster):
        plt.scatter(X[y_kmeans == i, 0],
                    X[y_kmeans == i, 1],
                    s=100,
                    c=colors[i],
                    label='Cluster %i'%(i+1))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

visualizeKMeans(X,
                y_kmeans,
                cluster,
                "Clusters of Customers - Age X Spending Score",
                "Age",
                "Spending Score",
                colors)

###Thực nghiệm gom cụm theo 2 cột khác: Cột Annual Income và Spending Score
columns = ['Annual Income', 'Spending Score']
elbowMethod(df2,columns)

X = df2.loc[:, columns].values
cluster=5

y_kmeans,centroids,labels=runKMeans(X,cluster)

print(y_kmeans)
print(centroids)
print(labels)

df2["cluster"]=labels
visualizeKMeans(X,
                y_kmeans,
                cluster,
                "Clusters of Customers - Annual Income X Spending Score",
                "Annual Income",
                "Spending Score",
                colors)


# Lấy danh sách khách hàng trong từng cụm
def getCustomersByCluster(conn, df, cluster_number):
    customer_ids = df[df["cluster"] == cluster_number]["CustomerId"].tolist()
    if not customer_ids:
        print(f"Không có khách hàng nào trong cụm {cluster_number}")
        return None

    customer_ids_str = ",".join(map(str, customer_ids))
    sql = f"SELECT * FROM customer WHERE CustomerId IN ({customer_ids_str})"

    df_cluster = queryDataset(conn, sql)

    print(f"\n--- Danh sách khách hàng trong cụm {cluster_number} ---")
    print(df_cluster)
    return df_cluster

getCustomersByCluster(conn, df2, 3)

###Thực nghiệm gom cụm theo 3 cột khác: Cột Age, Annual Income và Spending Score
columns = ['Age','Annual Income', 'Spending Score']
elbowMethod(df2,columns)

X = df2.loc[:, columns].values
cluster=6


y_kmeans,centroids,labels=runKMeans(X,cluster)

print(y_kmeans)
print(centroids)
print(labels)
df2["cluster"]=labels
print(df2)


def visualize3DKmeans(df, columns, hover_data, cluster):
    fig = px.scatter_3d(
        df,
        x=columns[0],
        y=columns[1],
        z=columns[2],
        color='cluster',
        hover_data=hover_data,
        category_orders={"cluster": range(0, cluster)},
    )

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()


hover_data=df2.columns
visualize3DKmeans(df2,columns,hover_data,cluster)


