import re
import requests
from bs4 import BeautifulSoup as bs

headers = {

"authority": "www.realtor.com",
"method": "GET",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"cookie": '''split=n; split_tcv=192; __vst=d5167bc1-5f92-434f-a380-21f3833696dc; permutive-id=a9bde4b1-1b07-4841-8fa7-349520772cec; _gcl_au=1.1.1835334503.1644064469; G_ENABLED_IDPS=google; __gads=ID=d8bf8837123e5ade:T=1644064470:S=ALNI_MY5IDthRpUq9AXWjrGU7_60VkTRIA; ajs_anonymous_id=%22d0b5c2ec-6385-43dc-a399-5a7c5118b5ad%22; _fbp=fb.1.1644064471159.845719435; _ga=GA1.2.676143506.1644064470; s_ecid=MCMID%7C45933460820227988632129314995161776028; _ncg_id_=9ac91f45-3089-488c-804d-ef610b1fd55b; __qca=P0-102178196-1644064475418; _pxvid=5a080029-8680-11ec-9349-6b6673417244; _ncg_g_id_=d01cc2a5-f595-4f0b-96d1-7e63d489b520; _ta=us~1~c633ec0672eeb80ac2319af62d9003ff; _tac=false~google|not-available; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; CSAT_RENTALS=true; QSI_SI_2lgRMi8TnPPfroO_intercept=true; g_state={"i_p":1644904511431,"i_l":3}; cto_bundle=orvkfF9KMnA1a2R2eEMlMkJwT1p5VnpXUmY4b0RhcE9SRiUyQklSdGc2ZFp5Rk5DdXYwVHBiSXNTSUVuendKRkZta1RXc1F6QnVyeEwyRVdtR1UyN0NhRzdrVFA0aWxvVVZtalBZS3JERWJrWDIlMkZ6VXBhYUdrNW5BWDBzVjhaZ1hmdGVnUWMyUGVqbCUyRkFzTnBHQWRMeHZQJTJGN0x1MkVBJTNEJTNE; __ssn=7e3479c1-7e65-4341-ac04-e5a97cb46ff1; __ssnstarttime=1644601652; __split=16; _ncg_sp_ses.cc72=*; pxcts=b3ab0bf0-8b62-11ec-8f98-77d04bf7adfe; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19035%7CMCMID%7C45933460820227988632129314995161776028%7CMCAAMLH-1645206459%7C3%7CMCAAMB-1645206459%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1644608859s%7CNONE%7CMCSYNCSOP%7C411-19036%7CMCAID%7CNONE%7CvVersion%7C5.2.0; AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=1; AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCMID%7C45933460820227988632129314995161776028%7CMCIDTS%7C19035%7CMCOPTOUT-1644608859s%7CNONE%7CvVersion%7C5.2.0; _tas=i5jyhkkvfcm; _gid=GA1.2.606075142.1644601660; _pxff_bdd=2000; _pxff_cde=5,10; QSI_HistorySession=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F2405-Ayers-Dr_Seguin_TX_78155_M97209-36537~1644601659768%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F3241-Starflower_New-Braunfels_TX_78130_M93521-96922~1644602283727%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F5115-Hornbeck-Hts_Converse_TX_78109_M93249-28039~1644602786723%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F133-Gatewood-Bay_Cibolo_TX_78108_M94743-09761~1644603242226; _ncg_sp_id.cc72=9ac91f45-3089-488c-804d-ef610b1fd55b.1644064473.8.1644603290.1644315000.6f87643f-cf30-4938-ae8a-d6a8c08f5d65; adcloud={%22_les_v%22:%22y%2Crealtor.com%2C1644605091%22}; _uetsid=b54ad1e08b6211eca4e47f7fe935fa48; _uetvid=f80145f0867f11ecbc76ed6ca3ff4591; _px3=379125272807b0973741421f28f6e6028f8a012e952c72e1dab3a04796cc7587:bA7/DcmNRp6/UHFcNNFpwUcTME2/W97iKC08RS6gMibDVHbv8U7LJmfgJUn5CA4IfdxRfAB8MxZRo/KwMIRUwA==:1000:cd8C2ExxfI+tYFIq/2WCxFN0ZCJ/JGxps5jv0PjtON/imuJWPrCGWyhlIob6etNFtLv5LkETByygfdYEjCssjreGS4tdp44dM4Mmlxb4RTi1UQE8eK/wV0QpFwOHHmaEbVpp7meg7lkKznqGBa/NA9R1ts4OQhe0qfFw2QMgRzFXdXgLLjbOMxGp4oQWLC6Z5zcX6udjnSU036fSfn0CZw==''',
"if-none-match": '''"3b58c-i0xp2bW1sajuk/SBEPOOM+2Tdto"''',
"sec-ch-ua": '''" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"''',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": '''"Windows"''',
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
main_list = []
list1 = ['https://www.realtor.com/realestateandhomes-detail/133-Gatewood-Bay_Cibolo_TX_78108_M94743-09761\n', 'https://www.realtor.com/realestateandhomes-detail/4902-Brookhead-Ln_Schertz_TX_78108_M95180-34264\n', 'https://www.realtor.com/realestateandhomes-detail/304-Longhorn-Way_Cibolo_TX_78108_M90515-76499\n', 'https://www.realtor.com/realestateandhomes-detail/5244-Brookline_Schertz_TX_78108_M95757-22055\n', 'https://www.realtor.com/realestateandhomes-detail/337-Cattle-Run_Cibolo_TX_78108_M90709-41558\n', 'https://www.realtor.com/realestateandhomes-detail/228-Cloud-Xing_Cibolo_TX_78108_M90089-01934\n', 'https://www.realtor.com/realestateandhomes-detail/520-Saddle-Back-Trl_Cibolo_TX_78108_M98329-00383\n', 'https://www.realtor.com/realestateandhomes-detail/213-Gatewood-Trce_Cibolo_TX_78108_M99376-02133\n', 'https://www.realtor.com/realestateandhomes-detail/117-Steer-Ln_Cibolo_TX_78108_M97805-85853\n', 'https://www.realtor.com/realestateandhomes-detail/216-Dove-Hl_Cibolo_TX_78108_M91142-98647\n', 'https://www.realtor.com/realestateandhomes-detail/1206-Haeckerville-Rd-2_Cibolo_TX_78108_M77168-99430\n', 'https://www.realtor.com/realestateandhomes-detail/217-Albarella_Cibolo_TX_78108_M91808-08298\n', 'https://www.realtor.com/realestateandhomes-detail/309-Lancer-Hl_Cibolo_TX_78108_M91008-95525\n', 'https://www.realtor.com/realestateandhomes-detail/141-Springtree-Bnd_Cibolo_TX_78108_M91634-25900\n', 'https://www.realtor.com/realestateandhomes-detail/309-Washta-Riv_Schertz_TX_78108_M96834-49465\n', 'https://www.realtor.com/realestateandhomes-detail/1206-Haeckerville-Rd-1_Cibolo_TX_78108_M77169-36696\n', 'https://www.realtor.com/realestateandhomes-detail/114-Indian-Blanket-St_Cibolo_TX_78108_M94423-52925']





#li = "https://www.realtor.com/realestateandhomes-detail/731-F-St_West-Sacramento_CA_95605_M91240-76209"

for li in list1:
    li1 = li.replace("\n","")
    r = requests.get(li1, headers=headers)
    #print(r.content)
    soup = bs(r.content, "html5lib")

    try:
        rent = soup.find("div", {"class": "rui__sc-62xokl-0 dgVFTR heading"})
        real_rent = str(rent.text)
        main_list.append(real_rent)
    except:
        main_list.append("None")

    try:
        beds = soup.find("li", {"data-testid": "property-meta-beds"})
        real_beds = str(beds.text)
        main_list.append(real_beds)
    except:
        main_list.append("None")

    try:
        baths = soup.find("li", {"data-testid": "property-meta-baths"})
        real_baths = str(baths.text)
        main_list.append(real_baths)
    except:
        main_list.append("None")

    try:
        area = re.findall(r'''data-testid="screen-reader-value">(.*?) square feet<''', str(r.text))
        real_area = str(area[0])
        main_list.append(real_area)
    except:
        main_list.append("None")

    try:
        address = soup.find("p", {"class": "rui__ygf76n-0 hLSoqa rui__sc-17fo6pt-0 kTsrsI address"})
        real_address = str(address.text)
        main_list.append(real_address)
    except:
        main_list.append("None")

    try:
        facts = soup.findAll("span", {"class": "fact-text-value"})
        for fact in facts:
            main_list.append(str(fact.text))
    except:
        for i in range(5):
            main_list.append("None")
    if len(facts) == 4:
        main_list.append("None")

    try:
        description = soup.find("div", {"class": "rui__ygf76n-0 bVPpjr rui__sc-1128a73-0 jrKGRL content-text"})
        real_description = description.text
        main_list.append(real_description)
    except:
        main_list.append("None")

    try:
        phone = soup.findAll("p", {"class": "rui__ygf76n-0 bVPpjr rui__sc-17fo6pt-0 kTsrsI"})
        real_phone = str(phone[1].text)
        if real_phone == "":
            main_list.append("None")
        else:
            main_list.append(real_phone)
    except:
        main_list.append("None")

    a = open("new.txt", "a", encoding="utf-8")
    for ma in main_list:
        a.write(ma + "**")

    a.write("\n")
    a.close()
    print(main_list)
    main_list.clear()



