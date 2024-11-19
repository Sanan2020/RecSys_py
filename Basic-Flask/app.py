from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# API Endpoint สำหรับดึงข้อมูลหนังทั้งหมด
@app.route('/')
def index():
    try:
        # โหลดข้อมูลจากไฟล์ Excel
       # df = pd.read_excel('Basic-Flask/movies.xlsx', sheet_name='movies')
      #  df_limited = df.head(100)  # ใช้ .head() เพื่อเลือกจำนวนแถวที่ต้องการ
        # แปลง DataFrame เป็น dictionary
      #  movies = df_limited.to_dict(orient='records')  # 'records' ทำให้แต่ละแถวกลายเป็น dict
        
        # โหลดข้อมูลจากไฟล์ CSV
        df2 = pd.read_csv('Basic-Flask/ratings.csv')
        
        # ส่งคืนข้อมูลในรูปแบบ JSON
        return render_template("index4.html", movies=movies)
    except Exception as e:
        return ({"error ex": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
