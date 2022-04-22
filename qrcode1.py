import pyqrcode
def menu():
    print('*'*167)
    print("MAIN MENU".center(160),"\n")
    print(" WELCOME TO THE QR CODE GENERATOR ".center(160))
    
    
menu()
n=int(input("HOW MANY QRCODES YOU WANT : "))
print('*'*167)
for i in range(n):
    def qrcode():
       q= pyqrcode.create(input("ENTER THE TEXT YOU WANT TO HIGHLIGHT : "))
       c="qrcode"+ str(i) + ".png"
       q.png (c,scale=6)
       print("successfully created qr code")
       print('*'*167)

    if __name__=="__main__":
        qrcode()
