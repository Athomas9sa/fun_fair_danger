from helper import enter

def exit_key():
    print('''    Oh dear. The wizard has forgotten English and 
    will from now on out only be speaking wizard. 
    But don't be too alarmed! In the each sentence, type the first letter of the second word.  

Psviq 1twyq hspsv wmx eqix, gsrwigxixyv ehmtmwgmrk ipmx. Tippirxiwuyi ujj ijjmgmxyv evgy. Wywtirhmwwi 6ymw yvre jvmrkmppe, ikiwxew svgm rig, psfsvxmw rmfl. Qeyvmw 6x qsppmw ivex. Gvew 5ip yvre zipmx. Ixmeq ceygmfyw pmfivs zip xyvtmw gyvwyw, ex yppeqgsvtiv rmwp gsrwigxixyv. Ryppeq omx eqix pygxyw wetmir. Req 3srzeppmw ivsw e typzmrev gsrwiuyex. Mr silmgype, pmkype tsvxxmxsv tlevixve jivqirxyq, jipmw hspsv jegmpmwmw eykyi, mh kvezmhe ryppe zipmx eg svgm. Wywtirhmwwi 2kix eygxsv zipmx.

Ryppeq 8y shms iy hmeq kvezmhe xiqtyw ijjmgmxyv iy pmfivs. Hsrig 9ygxyw pis nywxs, zmxei qexxmw hmeq tswyivi jegmpmwmw. Eirier ipmuyix gsrkyi qsppmw. Gyvefmxyv 4vmrkmppe wih tyvyw ix zirirexmw. Hsrig 0sviq ivsw, svrevi rsr megypmw ikix, jmrmfyw uymw uyeq. Hsrig hymw wekmxxmw ib. Ryrg 9ih uyeq zmxei jipmw ipimjirh svrevi fmfirhyq wih mtwyq. Req 7ym erxi, ypxvmgiw ikix xippyw zip, zevmyw ypxvmgmiw ryrg. Qeigirew 2pegivex, qeyvmw e zyptyxexi xmrgmhyrx, zipmx pigxyw zirirexmw hspsv, zip pygxyw evgy rmfl zip wiq. Ziwxmfypyq 8g vmwyw gsqqshs, psfsvxmw evgy ikix, eggyqwer pmkype. Epmuyeq 4y vyxvyq hmeq.
    ''')
    code = input("Enter code here: ")
    if code == "1u665 co3s 289 i4 0h9 7284":
        print("Your passphrase is: {}".format(leet_speak("1u665 co3s 289 i4 0h9 7284")))

leet_dict = {
    '4' : 'N',
    '3' : 'W',
    '6' : 'Z',
    '1' : 'F',
    '0' : 'T',
    '5' : 'Y',
    '7' : 'B',
    '9' : 'E',
    '2' : 'A',
    '8' : 'R'
}


def leet_speak(my_string):
    leet_string = ""
    for i in my_string:
        if i.upper() in leet_dict:
            leet_string += (leet_dict[i.upper()])
        else:
            leet_string += (i)
    return leet_string.capitalize()




# exit_key()

