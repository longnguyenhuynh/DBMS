### Mô tả
Ứng dụng hiển thị danh sách phim viết bằng Flask, sử dụng cơ sở dữ liệu từ trang themoviedb.org

### Tính năng
* Hiển thị danh sách các bộ phim
* Hỗ trợ tìm kiếm và xem đánh giá phim

### Yêu cầu
* python3.+ 
* PostgresSQL

### Cài đặt
* **Bước 1** : Cài đặt thư viện virtualenv để thiết lập môi trường ảo tránh làm ảnh hưởng tới những thư viện có sẵn trong máy
    * **`pip install virtualenv`**
    * **`virtualenv virtual`**
    * **`source virtual/bin/activate`**
* **Bước 2** : Cài đặt thư viện **`pip install -r requirements.txt`**
* **Bước 3** : Đăng ký tài khoản và tạo API key từ trang themoviedb.org và thay vào MOVIE_API_KEY trong run.sh (cho Linux)
* **Bước 4** : Khởi động postgresql **postgres**
    * Dùng lệnh **psql** để vào shell
    * Tạo một database tên **'watchlist'** bằng cách sử dụng lệnh **`CREATE DATABASE watchlist;`**
    * Đặt password **`ALTER USER <username> WITH PASSWORD "<new_password>";`**
    * Mở file **config.py**, đặt lại biến **SQLALCHEMY_DATABASE_URI** với định dạng sau:
    **`SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://<username>:<password>@localhost/watchlist"`**
* **Bước 5** : Nâng cấp database theo schema:
```
python manage.py db upgrade
```
* **Bước 6** : Chạy lệnh **`chmod +x run.sh`**
    * Chạy **`./start.sh`** 
    * Mở trình duyệt và truy cập đường dẫn **http://127.0.0.1:5000/**.
