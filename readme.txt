chạy myenv/scripts/activate.ps1
pip install -r requirements.txt
flask run 
################
NOTE
database k có khóa ngoại, chỉ có khóa chính 
khi query nhớ kiểm tra xem dữ liệu thõa mãn khóa phụ với mấy trường trong models 
(unique)