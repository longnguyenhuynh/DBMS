### Mô tả
Ứng dụng hiển thị danh sách phim viết bằng Flask
### Tính năng
* Hiển thị danh sách các bộ phim
* Hỗ trợ tìm kiếm và xem thông tin diễn viên, các bộ phim liên quan

### Yêu cầu
* python3.+ 
* PostgresSQL

### Cài đặt
* **Bước 1** : Cài đặt thư viện virtualenv để thiết lập môi trường ảo tránh làm ảnh hưởng tới những thư viện có sẵn trong máy
    * **`pip install virtualenv`**
    * **`virtualenv virtual`**
    * **`source virtual/bin/activate`**
* **Bước 2** : Cài đặt thư viện **`pip install -r requirements.txt`**
* **Bước 3** : Khởi động Neo4j Server (http://neo4j.com/download[Download & Install])
    * Mở http://localhost:7474[Neo4j Browser]
    * Cài bộ dữ liệu Movies bằng lệnh `:play movies`
    * Bấm nút `Run`
* **Bước 4** : Khỏi tạo web server:
```
python movies.py
```
* **Bước 5** : Mở trình duyệt và truy cập đường dẫn **http://127.0.0.1:8080/**.
