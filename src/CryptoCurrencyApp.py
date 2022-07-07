try:
    import os
    import sv_ttk
    import tkinter
    import requests
    import ntkutils
    import threading
    import darkdetect
    import webbrowser
    from bs4 import BeautifulSoup
    from typing_extensions import Self
    from typing import (Literal , final)
    from tkinter import (Label , StringVar)
    from tkinter.ttk import (Notebook , Frame , Button)
    
    from Management import Materials
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run Application') from None

finally:
    ...
    





@final
class Widget:
    def __init__(self : Self) -> Literal[None] | Self:
        self.root = tkinter.Tk()
        self.root.title(string='CryptoCurrency Prices')
        self.root.geometry(newGeometry='400x600')
        self.root.minsize(width=400 , height=600)
        self.root.maxsize(width=400 , height=600)
        self.root.resizable(width=False , height=False)
        self.root.iconbitmap(bitmap=os.path.normpath(path=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__)) , r'images/icon.ico')))
        
        self.tabControl = Notebook(master=self.root)
        
        self.tabCurrencies = Frame(master=self.tabControl)
        self.tabAbout = Frame(master=self.tabControl)
        
        self.tabControl.add(child=self.tabCurrencies , text='Currencies')
        self.tabControl.add(child=self.tabAbout , text='About')
        
        self.tabControl.pack(expand=1 , fill=Materials.Alignments.both)
        
        self.svBitcoin = StringVar(master=self.root)
        self.svEtherium = StringVar(master=self.root)
        self.svTether = StringVar(master=self.root)
        self.svShiba = StringVar(master=self.root)
        self.svStepn = StringVar(master=self.root)
        self.svSolana = StringVar(master=self.root)
        self.svDoge = StringVar(master=self.root)
        self.svBnb = StringVar(master=self.root)
        
        @final
        def setBySystemTheme() -> Literal[None]:
            match darkdetect.theme():
                case Materials.Themes.DARK:
                    sv_ttk.set_theme(theme=Materials.Themes.DARK.lower())
                    self.bitcoinLabel.configure(fg=Materials.Colors.white)
                    self.bitcoinPrice.configure(fg=Materials.Colors.white)
                    self.EtheriumLabel.configure(fg=Materials.Colors.white)
                    self.etheriumPrice.configure(fg=Materials.Colors.white)
                    self.ThetherLabel.configure(fg=Materials.Colors.white)
                    self.tetherPrice.configure(fg=Materials.Colors.white)
                    self.ShibaLabel.configure(fg=Materials.Colors.white)
                    self.ShibaPrice.configure(fg=Materials.Colors.white)
                    self.SolanaLabel.configure(fg=Materials.Colors.white)
                    self.SolanaPrice.configure(fg=Materials.Colors.white)
                    self.StepnLabel.configure(fg=Materials.Colors.white)
                    self.StepnPrice.configure(fg=Materials.Colors.white)
                    self.DogeLabel.configure(fg=Materials.Colors.white)
                    self.DogePrice.configure(fg=Materials.Colors.white)
                    self.BnbLabel.configure(fg=Materials.Colors.white)
                    self.BnbPrice.configure(fg=Materials.Colors.white)
                    ntkutils.dark_title_bar(window=self.root)
                case Materials.Themes.LIGHT:
                    sv_ttk.set_theme(theme=Materials.Themes.LIGHT.lower())
                    self.bitcoinLabel.configure(fg=Materials.Colors.black)
                    self.bitcoinPrice.configure(fg=Materials.Colors.black)
                    self.EtheriumLabel.configure(fg=Materials.Colors.black)
                    self.etheriumPrice.configure(fg=Materials.Colors.black)
                    self.ThetherLabel.configure(fg=Materials.Colors.black)
                    self.tetherPrice.configure(fg=Materials.Colors.black)
                    self.ShibaLabel.configure(fg=Materials.Colors.black)
                    self.ShibaPrice.configure(fg=Materials.Colors.black)
                    self.SolanaLabel.configure(fg=Materials.Colors.black)
                    self.SolanaPrice.configure(fg=Materials.Colors.black)
                    self.StepnLabel.configure(fg=Materials.Colors.black)
                    self.StepnPrice.configure(fg=Materials.Colors.black)
                    self.DogeLabel.configure(fg=Materials.Colors.black)
                    self.DogePrice.configure(fg=Materials.Colors.black)
                    self.BnbLabel.configure(fg=Materials.Colors.black)
                    self.BnbPrice.configure(fg=Materials.Colors.black)
                    self.root.update_idletasks()
            
        @final        
        def getCurrenciesPrice() -> Literal[None]:
            bitcoinPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/bitcoin/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            etheriumPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/ethereum/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            tetherPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/tether/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            shibaPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/shiba-inu/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            stepnPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/green-metaverse-token/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            solanaPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/solana/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            dogePrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/dogecoin/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            bnbPrice = BeautifulSoup(requests.get(url='https://coinmarketcap.com/currencies/bnb/').content , 'html.parser').find('div' , attrs={'class':'priceValue'}).text.strip().replace('\n' , '')
            self.svBitcoin.set(value=bitcoinPrice)
            self.svEtherium.set(value=etheriumPrice)
            self.svTether.set(value=tetherPrice)
            self.svShiba.set(value=shibaPrice)
            self.svStepn.set(value=stepnPrice)
            self.svSolana.set(value=solanaPrice)
            self.svDoge.set(value=dogePrice)
            self.svBnb.set(value=bnbPrice)
            
        @final
        def updatePrices() -> Literal[None]:
            self.root.after(ms=5000 , func=getCurrenciesPrice)
         
        @final   
        def startThread() -> Literal[None]:
            th = threading.Thread(target=getCurrenciesPrice)
            th2 = threading.Thread(target=updatePrices)
            
            th.daemon = True
            th2.daemon = True
            
            th.start()
            th2.start()
            
        @final
        def aboutMeClickEvent() -> Literal[None]:
            webbrowser.open(url='https://github.com/shervinbdndev/')
                    
        self.B = Label(
            master=self.tabCurrencies ,
            text='B' ,
            fg=Materials.Colors.yellow ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.B.place(relx=0.05 , rely=0.08 , anchor=Materials.Alignments.center)
                    
        self.bitcoinLabel = Label(
            master=self.tabCurrencies ,
            text='itcoin' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.bitcoinLabel.place(relx=0.17 , rely=0.08 , anchor=Materials.Alignments.center)
        
        self.bitcoinPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svBitcoin ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.bitcoinPrice.place(relx=0.7 , rely=0.075 , anchor=Materials.Alignments.center)
        
        self.E = Label(
            master=self.tabCurrencies ,
            text='E' ,
            fg=Materials.Colors.blue ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.E.place(relx=0.05 , rely=0.2 , anchor=Materials.Alignments.center)
        
        self.EtheriumLabel = Label(
            master=self.tabCurrencies ,
            text='therium' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.EtheriumLabel.place(relx=0.207 , rely=0.2 , anchor=Materials.Alignments.center)
        
        self.etheriumPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svEtherium ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.etheriumPrice.place(relx=0.7 , rely=0.196 , anchor=Materials.Alignments.center)
        
        self.ThetherLabel = Label(
            master=self.tabCurrencies ,
            text='ether' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.ThetherLabel.place(relx=0.16 , rely=0.323 , anchor=Materials.Alignments.center)
        
        self.T = Label(
            master=self.tabCurrencies ,
            text='T' ,
            fg=Materials.Colors.green ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.T.place(relx=0.05 , rely=0.323 , anchor=Materials.Alignments.center)
        
        self.tetherPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svTether ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.tetherPrice.place(relx=0.7 , rely=0.320 , anchor=Materials.Alignments.center)
        
        self.S = Label(
            master=self.tabCurrencies ,
            text='S' ,
            fg=Materials.Colors.orange ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.S.place(relx=0.05 , rely=0.449 , anchor=Materials.Alignments.center)
        
        self.ShibaLabel = Label(
            master=self.tabCurrencies ,
            text='hiba' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.ShibaLabel.place(relx=0.145 , rely=0.449 , anchor=Materials.Alignments.center)
        
        self.ShibaPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svShiba ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.ShibaPrice.place(relx=0.7 , rely=0.445 , anchor=Materials.Alignments.center)
        
        self.ST = Label(
            master=self.tabCurrencies ,
            text='S' ,
            fg=Materials.Colors.darkOrange ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.ST.place(relx=0.05 , rely=0.570 , anchor=Materials.Alignments.center)
        
        self.StepnLabel = Label(
            master=self.tabCurrencies ,
            text='tepn' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.StepnLabel.place(relx=0.148 , rely=0.570 , anchor=Materials.Alignments.center)
        
        self.StepnPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svStepn ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.StepnPrice.place(relx=0.7 , rely=0.566 , anchor=Materials.Alignments.center)
        
        self.SOL = Label(
            master=self.tabCurrencies ,
            text='S' ,
            fg=Materials.Colors.purple ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.SOL.place(relx=0.05 , rely=0.692 , anchor=Materials.Alignments.center)
        
        self.SolanaLabel = Label(
            master=self.tabCurrencies ,
            text='olana' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.SolanaLabel.place(relx=0.167 , rely=0.692 , anchor=Materials.Alignments.center)
        
        self.SolanaPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svSolana ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.SolanaPrice.place(relx=0.7 , rely=0.689 , anchor=Materials.Alignments.center)
        
        self.Dg = Label(
            master=self.tabCurrencies ,
            text='D' ,
            fg=Materials.Colors.golden ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.Dg.place(relx=0.05 , rely=0.802 , anchor=Materials.Alignments.center)
        
        self.DogeLabel = Label(
            master=self.tabCurrencies ,
            text='oge' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.DogeLabel.place(relx=0.140 , rely=0.802 , anchor=Materials.Alignments.center)
        
        self.DogePrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svDoge ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.DogePrice.place(relx=0.7 , rely=0.802 , anchor=Materials.Alignments.center)
        
        self.bB = Label(
            master=self.tabCurrencies ,
            text='B' ,
            fg=Materials.Colors.burlyWood ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=0 ,
        )
        
        self.bB.place(relx=0.05 , rely=0.920 , anchor=Materials.Alignments.center)
        
        self.BnbLabel = Label(
            master=self.tabCurrencies ,
            text='NB' ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.BnbLabel.place(relx=0.129 , rely=0.920 , anchor=Materials.Alignments.center)
        
        self.BnbPrice = Label(
            master=self.tabCurrencies ,
            textvariable=self.svBnb ,
            fg=Materials.Colors.white ,
            font=(Materials.Fonts.vani , 20 , Materials.FontWeights.bold) ,
            justify=Materials.Alignments.center ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            border=0 ,
            borderwidth=0 ,
            underline=None ,
        )
        
        self.BnbPrice.place(relx=0.7 , rely=0.914 , anchor=Materials.Alignments.center)
        
        self.btnGithub = Button(
            master=self.tabAbout ,
            text="Github" ,
            command=aboutMeClickEvent ,
            width=15 ,
            state=Materials.States.normal ,
            cursor=Materials.Cursors.hand ,
            underline=None ,
        )
        
        self.btnGithub.place(relx=0.5 , rely=0.5 , anchor=Materials.Alignments.center , height=45)
        
        setBySystemTheme()
        startThread()
        
        self.root.mainloop()
        
        
        
        

@final
def main() -> Literal[None]:
    Widget()


    
    
    

if (__name__ == '__main__' and __package__ is None):
    main()