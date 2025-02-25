import pandas as pd

def find_orders_within_range(df, minValue, maxValue, sortType):
    # Tính tổng giá trị từng hóa đơn
    #order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    order_totals = df.groupby('OrderID')[['UnitPrice', 'Quantity', 'Discount']].apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())

    # lọc đơn hàng trong range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]

    # Chuyển thành DataFrame và sắp xếp theo `sortType`
    result = orders_within_range.reset_index(name='Sum').sort_values(by='Sum', ascending=sortType)
    return result

# Đọc dữ liệu
df = pd.read_csv(r'/\dataset\SalesTransactions.csv')

# Nhập giá trị min, max và kiểu sắp xếp
minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
sortType = input("Nhập kiểu sắp xếp (True: Tăng dần, False: Giảm dần): ").strip().lower() == 'true'

# Gọi hàm và hiển thị kết quả
result = find_orders_within_range(df, minValue, maxValue, sortType)
print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, ' là:')
print(result)
