import random
import string

#Dictionary που αντιστοιχίζει γράμμα με δυαδικό νούμερο
possible_messages={"A": "00000", "B": "00001", "C": "00010", "D": "00011", "E": "00100", "F": "00101", "G": "00110", "H": "00111",
                   "I": "01000", "J": "01001", "K": "01010", "L": "01011", "M": "01100", "N": "01101", "O": "01110", "P": "01111",
                   "Q": "10000", "R": "10001", "S": "10010", "T": "10011", "U": "10100", "V": "10101", "W": "10110", "X": "10111",
                   "Y": "11000", "Z": "11001", ".": "11010", "!": "11011", "?": "11100", "(": "11101", ")": "11110", "-": "11111"}
flag=True
this_message=''
while flag:
    message= input('Please type a message to encrypt uppercase letters and special characters only: ')
    for m in message:
        this_message+=m  #Προσθέτω τον τωρινό χαρακτήρα στο προσωρινό string this_message
        if m not in possible_messages.keys():   #Αν ο τωρινός χαρακτήρας δεν υπάρχει στο dictionary possible_messages
            this_message=''                     #τότε κάνω κενό το this_message και το loop ξεκινά από την αρχή
            break
        else:              #Αν ο χαρακτήρας υπάρχει στο dictionary τότε προχωράει στο επόμενο γράμμα
            continue
    if this_message==message:  #Αν έχει τελειώσει επιτυχώς το for loop δηλαδή έχουν ελεγθεί όλοι οι χαρακτήρες τότε τελειώνει το while
        flag=False
    
#Μετατροπή μηνύματος σε δυαδικό
binary_message=''
for this_character in message:   #Εξετάζω έναν έναν τους χαρακτήρες του μηνύματος
    for i in possible_messages:   #Διαπερνώ όλους τους χαρακτήρες του dictionary, 
        if i==this_character:          #Ελέγχω αν ο χαρακτήρας του dictionary είναι ίσος με τον χαρακτήρα του μηνύματος
            binary_message+=possible_messages[i]   #προσθέτω τον δυαδικό του αντίστοιχο αριθμό στο binary_message
print("The binary message is: "+ binary_message)

key=""
for i in range(len(binary_message)):   #Το κλειδί θα έχει ίδιο μήκος με το μήνυμα
    key += str(random.randint(0, 1))   #δημιουργώ το κάθε ψηφίο του με την random.randint
print("The key is: "+ key) 

#encryption
encrypted_message=''
for i in range(len(binary_message)):
    temp=int(binary_message[i])^int(key[i]) #Κάνω XOR ένα ένα τα bit του μηνύματος με του κλειδιού
    encrypted_message+=str(temp)  #Προσθέτω ένα ένα τα bit του αποτελέσματος σε ένα string
   
print("The encrypted message is: " + encrypted_message)

#decryption
count=1
decrypted_message=''
current_binary_character=''
for i in range(len(encrypted_message)):
    temp=int(encrypted_message[i])^int(key[i])   #Αποκρυπτογραφώ 5 δυαδικούς χαρακτήρες    
    current_binary_character+=str(temp)
    count+=1
    if count>5: #Όταν το count>5 τότε έχουμε βρει έναν χαρακτήρα του μηνύματος γιατί ο binary αντίστοιχος έχει 5 ψηφία
        for letter in possible_messages:
            if current_binary_character==possible_messages[letter]:    #Βρίσκω τον χαρακτήρα που αντιστοιχεί στο 5ψήφιο binary
                decrypted_message+=letter   #Προσθέτω τον χαρακτήρα στο τελικό αποκρυπτογραφημένο μήνυμα
        temp=''      #Ρυθμίζω τις παραμέτρους για το επόμενο δυαδικό με 5 bits    
        count=1
        current_binary_character=''
print("The decrypted message is: " + decrypted_message)