# PardisBook | پردیس‌بوک

سامانه مدیریت کتابخانه با Django و PostgreSQL.

## امکانات برنامه‌ریزی‌شده
- صفحه اصلی و جست‌وجوی کتاب‌ها
- فهرست و جزئیات کتاب‌ها
- ثبت‌نام و ورود اعضا
- پنل عضو و ثبت درخواست امانت
- پنل مدیریت از طریق Django Admin

## راه‌اندازی در Windows / VS Code

### 1. محیط مجازی
```powershell
py -m venv venv
.env\Scripts\Activate.ps1
```

### 2. نصب وابستگی‌ها
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. تنظیم متغیرهای محیطی
در PowerShell:
```powershell
Copy-Item .env.example .env
```
سپس فایل `.env` را باز کنید و `DB_PASSWORD` و `SECRET_KEY` را با مقادیر واقعی خودتان جایگزین کنید.

### 4. ایجاد دیتابیس PostgreSQL
در pgAdmin یک دیتابیس با نام `library_db` ایجاد کنید. اگر نام کاربری یا رمز PostgreSQL شما متفاوت است، فایل `.env` را مطابق آن تغییر دهید.

### 5. اجرای مهاجرت‌ها و سرور
```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
سپس به `http://127.0.0.1:8000/` بروید.

## Git و GitHub
این پروژه از ابتدا با `git init -b main` مقداردهی اولیه شده است. `.env`، محیط مجازی، فایل‌های ویرایشگر و دیتابیس محلی در Git نادیده گرفته می‌شوند.

برای اتصال به مخزن GitHub خودتان:
```powershell
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
مقادیر `YOUR-USERNAME` و `YOUR-REPOSITORY` را با اطلاعات واقعی مخزن خود جایگزین کنید.

اگر مخزن GitHub از قبل README یا commit دارد، قبل از push وضعیت را بررسی کنید تا تاریخچه‌ها با هم تداخل نکنند.
