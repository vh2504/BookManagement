from app import db
from app import login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import relationship, synonym

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     role = db.Column(db.String(24))
#     password= db.Column(db.String(128))

#     def __repr__(self):
#         return '<User> {}'.format(self.username)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#     def __repr__(self):
#         return '<Post> {}'.format(self.body)

# New KhachHang
class KhachHang(UserMixin, db.Model):
    MaKH = db.Column(db.Integer, primary_key=True,autoincrement=True)
    HoTen = db.Column(db.String(200))
    DiaChi = db.Column(db.String(200))
    SDT = db.Column(db.String(200))
    Email = db.Column(db.String(100))
    Username = db.Column(db.String(100),unique=True, nullable=False)
    _password = db.Column(db.String(100),nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        if password:
            password = password.strip()
            self._password = generate_password_hash(password)

    password_descriptor = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password_descriptor)

    def check_password(self, password):
        if self.password is None:
            return False
        password = password.strip()
        if not password:
            return False
        return check_password_hash(self.password, password)

    
    def __repr__(self):
        return ('<{self.__class__.__name__}: {self.MaKH}>'.format(self=self))        
@login.user_loader
def load_user(Username):
    return KhachHang.query.get(Username)


#Hoa Don
class HoaDon(UserMixin, db.Model):
    MaHoaDon = db.Column(db.Integer, primary_key=True,autoincrement=True)
    MaKH = db.Column(db.Integer)
    NgayMua = db.Column(db.DateTime, default=datetime.utcnow)
    damua = db.Column(db.Boolean, default=False)

#Sach
class Sach(UserMixin, db.Model):
    MaSach = db.Column(db.String(200), primary_key=True) 
    TenSach =  db.Column( db.String(200))
    SoLuong = db.Column(db.Integer)
    Gia = db.Column(db.Integer)
    MaLoai = db.Column( db.String(200))
    SoTap =  db.Column( db.String(200))
    Anh =  db.Column( db.String(200))
    NgayNhap =  db.Column( db.DateTime,default=datetime.utcnow)
    TacGia = db.Column( db.String(200))

#Loai
class Loai(UserMixin, db.Model):
    MaLoai = db.Column(db.String(200), primary_key=True) 
    TenLoai =  db.Column( db.String(200))

#Chi Tiet Hoa Don
class ChiTietHoaDon(UserMixin, db.Model):
    MaCTHD = db.Column(db.Integer, primary_key=True,autoincrement=True)  
    MaSach =db.Column(db.String(200))
    SoLuongMua = db.Column(db.Integer)
    MaHoaDon = db.Column(db.Integer)
    damua = db.Column(db.Boolean, default=False)

class DangNhap(UserMixin, db.Model):
    TenDangNhap = db.Column(db.String(200),primary_key=True)
    MatKhau = db.Column(db.String(200))
    Quyen = db.Column(db.Boolean, default=True)