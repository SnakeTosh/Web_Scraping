from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
from math import floor


def scrape(browser):
    sleep(2)
    #browser = webdriver.Chrome()
    #browser.get("https://www.larvf.com/domaine-de-l-abbaye-du-petit-quincy,10516,405537.asp")
    #browser.get("https://www.larvf.com/,domaine-de-l-abbaye-sainte-radegonde,10762,2015796.asp")
    producer = browser.find_element(By.XPATH, "//h1[@class='Title Title--article ArticleHeader-title']").text
    infos_1 = browser.find_elements(By.XPATH, "//div[@class='Article-meta']")
    infos_2 = browser.find_element(By.XPATH, "//div[@class='Article-textContainer Article-text']")
    infos_3 = infos_2.find_elements(By.XPATH, "//div[@class='ContactInformationsDataList']")

    dico = {'producer': producer}
    new_info = infos_1[0].text
    new_info = new_info.split('\n')
    #print(new_info)

    un = new_info[0]
    un = list(un)
    tour = 0
    for i in un:
        if i =='n':
            un.insert(tour+1,':')
            break
        tour+=1
    new_un = ''
    for i in un:
        new_un = new_un+i
    new_info[0] = new_un

    deux = new_info[1]
    deux = list(deux)
    tour = 0
    for i in deux:
        if i =='n':
            deux.insert(tour+1,':')
            break
        tour+=1
    new_deux = ''
    for i in deux:
        new_deux = new_deux+i
    new_info[1] = new_deux

    try :
        trois = new_info[2]
        trois = list(trois)
        tour = 0
        for i in trois:
            if i =='e':
                trois.insert(tour+1,':')
                break
            tour+=1
        new_trois = ''
        for i in trois:
            new_trois = new_trois+i
        new_info[2] = new_trois
    except Exception :
        pass


    for i in new_info:
        try:
            paire = i.split(':')
            dico[paire[0]]=paire[1]
        except Exception:
            pass

    all_p = browser.find_elements(By.CSS_SELECTOR, 'p')


    for i in all_p:
        if "Achat de raisin :" in i.text :
            p = i.text

    try :
        p = re.sub("\(.*?\)|\[.*?\]","",p)
    except Exception :
        pass


    new_p = p.split('\n')

    for i in new_p:
        duo = i.split(":")
        dico[duo[0]]=duo[1]

    try:
        surface = dico['Surface plantée ']
        surface = surface.split(' ')
        surface = surface[1]
        surface = float(surface)
        surface = floor(surface)
        dico['Surface plantée '] = surface
    except Exception:
        pass


    try :
        phone = infos_3[0].find_element(By.CLASS_NAME, "ContactInformationsDataListItem").text
        # phone = browser.find_element(By.CLASS_NAME, "ContactInformationsDataList").text
        phone = phone.split(":")
        dico[phone[0]] = phone[1]
        adress = infos_3[0].find_element(By.XPATH, "//div[@class='ContactInformationsDataList']").text
        adress = adress.split('\n')
        new_add = ''
        tour = 0
        for i in adress :
            if 'Tél' in i :
                    break
            else:
                new_add = new_add+' '+i
            tour +=1
        dico['Adresse']=new_add
    except Exception :
        pass

    modele = { 0 :'producer', 1 : 'Région', 2 :'Sous-région', 3 : 'Propriétaire', 4: 'Nombre de bouteilles par an ',
              5 : 'Surface plantée ', 6 : 'Mode de vendange ', 7: 'Âge moyen des vignes ', 8 : 'Cépages rouges ',
              9 : 'Cépages blancs ', 10 : 'Tél ', 11 : 'Adresse'}

    new_dic ={}
    cle = dico.keys()
    key_liste =[]
    for i in cle :
        key_liste.append(i)

    for i in modele.values():
        if i in key_liste :
            new_dic[i]=dico[i]
        else :
            new_dic[i] = ""

    # print(len(new_dic))
    # for i in new_dic.items():
    #     print(i)
    # print("")
    return new_dic


#scrape()


# ---------------------------------------------------------------------------------------------------------------------

#browser = webdriver.Chrome()
#browser.get("https://www.larvf.com/,georges-laval,10602,408117.asp")
#browser.get("https://www.larvf.com/,domaines-barons-de-rothschild-,12670,4407638.asp")
#browser.get("https://www.larvf.com/domaine-maurice-ecart,10592,405297.asp")
#browser.get("https://www.larvf.com/thomas-batardiere,4752394.asp")
# browser.get("https://www.larvf.com/domaine-des-echardiereres,10782,408056.asp")
# browser.maximize_window()
# browser.find_element(By.ID, 'didomi-notice-agree-button').click()
# sleep(2)

# x = 0
# # while True:
# #     x += 1
# #     browser.execute_script('scrollBy(0,300)')
# #     sleep(0.3)
# #     if x > 50:
# #         break
#
# #browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


# for i in liste_2 :
#     if i.text == 'Non' \
#     or i.text == 'Oui' :
#         continue
#     else :
#         result_2.append(i.text)

# try :
#     mail = infos_3[1].text
#     dico["mail"] = mail
# except Exception:
#     pass

# try :
#     mails = infos_3[1]
#     mail = mails.find_elements(By.XPATH, "//div[@class='ContactInformationsDataListItem']")
#     dico["mail"] = mail[1].text
# except Exception:
#     pass