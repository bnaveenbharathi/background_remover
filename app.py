from flask import Flask,render_template as render,request,redirect,url_for
from PIL import Image
from rembg import remove
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
#uploadfolder
upload_folder=os.path.join('static','uploads')
upload_folder2=os.path.join('static','removed')

#Database Connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=''
app.config["MYSQL_DB"]='bgremover'
app.config["MYSQL_CURSORCLASS"]='DictCursor'
mysql=MySQL(app)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        file=request.files["img"]
        if file:
            filename=secure_filename(file.filename)
            img_path=os.path.join(upload_folder,filename)
            file.save(img_path)
            #bgremove
            inputimg=Image.open(img_path)
            removebg=remove(inputimg)
            bgrm_img=os.path.join(upload_folder2,'image.png')
            #Database save the path
            con=mysql.connection.cursor()
            sql="INSERT INTO path (beforeimg_path,removeimg_path) values (%s,%s)"
            con.execute(sql,(img_path,bgrm_img))
            mysql.connection.commit()
            con.close()
            conremove=removebg.convert("RGBA")
            conremove.save(bgrm_img) #removeimg save
            return redirect(url_for('home'))
    #fetch the images using path
    con=mysql.connection.cursor()
    sql="SELECT * FROM path ORDER BY recent_date DESC"
    con.execute(sql)
    imgpaths=con.fetchall()   
    con.close()    
    return render('index.html',path=imgpaths)

if __name__=="__main__":
    app.run(debug=True)

