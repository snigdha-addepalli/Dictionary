import json
from difflib import get_close_matches
from google_trans_new import google_translator as Translator
import tkinter as tk

translator=Translator()
data=json.load(open("data.json"))

def jsonmatches(w):
    w=w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes, or N if no: "%get_close_matches(w,data.keys())[0]).upper()

        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

root=tk.Tk()
root.geometry("900x375")

word=tk.StringVar()
word1=tk.StringVar()
word2=tk.StringVar()
word3=tk.StringVar()
word4=tk.StringVar()

def submit():
    definition.delete(0)
    word_val=word.get()
    translated_word_val=translator.translate(word_val)
    output=jsonmatches(translated_word_val)

    if type(output)==list:
        definition.insert(0,"\n".join(output))
    else:
        definition.insert(0,output)

name_label=tk.Label(root, text = 'Enter a word: ', font=('calibre',12))
name_entry=tk.Entry(root,textvariable = word, font=('calibre',12,'normal'))

name_label1=tk.Label(root, text = 'Enter a word: ', font=('calibre',12))
name_entry1=tk.Entry(root,textvariable = word1, font=('calibre',12,'normal'))

name_label2=tk.Label(root, text = 'Enter a word: ', font=('calibre',12))
name_entry2=tk.Entry(root,textvariable = word2, font=('calibre',12,'normal'))

name_label3=tk.Label(root, text = 'Enter a word: ', font=('calibre',12))
name_entry3=tk.Entry(root,textvariable = word3, font=('calibre',12,'normal'))

name_label4=tk.Label(root, text = 'Enter a word: ', font=('calibre',12))
name_entry4=tk.Entry(root,textvariable = word4, font=('calibre',12,'normal'))

definition_label=tk.Label(root, text="Its Meaning: ", font=('calibre',12))
definition=tk.Entry(root,width=80,font=('calibre',12,'normal'))

sub_btn=tk.Button(root,text = 'Submit',command=submit)

definition_label1=tk.Label(root, text="Its Meaning: ", font=('calibre',12))
definition1=tk.Entry(root,width=80,font=('calibre',12,'normal'))
sub_btn1=tk.Button(root,text = 'Submit',command=submit)

definition_label2=tk.Label(root, text="Its Meaning: ", font=('calibre',12))
definition2=tk.Entry(root,width=80,font=('calibre',12,'normal'))
sub_btn2=tk.Button(root,text = 'Submit',command=submit)

definition_label3=tk.Label(root, text="Its Meaning: ", font=('calibre',12))
definition3=tk.Entry(root,width=80,font=('calibre',12,'normal'))
sub_btn3=tk.Button(root,text = 'Submit',command=submit)

definition_label4=tk.Label(root, text="Its Meaning: ", font=('calibre',12))
definition4=tk.Entry(root,width=80,font=('calibre',12,'normal'))
sub_btn4=tk.Button(root,text = 'Submit',command=submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
definition_label.grid(row=1,column=0)
definition.grid(row=1,column=1)

sub_btn.grid(row=2,column=1)

name_label1.grid(row=3,column=0)
name_entry1.grid(row=3,column=1)
definition_label1.grid(row=4,column=0)
definition1.grid(row=4,column=1)

sub_btn1.grid(row=5,column=1)

name_label2.grid(row=6,column=0)
name_entry2.grid(row=6,column=1)
definition_label2.grid(row=7,column=0)
definition2.grid(row=7,column=1)

sub_btn2.grid(row=8,column=1)

name_label3.grid(row=9,column=0)
name_entry3.grid(row=9,column=1)
definition_label3.grid(row=10,column=0)
definition3.grid(row=10,column=1)

sub_btn3.grid(row=11,column=1)

name_label4.grid(row=12,column=0)
name_entry4.grid(row=12,column=1)
definition_label4.grid(row=13,column=0)
definition4.grid(row=13,column=1)

sub_btn4.grid(row=14,column=1)

root.mainloop()