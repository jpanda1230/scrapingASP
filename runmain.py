from lxml import html
import requests
import time

search_words = ["OPENDOOR","OFFERPAD","SPH"]
loopnum = 0
for i in range(398900,400001):
    i_str = "{:07d}".format(i)
    print("Checking ID " + i_str)

    # open the Deed page and get the content
    url = "http://services.wakegov.com/realestate/Deeds.asp?id="+i_str
    page = requests.get(url)
    tree = html.fromstring(page.content)
    back1 = tree.xpath('//tr[@valign="top"]/td[2]/b/font/text()')

    if len(back1) <= 1:
        continue
    currentStr = '  ' + back1[1].strip()
    prewordSPH = currentStr[currentStr.find(str(search_words[2])) - 1:currentStr.find(str(search_words[2]))]
    backwordSPH=currentStr[currentStr.find(str(search_words[2])) + 3:currentStr.find(str(search_words[2])) + 4]
    if currentStr.find(str(search_words[0]))>1 or currentStr.find(str(search_words[1]))>1:
        print("Current field detected : " + currentStr + "\n")
        continue
    elif currentStr.find(str(search_words[2]))>1 and not((ord(prewordSPH)>=97 and ord(prewordSPH)<=122) or (ord(prewordSPH)>=65 and ord(prewordSPH)<=90)) \
            and not((ord(backwordSPH)>=97 and ord(backwordSPH)<=122) or (ord(backwordSPH)>=65 and ord(backwordSPH)<=90)):
        print("Current field detected : " + currentStr + "\n")
        continue
    else:
        for loopindex in range(2, len(back1)):
            detectedStr = '  ' + back1[loopindex].strip()
            prewordSPHOne = detectedStr[detectedStr.find(str(search_words[2])) - 1:detectedStr.find(str(search_words[2]))]
            backwordSPHOne = detectedStr[detectedStr.find(str(search_words[2])) + 3:detectedStr.find(str(search_words[2])) + 4]
            if detectedStr.find(str(search_words[0])) > 1 or detectedStr.find(str(search_words[1])) > 1 :
                f = open("matches.txt", "a")
                f.write(i_str + "   Detected Item: "+ detectedStr + "\n")
                #f.write(i_str + "\n")
                f.close()
                break
            elif detectedStr.find(str(search_words[2])) > 1 and not((ord(prewordSPHOne)>=97 and ord(prewordSPHOne)<=122) or (ord(prewordSPHOne)>=65 and ord(prewordSPHOne)<=90)) \
                    and not((ord(backwordSPHOne)>=97 and ord(backwordSPHOne)<=122) or (ord(backwordSPHOne)>=65 and ord(backwordSPHOne)<=90)):
                f = open("matches.txt", "a")
                f.write(i_str + "   Detected Item: " + detectedStr + "\n")
                # f.write(i_str + "\n")
                f.close()
                break
            else:
                continue





