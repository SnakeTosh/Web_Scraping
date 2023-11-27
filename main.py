import yaml
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from test import scrape
import pandas as pd

browser = webdriver.Chrome()
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#alph = ["a"]
all_dic = []

for letter in alpha :
    browser.get(f"https://www.larvf.com/domaines/alpha/{letter}")
    browser.maximize_window()
    original_window = browser.current_window_handle

    liste = browser.find_elements(By.XPATH, "//a[@class='DomainList-domainLink']")
    browser.find_element(By.ID, 'didomi-notice-agree-button').click()

    tour = 0

    for i in range(0,len(liste)+1) :
        if tour == 3 :
            break
        liste[tour].click()
        sleep(2)

        result = scrape(browser)
        all_dic.append(result)

        browser.back()
        sleep(2)
        liste = browser.find_elements(By.XPATH, "//a[@class='DomainList-domainLink']")
        tour += 1


browser.close()

df = pd.DataFrame(all_dic, columns=['producer', 'Région', 'Sous-région', 'Propriétaire', 'Nombre de bouteilles par an ',
                                    'Surface plantée ', 'Mode de vendange ', 'Âge moyen des vignes ', 'Cépages rouges ',
                                    'Cépages blancs ', 'Tél ', 'Adresse'])

df.head()
df.to_sql('fichier_uptowork.sql',index=False, encoding='utf-8')