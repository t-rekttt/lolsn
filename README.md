## Tool nhập code sinh nhật LOL 2021

![demo](https://user-images.githubusercontent.com/9071846/127822154-6bc58822-b073-4050-88a2-1bab5c0857df.jpg)

### Ưu điểm:
- Sử dụng API, không chiếm cửa sổ LOL
- Tự động extract token từ logs folder
- Người code đẹp trai
- Nhanh vcl

### Nhược điểm
- Đang tìm...

### Hướng dẫn sử dụng cho người lowtech
- Clone/download repo này
- Mở thư mục `dist`
- Mở file `lolsn.exe`
- Nếu thấy lỗi `The system cannot find the path specified...` thì sửa lại đường dẫn cho đúng với thư mục LOL và chạy lại

### Hướng dẫn sử dụng từ source
- Clone/download repo này
- Mở cmd/terminal, cd vào folder, chạy `pip install requests`
- Thay đường dẫn thư mục logs của LOL vào biến `logsPath` (hoặc để mặc định nếu bạn cài LOL ở ổ C:\Garena\...). Lưu ý dấu phân cách thư mục phải để là `\\`
- Thay đường dẫn file code ở dòng gán biến `codes` nếu cần
- Chạy `python lolsn.py`

### Lưu ý
- Chỉ chạy được max tới 500 bóng bay nên code sẽ break nếu như gặp giới hạn này
- Nếu bị lỗi `SERVER_ERROR` thì bạn thử xoá hết logs đi sau đó chạy lại client LOL 1 lần để token trong logs được cập nhật sau đó chạy lại tool
- File code mặc định được lấy từ https://github.com/HanaIroha/ToolSinhNhatLOL2021/blob/main/Toolcodell/bin/Release/code.txt. Hãy star repo đó nếu nó giúp ích cho bạn

### Nếu code chạy tốt, hãy
- Star repo này, follow Github
- Like bài viết
- Khen chủ thớt đẹp trai
