import requests
import json
import mysql.connector

try: 
    mydb=mysql.connector.connect(host = 'localhost', user='root',password='',database='publicapidb')
except mysql.connector.Error as e:
    print("Mysql connecter error",e)

mycursor = mydb.cursor()

data = requests.get("https://api.publicapis.org/entries").text

data_info = json.loads(data)

for i in data_info['entries']:

    https = str(i['HTTPS'])
    sql = "INSERT INTO `publicapidata`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ('"+i['API']+"','"+i['Description']+"','"+i['Auth']+"','"+https+"','"+i['Cors']+"','"+i['Link']+"','"+i['Category']+"')"
    #sql = 'INSERT INTO `publicapidata`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ("'+i["API"]+'","'+i["Description"]+'","'+i["Auth"]+'","'+https+'","'+i["Cors"]+'","'+i["Link"]+'","'+i["Category"]+'")'
    mycursor.execute(sql)
    mydb.commit()
    print("Data inserted successfully, ", i['API'])