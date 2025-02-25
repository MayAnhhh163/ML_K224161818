import sqlite3
import pandas as pd


def get_customers_with_invoices(database_path, min_invoices):
    """
    Trả về danh sách Customer có tham gia >= min_invoices.

    Args:
        database_path (str): Đường dẫn tới tệp SQLite database.
        min_invoices (int): Số lượng hóa đơn tối thiểu.

    Returns:
        pandas.DataFrame: Danh sách Customer đáp ứng điều kiện.
    """
    try:
        # Kết nối đến cơ sở dữ liệu
        sqlite_connection = sqlite3.connect(database_path)
        print("Kết nối CSDL thành công!")

        # Truy vấn dữ liệu
        query = f"""
        SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, COUNT(Invoice.InvoiceId) AS InvoiceCount
        FROM Customer
        JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId, Customer.FirstName, Customer.LastName
        HAVING InvoiceCount >= {min_invoices};
        """
        # Chuyển đổi kết quả truy vấn thành DataFrame
        df = pd.read_sql_query(query, sqlite_connection)
        #print(df)
        if df.empty:
            print("Không có khách hàng nào thỏa mãn điều kiện.")
        else:
            print("Dữ liệu truy vấn:")
            print(df)

    except sqlite3.Error as error:
        print("Đã xảy ra lỗi: ", error)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Đã đóng kết nối CSDL.')


result = get_customers_with_invoices(r'/\databases\Chinook_Sqlite.sqlite', 5)
print(result)