from flask import Flask, request, render_template, session, redirect, app
import numpy as np
import pandas as pd
from libs.sorted_orders import find_and_sort_orders

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main():
    if "min_value" in request.form:
        min_value = float(request.form["min_value"])
        max_value = float(request.form["max_value"])
        sort_type = request.form.get("sort_type", "ascending") == "ascending"
        df = pd.read_csv(r'/\dataset\SalesTransactions.csv')
        result = find_and_sort_orders(df, min_value, max_value, sort_type)
        return render_template("orders_sort.html",  tables=[result.to_html(classes='data')], titles=result.columns.values)
    else:
        return render_template("orders_sort.html")
if __name__ =="__main__":
    app.run(host="localhost",port=9000,debug=True)
