import xlsxwriter
import re

# workbook = xlsxwriter.Workbook('gcmsgs.xlsx')

def allgchistory(sk, gcid):
    
    workbook = getworkbook() #workbook
    
    ln = len(gcid)
    history = True
    
    for x in gcid:
        if ln <= 0:
            workbook.close()
            history = False
            print("Group chat history successfully extracted.")
            break
        else:
            ln-=1
        
        if re.findall('19', x):
            ch = sk.chats.chat(x)
            
            cleanString = re.sub('\W+', ' ', gcid[x].topic) #remove special characters
            msg(cleanString)
            worksheet = workbook.add_worksheet(cleanString)

            getMsgs(ch ,sk, worksheet, history)            

    workbook.close()


def removeHtmlTag(raw_txt):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_txt)
    return cleantext.strip()


def singlegchistory(sk, gcid, id):
    
    workbook = getworkbook() #generate workbook
    
    ch = sk.chats.chat(id)    
    history = True    
    sheetname = gcid[id.strip()].topic
    cleanString = re.sub('\W+', ' ', sheetname) 
    worksheet = workbook.add_worksheet(cleanString)
    msg(cleanString)
    
    getMsgs(ch,sk, worksheet, history)               

    workbook.close()


def getworkbook():
    filename = input("Enter File name: ")
    workbook = xlsxwriter.Workbook(filename + '.xlsx')
    return workbook


def getMsgs(ch,sk, worksheet, history):
    from animatecursor import CursorAnimation
    spin = CursorAnimation()
    spin.start()

    col = 0
    row = 0
    outer = False    
    
    while history:
        
        gcmsgs = ch.getMsgs()
        
        for ms in gcmsgs:

            if re.findall('HistoryDisclosedUpdate', ms.type): # 
                print(ms.type)
                print(ms.history)
                history = False                
                outer = ms.history
                
                break

            else:
                if sk.contacts[ms.userId]:
                    worksheet.write(row, col, str(ms.time))
                    worksheet.write(row, col + 1, sk.contacts[ms.userId].name.first)
                    worksheet.write(row, col + 2, removeHtmlTag(ms.content))
                    row += 1                                           
                    
        if outer:   
            spin.stop()        
            break            


def msg(cleanString):    
    print(f"Extracting: {cleanString} Chat History...")
    






# col = 0
            # row = 0

            # while history:

            #     gcmsgs = ch.getMsgs()

            #     for ms in gcmsgs:

            #         if re.findall('HistoryDisclosedUpdate', ms.type): # 
            #             print(ms.type)
            #             print(ms.history)
            #             # history = False
            #             outer = ms.history
            #             break

            #         else:
            #             if sk.contacts[ms.userId]:
            #                 worksheet.write(row, col, str(ms.time))
            #                 worksheet.write(row, col + 1, sk.contacts[ms.userId].name.first)
            #                 worksheet.write(row, col + 2, removeHtmlTag(ms.content))
            #                 row += 1
            #     if outer:
            #         break

