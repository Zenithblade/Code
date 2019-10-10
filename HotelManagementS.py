from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import tkinter as app

global daysh, rmtyp, bedsz, rmcpc, capacity, dayRate, capRate, bedRate, roomRate

dayRate = 750
capRate = 250
bedRate = 1500
roomRate = 12500

roomtype = ["President Suite", "Executive", "Penthouse", "Economy"]
bedsize = ["Single", "Double", "Queen", "King"]
capacity = ["1-2", "3-4", "5-6", "7-8"]



win = app.Tk()
win.title("Hotel Reservation System")
win.geometry('400x250')


#init 1st Row, Contacts and Days of Stay
confra = Frame(win)
confra.grid(row=0, column=0, padx = 10, pady =10)

name = StringVar()
nml = Label(confra, text="Occupant Name :")
nml.grid(row = 0, column = 0, sticky = E)
nme = Entry(confra, textvariable = name, width = 30)
nme.grid(row = 0, column = 1)

cont = StringVar()
ctl = Label(confra, text="Contact No. :")
ctl.grid(row = 1, column = 0, sticky = E)
cte = Entry(confra, textvariable = cont, width = 30)
cte.grid(row = 1, column = 1)


daysh = IntVar()
dayfra = Frame(win)
dayfra.grid(row=0, column=1, padx = 10, pady =10)

dyl = Label(dayfra, text="No. of Days")
dyl.grid(row = 0, column = 0)
dye = Entry(dayfra, width = 10)
dye.grid(row = 1, column = 0)


#init 2nd Row of UI, Room type
rmtdiv = Frame(win)
rmtdiv.grid(row=1, column=0, columnspan=2, padx = 10, pady=10)

rmtype = Frame(rmtdiv)
rmtype.grid(row=0, column=0, columnspan=2)

rmtypi = IntVar()
rmtyps = StringVar()
rmdiv1 = Frame(rmtdiv)
rmdiv1.grid(row=1, column=0, padx = 10, pady=10)
rmdiv2 = Frame(rmtdiv)
rmdiv2.grid(row=1, column=1, padx = 10, pady=10)

rtl = Label(rmtype, text="Type of Room:")
rtl.grid(row = 1, column = 0, columnspan = 2, sticky = EW)

rt1 = Radiobutton(rmdiv1, text = "President Suite", variable = rmtypi, value = 1)
rt1.grid(row = 1, column=0, sticky = W, padx = 20)

rt2 = Radiobutton(rmdiv1, text = "Executive", variable = rmtypi, value = 2)
rt2.grid(row = 2, column=0, sticky = W, padx = 20)

rt3 = Radiobutton(rmdiv2, text = "Penthouse", variable = rmtypi, value = 3)
rt3.grid(row = 1, column=0, sticky = W, padx = 20)

rt4 = Radiobutton(rmdiv2, text = "Economy", variable = rmtypi, value = 4)
rt4.grid(row = 2, column=0, sticky = W, padx = 20)



#init 3rd row of UI, Size of Bed and Room Capacity
cmbdiv = Frame(win)
cmbdiv.grid(row=3, column=0, columnspan = 2)

bedsz = StringVar()
bszfra = Frame(cmbdiv)
bszfra.grid(row=0, column=0, padx = 10)

bzl = Label(bszfra, text="Size of Bed")
bzl.grid(row = 0, column = 0)
bzc = Combobox(bszfra, state = "readonly")
bzc['values'] = bedsize
bzc.set("Choose Size")
bzc.grid(row = 1, column=0)
bzc.bind('<<ComboboxSelected>>', lambda x:changeCapacity(x))


rmcpc = StringVar()
rcpfra = Frame(cmbdiv)
rcpfra.grid(row=0, column=1, padx = 10, sticky= W)

rcl = Label(rcpfra, text="Room Capacity")
rcl.grid(row = 0, column = 0)
rcc = Combobox(rcpfra, state = "readonly")
rcc.set("Choose Max Capacity")
rcc.grid(row = 1, column=0)

def changeCapacity(bedsz):
    bedsz = bzc.get()
    a = bedsize.index(bedsz)
    if a == 0:
        rcc['values'] = ["1-2"]
    elif a == 1:
        rcc['values'] = ["1-2", "3-4"]
    elif a == 2:
        rcc['values'] = ["1-2", "3-4", "5-6"]
    else:
        rcc['values'] = ["1-2", "3-4", "5-6", "7-8"]

def calculate_Price():
    name = nme.get()
    cont = cte.get()
    daysh = dye.get()
    rtm = rmtypi.get()  #rtm = room type multiplier
    rmtyps = roomtype[rtm-1]
    bedsz = bzc.get()
    bdm = bedsize.index(bedsz) #bdm = bed size multiplier
    rmcpc = rcc.get()
    rcm = bedsize.index(bedsz) #rcm = room capacity multiplier

    dayFee = int(dayRate) * int(daysh)
    rmtFee = roomRate * (1 / (2*int(rtm)))
    bedFee = (bedRate * (int(bdm)+1)) * 0.75 + 150
    capFee = capRate * (int(rcm)+1)
    preFee = (rmtFee + dayFee + bedFee) * 0.2   #Prestige Fee
    serFee = (rmtFee + bedFee + capFee) * 0.1   #Service Fee
    totFee = dayFee + rmtFee + bedFee + capFee + preFee + serFee  #Total Fee


    messagebox.showinfo("Receipt",
                        "Name: " + name + "\n"
                        "Contact: " + cont + "\n"
                        "Room Type: " + str(rmtyps) + "\n"
                        "Bed Type: " + str(bedsz) + "\n"
                        "Max Cap.: " + str(rmcpc) + "\n"
                                                    "\n"
                                                    "\n"
                        "Stay Fee: " + str(dayFee) + "\n"
                        "Room Fee: " + str(rmtFee) + "\n"
                        "Bed Fee: " + str(bedFee) + "\n"
                        "Capacity Fee: " + str(capFee) + "\n"
                        "Prestige Fee: " + str(preFee) + "\n"
                        "Service Fee: " + str(serFee) + "\n"
                                                        "\n"
                                                        "\n"
                        "Total Fee: " + str(totFee) + " PHP"

                        )




rsrve = Frame(win)
rsrve.grid(row = 4, column = 0, columnspan = 2)

reser = Button(rsrve, text= "Reserve", command = lambda : calculate_Price())
reser.pack(pady =10)



win.mainloop()

