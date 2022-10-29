from traceback import TracebackException
from twill.commands import *
from bs4 import BeautifulSoup
import time
import mysql.connector
from mysql.connector import errorcode


instance = 1
while True:
    try:

        fu = 0
        heutesame = False
        morgensame = False

        while True:
            try:
                startT = time.time()
                go('https://whg.ms.de')
                try:
                    fv("1", "_username", "vorname.nachname")
                    fv("1", "_password", "PaSswoRt123")
                    submit()
                except Exception as e:
                    print("---Already logged in---")
                go('https://whg.ms.de/iserv/infodisplay/file/151/infodisplay/0/infoUpload/vertrSuSIserv/heute/subst_001.htm')
                try:
                    fv("1", "_username", "vorname.nachname")
                    fv("1", "_password", "PaSswoRt123")
                    submit()
                except Exception as e:
                    print("---Already logged in---")
                with open("/path/to/heute.html", "w", encoding="utf-8") as f:
                    f.write(show())
                go('https://whg.ms.de/iserv/infodisplay/file/151/infodisplay/0/infoUpload/vertrSuSIserv/heute+1/subst_001.htm')
                try:
                    fv("1", "_username", "vorname.nachname")
                    fv("1", "_password", "PaSswoRt123")
                    submit()
                except Exception as e:
                    print("---Already logged in---")
                with open("/path/to/morgen.html", "w", encoding="utf-8") as f:
                    f.write(show())
                
                #####
                
                tage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]
                spalten = ["Klassen","Stunden","Fach","Raum","Art","Text"]
                
                try:
                    db = mysql.connector.connect(
                        host="mysql.server.url",
                        user="username",
                        password="PaSswoRt123",
                        database="databasename"
                    )
                    print("---Verbunden---")
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Anmeldedaten falsch")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Datenbank nicht da")
                    else:
                        print(err)
                cursor = db.cursor()
                for tag in tage:
                    cursor.execute("DELETE FROM " + tag)
                
                with open("/path/to/heute.html") as heute:
                    soup = BeautifulSoup(heute, "lxml")
                zeile = 0
                for tr in soup.find_all("tr", class_="list".split()):
                    if zeile > 0:
                        spalte = 0
                        values = ["","","","","",""]
                        for td in tr.contents:
                            content = td.get_text()
                            values[spalte] = content
                            spalte += 1
                        #cursor.execute()
                    zeile += 1
                
                db.close()
                
                #####
                
                endT = time.time()
                timeTook = endT - startT
                waitTime = 10 - timeTook
                waitTime = max(0, waitTime)
                time.sleep(waitTime)
                fu = 0
            except Exception as e:
                print("---Program fucked up---")
                #time.sleep(30)
                fu += 1
                if fu > 30:
                    print("---Too many errors---")
                    break
    except Exception as e:
        instance += 1
        print("""
              #######################
              #######################
              #######################
              #######################
              #######################
              Running again... (Instance """ + str(instance) + """)
              #######################
              #######################
              #######################
              #######################
              #######################""")
