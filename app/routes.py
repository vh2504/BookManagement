
from flask import Flask, render_template, redirect, request, session, sessions
import flask
from flask.helpers import flash
from flask import redirect
from flask_login.utils import login_required, logout_user
from sqlalchemy.sql.elements import Null
from werkzeug.local import F
from app import app
from app.models import Sach, db,DangNhap
from app.form import LoginForm, RegisterForm
from flask_login import login_user,current_user
from flask import request
from werkzeug.urls import url_parse
import os
from app.models import KhachHang

from flask import Flask, render_template, redirect, request, session


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/example')
def example():
    khachhang=[]
    for u in KhachHang.query.all():
        khachhang.append(u.Username)
  
    return render_template('example.html',KhachHang = khachhang)

@app.route('/register',methods=['Get','Post'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegisterForm()  
    if form.validate_on_submit():
        
        if form.password.data != form.passwordRepeat.data :
            flash('Password repeat is incorrect')
            return redirect('/register')
        
        if KhachHang.query.filter_by(username=form.username.data).first() is not None:
            flash('Username is exist ')
            return redirect('/register')
        u1=KhachHang(username=form.username.data,email=form.gmail.data,password=form.password.data)
        db.session.add(u1)
        db.session.commit()
        flash(f'Register of user {form.username.data}')
        login_user(u1)
        return redirect('/register')
    return render_template('register.html',title='Register',form=form)
@app.route('/logout',methods=['Get','Post'])
def logout(): 
    logout_user()
    return redirect('index')

######################################
@app.route('/admin')
@app.route('/adminlogin',methods=['Get','Post'])
def adminlogin(): 
    if session.get("TenDangNhap"):
        return redirect('/adminqlysach')
    if request.method == 'POST':
        TenDangNhap=request.form["TenDangNhap"]
        MatKhau = request.form["MatKhau"]
        admin = DangNhap.query.filter_by(TenDangNhap=TenDangNhap,MatKhau=MatKhau).first()
        if admin is not None:
            session["TenDangNhap"] = TenDangNhap
            return redirect('/adminqlysach')
        else:
            message = "Đăng nhập sai " + TenDangNhap
            session["message"] = message
            return render_template('adminlogin.html')
        
    else:
        return render_template('adminlogin.html')

@app.route('/logoutadmin')
def logoutadmin():
    session["TenDangNhap"]=None
    return redirect ('/admin')

@app.route('/adminqlysach',methods=['Get','Post'])
def adminqlysach():
    if session.get("TenDangNhap"):
        sach=db.session.query(Sach).all()
        #sua sach dang test
        if request.method == 'POST' and request.form.get("btnSua")!=Null:
            MaSach= request.form.get("MaSach")
            TenSach= request.form.get("TenSach")
            SoLuong= request.form.get("SoLuong")
            Gia= request.form.get("Gia")
            session["message"] = MaSach+"     "+TenSach+"     "+SoLuong+Gia
            
    
        return render_template('adminqlysach.html',sach=sach)
    else:
        return redirect('/admin')

    