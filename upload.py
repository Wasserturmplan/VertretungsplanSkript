
from traceback import TracebackException
from twill.commands import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform
import webdriver_manager.chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


instance = 1
while True:
    try:

        d = webdriver.Chrome()
        d.set_window_size(800, 600)
        d.set_window_position(0, 0)

        fu = 0
        heutesame = False
        morgensame = False

        while True:
            try:
                #print("@@@@@@@@@@@@@@@1")
                startT = time.time()
                go('https://whg.ms.de')
                try:
                    fv("1", "_username", "vorname.nachname")
                    fv("1", "_password", "PaSswoRt123")
                    submit()
                except Exception as e:
                    print("---Already logged in---")
                #print("@@@@@@@@@@@@@@@2")
                go('https://whg.ms.de/iserv/infodisplay/file/151/infodisplay/0/infoUpload/vertrSuSIserv/heute/subst_001.htm')
                try:
                    fv("1", "_username", "vorname.nachname")
                    fv("1", "_password", "PaSswoRt123")
                    submit()
                except Exception as e:
                    print("---Already logged in---")
                #print("@@@@@@@@@@@@@@@3")
                with open("/path/to/heute.html", "w", encoding="utf-8") as f:
                    f.write(show())
                #print("@@@@@@@@@@@@@@@4")
                go('https://whg.ms.de/iserv/infodisplay/file/151/infodisplay/0/infoUpload/vertrSuSIserv/heute+1/subst_001.htm')
                try:
                    fv("1", "_username", "vorname.nachname")
                    fv("1", "_password", "PaSswoRt123")
                    submit()
                except Exception as e:
                    print("---Already logged in---")
                #print("@@@@@@@@@@@@@@@5")
                # print("1*")
                with open("/path/to/morgen.html", "w", encoding="utf-8") as f:
                    f.write(show())
                # print("2**")
                d.get("https://wasserturmplan.steffenmolitor.de/pypost.php")
                # print("3***")
                d.find_element(By.XPATH,"//input[@name='heute']").send_keys("/path/to/heute.html")
                # print("4****")
                d.find_element(By.XPATH,"//input[@name='morgen']").send_keys("/path/to/morgen.html")
                # print("5*****")
                d.find_element(By.XPATH,"//input[@name='go']").click()
                # print("6******")
                #print("@@@@@@@@@@@@@@@6")
                
                """


                #formfile("fileuploads", "heute", "heute.html")
                #formfile("fileuploads", "morgen", "morgen.html")
                #submit(0)
                mailsubj = ""
                mailcont = ""
                if not heutesame or not morgensame:
                    mailsubj = "Neue Änderungen im Vertretngsplan für "
                    mailcont = "Hallo du da!\nIch habe auf dem Vertretungsplan Änderungen für "
                    if not heutesame:
                        mailsubj += "Heute"
                        mailcont += "Heute"
                    if not heutesame and not morgensame:
                        mailsubj += " und "
                        mailcont += " und "
                    if not morgensame:
                        mailsubj += "Morgen"
                        mailcont += "Morgen"
                    mailcont += " registriert!\nUm zu erfahren, was sich geändert hat, klicke auf "
                    if not heutesame and not morgensame:
                        mailcont += "einen der beiden folgenden Links:\n"
                    else:
                        mailcont += "den folgenden Link:\n"
                    if not heutesame:
                        mailcont += "Heute: https://whg.ms.de/iserv/infodisplay/file/151/infodisplay/0/infoUpload/vertrSuSIserv/heute/subst_001.htm\n"
                    if not morgensame:
                        mailcont += "Morgen: https://whg.ms.de/iserv/infodisplay/file/151/infodisplay/0/infoUpload/vertrSuSIserv/heute+1/subst_001.htm\n"
                    mailcont += "Oder gucke direkt auf dem Wasserturmplan nach:\nhttps://wasserturmplan.steffenmolitor.de\n"
                    mailcont += "\nBeepBeepBoop viele Grüße von Steffens Vertretungsplan-Bot \n\n\nZum Deabbonieren eine Mail mit dem Betreff \"vp-stop\" an mich (vorname.nachname@whg.ms.de) senden und gerne den Grund in den Inhalt schreiben!"
                d.get("https://whg.ms.de/iserv/mail")
                try:
                    d.find_element_by_name("_username").send_keys("vorname.nachname")
                    d.find_element_by_name("_password").send_keys("PaSswoRt123")
                    d.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/form/div[3]/div[1]/button").click()
                except Exception as e:
                    print("---Already logged in---")
                time.sleep(3)
                if d.find_element_by_xpath("//*[@id='message-list-body']/tr[6]/td[6]").get_attribute("innerText") == "vp-abo":
                    d.find_element_by_xpath("//*[@id='message-list-body']/tr[6]/td[5]/a").click()
                    time.sleep(3)
                    newE = d.find_element_by_xpath("//*[@id='message-from']/span[2]/a/span[1]").get_attribute("innerText").split("<")[1].replace(">", "")
                    print("---Adding " + newE + "---")
                    with open("/path/to/mailList.txt", "r", encoding="utf-8") as l:
                        if not newE in l.read():
                            with open("/path/to/mailList.txt", "a", encoding="utf-8") as f:
                                f.write(newE + "\n")
                elif d.find_element_by_xpath("//*[@id='message-list-body']/tr[6]/td[6]").get_attribute("innerText") == "vp-stop":
                    d.find_element_by_xpath("//*[@id='message-list-body']/tr[6]/td[5]/a").click()
                    time.sleep(3)
                    remE = d.find_element_by_xpath("//*[@id='message-from']/span[2]/a/span[1]").get_attribute("innerText").split("<")[1].replace(">", "")
                    print("---Removing " + remE + "---")
                    list = ""
                    with open("/path/to/mailList.txt", "r", encoding="utf-8") as f:
                        list = f.read()
                    list = list.split("\n")
                    try:
                        list.remove(remE)
                    except Exception as e:
                        print("---" + remE + " not in list---")
                    list = "\n".join(list)
                    with open("/path/to/mailList.txt", "w", encoding="utf-8") as f:
                        f.write(list)
                with open("/path/to/mailList.txt", "r", encoding="utf-8") as f:
                    list = f.read()
                lista = list.split("\n")
                if mailsubj != "" and len(lista) > 0:
                    d.get("https://whg.ms.de/iserv/mail")
                    try:
                        d.find_element_by_name("_username").send_keys("vorname.nachname")
                        d.find_element_by_name("_password").send_keys("PaSswoRt123")
                        d.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/form/div[3]/div[1]/button").click()
                    except Exception as e:
                        print("---Already logged in---")
                    time.sleep(3)
                    d.find_element_by_id("mail-compose").click()
                    time.sleep(3)
                    try:
                        d.find_element_by_id("toggleRecipients").click()
                    except Exception as e:
                        print("---No button---")
                    for e in lista:
                        if e != "":
                            d.find_element_by_id("iserv_mail_compose_bcc-selectized").send_keys(e)
                            d.find_element_by_id("iserv_mail_compose_bcc-selectized").send_keys(Keys.ENTER)
                    d.find_element_by_id("iserv_mail_compose_subject").send_keys(mailsubj)
                    d.find_element_by_id("iserv_mail_compose_content").clear()
                    d.find_element_by_id("iserv_mail_compose_content").send_keys(mailcont)
                    d.find_element_by_id("iserv_mail_compose_actions_send").click()
                """

                endT = time.time()
                timeTook = endT - startT
                waitTime = 10 - timeTook
                waitTime = max(0, waitTime)
                time.sleep(waitTime)
                fu = 0
                #print("@@@@@@@@@@@@@@@7")
            except Exception as e:
                print("---Program fucked up---")
                fu += 1
                d.set_window_size(800, 600)
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
