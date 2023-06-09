from tqdm import tqdm
import pandas as pd
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions
from selenium.common.exceptions import TimeoutException

df1 = pd.read_csv("cosmetic.csv")
df2 = pd.read_csv("cosmetic_TSNE.csv")
df3 = pd.read_csv("cosmetic_p.csv")
df_list = [df1, df2, df3]
df = pd.concat(df_list)
df = df[df['URL'].notna()]

df_urls = df["URL"].to_list()

options = ChromeOptions()
options.add_argument('--lang=en')

driver = uc.Chrome(
    options=options, driver_executable_path=r"C:\Users\MY-PC\Downloads\Compressed\chromedriver.exe")

img_list = []

for url in df_urls:
    print(url)
    try:
        driver.get(url)
        img = driver.find_elements(
            By.CSS_SELECTOR, "body > div:nth-child(3) > main > div:nth-child(1) > div.css-1v7u6og.eanm77i0 > div.css-v7bl16 > div.css-1a2dflv.eanm77i0 > div:nth-child(1) > div:nth-child(2) > div > ul > li:nth-child(1) > button > svg > foreignObject > img")
        if len(img) == 0:
            img_list.append("None")
        else:
            for i in img:
                img_list.append(i.get_attribute("src"))
    except TimeoutException:
        img_list.append("None")

a = {"img_source": img_list}
a_df = pd.DataFrame(a)
a_df.to_csv("img_source.csv")
print(len(img_list))
