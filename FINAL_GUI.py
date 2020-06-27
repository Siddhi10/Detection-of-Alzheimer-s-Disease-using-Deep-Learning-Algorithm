from tkinter import *
import tkinter as tk
#import score
#import score
#import sqlite3 as db
#from Q_AD1 import yoo1
#from show import hi
import numpy as np
import pandas as pd 
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os
import cv2
import pickle
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
import shutil
from tkinter import filedialog
from PIL import ImageTk, Image

def file1():
    root=Tk()         
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpeg files","*.jpg"),("all files","*.*")) )
    return filename
    root.mainloop()
def file2():
    file_name= file1()
    return file_name

def model():
    FAST_RUN = False
    IMAGE_WIDTH=128
    IMAGE_HEIGHT=128
    IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
    IMAGE_CHANNELS=2
    
    filenames = os.listdir("train1")
    categories = []
    for filename in filenames:
        category = filename.split('_GM')[0]
        if category == 'AD':
            categories.append(1)
        else:
            categories.append(0)
                
                #print(categories[0:60])
                
    df = pd.DataFrame({'filename': filenames,'category': categories})
    #print(df.head())
    #print(df.tail())
    #df['category'].value_counts().plot.bar()
        
    #sample = random.choice(filenames)
    #image = load_img('train/'+sample)
    #plt.imshow(image)
        
    df["category"] = df["category"].replace({0: 'CN', 1: 'AD'}) 
    #print(df.head())
    #print(df.tail())
    
    train_df, validate_df = train_test_split(df, test_size=0.20, random_state=42)
    train_df = train_df.reset_index(drop=True)
    validate_df = validate_df.reset_index(drop=True)
    
    total_train = train_df.shape[0]
    total_validate = validate_df.shape[0]
    batch_size=15
    
    test_filenames = os.listdir("train1")
    test_df = pd.DataFrame({
            'filename': test_filenames
            })
    nb_samples = test_df.shape[0]
    #print(nb_samples)
    
    test_gen = ImageDataGenerator(rescale=1./255)
    test_generator = test_gen.flow_from_dataframe(
            test_df, 
            "train1", 
            x_col='filename',
            y_col=None,
            class_mode=None,
            target_size=IMAGE_SIZE,
            batch_size=batch_size,
            shuffle=False
            )
    
    
    f=open('predict_model.pkl','rb')
    classify=pickle.load(f)
    prediction=classify.predict_generator(test_generator, steps=np.ceil(nb_samples/batch_size))
    #print(prediction)
    
    train_datagen = ImageDataGenerator(
            rotation_range=15,
            rescale=1./255,
            shear_range=0.1,
            zoom_range=0.2,
            horizontal_flip=True,
            width_shift_range=0.1,
            height_shift_range=0.1
            )
    
    train_generator = train_datagen.flow_from_dataframe(
            train_df, 
            "train1", 
            x_col='filename',
            y_col='category',
            target_size=IMAGE_SIZE,
            class_mode='categorical',
            batch_size=batch_size
            )
    
    test_df['category'] = np.argmax(prediction, axis=-1)
    
    label_map = dict((v,k) for k,v in train_generator.class_indices.items())
    test_df['category'] = test_df['category'].replace(label_map)
    #test_df['category'] = test_df['category'].replace({ 'AD': 1, 'CN': 0 }
    
    sample_test = test_df.head(18)
    sample_test.head()
    plt.figure(figsize=(12, 24))
    for index, row in sample_test.iterrows():
        filename = row['filename']
        category = row['category']
        img = load_img("train1/"+filename, target_size=IMAGE_SIZE)
        #img = load_img("", target_size=IMAGE_SIZE)
        plt.subplot(6, 3, index+1)
        plt.imshow(img)
        plt.xlabel(filename + '(' + "{}".format(category) + ')' )
        plt.tight_layout()
        plt.show()
def run2():
    root = tk.Tk()
    root.geometry('1000x600')
    root.title("AD Detection System")

    path='coolbrain1.jpg'

    canvas=tk.Canvas(root, height=600, width=1000)
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image = img)
    panel.place(x=0, y=0)
    canvas.pack()


    #button = tk.Button(root, text = "Browse A File")
    #button.place(x=80, y=150)

    
        
    #button = tk.Button(root, text = "UPLOAD", command=model.path)
    #button.place(x=80, y=250)
        
    button = tk.Button(root, text = "PREDICT",font=("bold", 13), bg='brown',fg='white',height=4, width=10, command=model)
    button.place(x=80, y=250)
    

    a=file2()
    label = tk.Label(root, text = "",font=("bold", 20),bg="gray6", fg="white")
    label.configure(text = a)
    label.place(x=80, y=150) 
    
    
    newPath = shutil.copy(a, 'train1')
    
    root.mainloop()
