correspondences = {'a' :'1','b':'2','c':'3','d' :'4','e':'5','f':'6','g' :'7','h':'8','i':'9','j' :'?','k':'¿','l':'¡','m' :'!','n':'{','ñ':'}','o' :'*','p':'(','q':')','r' :'-','s':'_','t':';','u' :'^','v':'=','w':'|','x' :'/','y':'<','z':'>',' ':' '}

def encrypt(message):
    encrypted_list = []
    for char in [*message.lower()]:
        encrypted_list.append(correspondences.get(char," "))

    return ''.join(map(str,encrypted_list))
def decrypt(message):
    decrypted_list = []
    for char in [*message.lower()]:
        decrypted_list.append(list(correspondences.keys())[list(correspondences.values()).index(char)])
 
    return ''.join(map(str,decrypted_list))


print(encrypt('Este es un programa capaz de encriptar cualquier mensaje que le pases y despues desencriptarlo usando las correspondencias arriba señaladas'))


