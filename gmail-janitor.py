from simplegmail import Gmail
from simplegmail.query import construct_query
import pandas as pd

gmail = Gmail()
labels = gmail.list_labels()

def getid(x):
    for l in labels:
        if x == l.name:
            return l.id

xls = pd.ExcelFile(r'./Filters.xlsx')
df_sender = pd.read_excel(xls, 'Sender')
df_word = pd.read_excel(xls, 'Word')

df_word.rename(columns={"Key Word (separate by \",\" and keep lowercase)":"Word", "Mark as Read? (Yes, No)":"Read", "If Delete, select # of days, or select 0":"Days"}, inplace = True)

df_word["Word"] = df_word["Word"].str.split(', ')
df_word = df_word.explode("Word")

df_word["id"] = df_word.apply(lambda real_id: getid(real_id[("Label")]),axis=1)

df_sender.rename(columns={"<Sender> (separate by \",\")":"Sender", "Mark as Read? (Yes, No)":"Read", "If Delete, select # of days, or select 0":"Days"}, inplace = True)

df_sender["Sender"] = df_sender["Sender"].str.split(', ')
df_sender = df_sender.explode("Sender")

df_sender["id"] = df_sender.apply(lambda real_id: getid(real_id[("Label")]),axis=1)

messages = gmail.get_unread_inbox()

for message in messages:
    #print(message.plain)
    def process_word(word_email):
        search_text = message.html
        if message.html == None:
            search_text = message.snippet
        #print(message.plain)
        if word_email["Word"] not in search_text.lower():
            return
        if word_email["Read"] == "Yes":
            message.mark_as_read()
        if word_email["Word"] in search_text.lower():
            message.modify_labels(to_add=word_email["id"], to_remove='INBOX') 
    df_word.apply(process_word,axis=1)

messages = gmail.get_unread_inbox()

for message in messages:
    def process_email(single_email):
        #print(message.sender)
        if single_email["Sender"] not in message.sender:
            return
        if single_email["Read"] == "Yes":
            message.mark_as_read()
        if single_email["Sender"] in message.sender:
            message.modify_labels(to_add=single_email["id"], to_remove='INBOX')
    df_sender.apply(process_email,axis=1)

df_delete_sender = pd.read_excel(xls, 'Sender')
df_delete_word = pd.read_excel(xls, 'Word')
df_delete_sender.rename(columns={"<Sender> (separate by \",\")":"Sender", "Mark as Read? (Yes, No)":"Read", "If Delete, select # of days, or select 0":"Days"}, inplace = True)
df_delete_word.rename(columns={"Key Word (separate by \",\" and keep lowercase)":"Word", "Mark as Read? (Yes, No)":"Read", "If Delete, select # of days, or select 0":"Days"}, inplace = True)
df_delete_sender.drop(columns=["Sender","Read"],axis=1,inplace=True)
df_delete_word.drop(columns=["Word","Read"],axis=1,inplace=True)

#print(df_delete_sender)
#print(df_delete_word)

for i in range(len(df_delete_sender)):
    if df_delete_sender.iloc[i,1]>0:
        #print(df_delete_sender.iloc[i,1])
        query_params = {
            "older_than": (df_delete_sender.iloc[i,1], "day"),
            "labels":[[df_delete_sender.iloc[i,0]]]
            }
        filtered_messages = gmail.get_messages(query=construct_query(query_params))
        #print(filtered_messages)
        for message in filtered_messages:
            message.trash()

for i in range(len(df_delete_word)):
    if df_delete_word.iloc[i,1]>0:
        #print(df_delete_sender.iloc[i,1])
        query_params = {
            "older_than": (df_delete_word.iloc[i,1], "day"),
            "labels":[[df_delete_word.iloc[i,0]]]
            }
        filtered_messages = gmail.get_messages(query=construct_query(query_params))
        #print(filtered_messages)
        for message in filtered_messages:
            message.trash()