def run1():
    os.system('python score.py')


def run():
    
    root = tk.Tk()
    root.geometry('1000x600')
    root.title("AD Detection System")
    
    path='coolbrain1.jpg'
    
    canvas=tk.Canvas(root, height=600, width=1000)
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image = img)
    panel.place(x=0, y=0)
    canvas.pack()
    
    
    #Name=StringVar()
    #Email=StringVar()
    #c=StringVar()
#Height=StringVar()
#Weight=StringVar()
#Number=StringVar()

#def database():
 #  n=Name.get()
  # d=m.get()
  # g=var.get()
   #h=Height.get()
   #w=Weight.get()
   #n=Number.get()
   #e=Email.get()
   #conn = sqlite3.connect('Form.db')
   #with conn:
    #  cursor=conn.cursor()
   #cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,DOB TEXT,Gender TEXT,Height INTEGER,Weight INTEGER,Number TEXT, Email TEXT)')
   #cursor.execute('INSERT INTO Student (Name,DOB,Gender,Height,Weight,Number,Email) VALUES(?,?,?,?,?,?,?)',(n,d,g,h,w,n,e,))
   #conn.commit()

    label_0 = Label(root, text="General Patient Information",borderwidth="1",width=22,font=("bold", 20),bg="gray6", fg="white")
    label_0.place(x=150,y=53)
    
    
    label_1 = Label(root, text="Name",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_1.place(x=80,y=130)
    
    entry_1 = Entry(root)
    entry_1.place(x=300,y=130)
    
    label_2 = Label(root, text="DOB",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_2.place(x=80,y=180)
    
    month = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    m=StringVar()
    droplist=OptionMenu(root,m, *month)
    droplist.config(width=9)
    m.set('Month') 
    droplist.place(x=300,y=180)
    
    date = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
    d=StringVar()
    droplist=OptionMenu(root,d, *date)
    droplist.config(width=3)
    d.set('Date') 
    droplist.place(x=400,y=180)
    
    year = ['2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999','1998','1997','1996','1995','1994','1993','1992','1991',
            '1990','1989','1988','1987','1986','1985','1984','1983','1982','1981',
            '1980','1979','1978','1977','1976','1975','1974','1973','1972','1971', 
            '1970','1969','1968','1967','1966','1965','1964','1963','1962','1961', 
            '1960','1959','1958','1957','1956','1955','1954','1953','1952','1951',
            '1950','1949','1948','1947','1946','1945','1944','1943','1942','1941',
            '1940','1939','1938','1937','1936','1935','1934','1933','1932','1931',
            '1930','1929','1928','1927','1926','1925','1924','1923','1922','1921',
            '1920','1919','1918','1917','1916','1915','1914','1913','1912','1911',
            '1910','1909','1908','1907','1906','1905','1904','1903','1902','1901','1900'];
    y=StringVar()
    droplist=OptionMenu(root,y, *year)
    droplist.config(width=8)
    y.set('Year') 
    droplist.place(x=460,y=180)
    
    label_3= Label(root, text="Gender",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_3.place(x=80,y=230)
    var = IntVar()
    Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=295,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=350,y=230)
    
    label_4=Label(root, text="Height",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_4.place(x=80,y=280)
    
    entry_4 = Entry(root)
    entry_4.place(x=300,y=280)
    
    label_5=Label(root, text="Weight",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_5.place(x=80,y=330)
    
    entry_5 = Entry(root)
    entry_5.place(x=300,y=330)
    
    label_6=Label(root, text="Number",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_6.place(x=80,y=380)
    
    entry_6 = Entry(root)
    entry_6.place(x=300,y=380)
    
    label_7=Label(root, text="Email",width=20,font=("bold", 15),bg="gray6", fg="white")
    label_7.place(x=80,y=430)
    
    entry_7 = Entry(root)
    entry_7.place(x=300,y=430)
    
    Button(root, text='Submit',width=10,bg='brown',fg='white').place(x=310,y=500)
    Button(root, text='Next Page >>>',width=12,bg='brown',fg='white',command=root.destroy).place(x=303,y=550)
    root.mainloop()
    
run()
run1()
run2()