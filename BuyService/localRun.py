from startup import *

if __name__ == "__main__":
    path = r'C:\Workspace\cert\www.iisheep.com\Apache'
    app.run(debug=True,host='0.0.0.0',port=443,ssl_context=(path+r'\2_www.iisheep.com.crt', path+r'\3_www.iisheep.com.key'))