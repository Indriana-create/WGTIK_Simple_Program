print ("===========================================")
print ("    ~ Celcius to Fahrenheit Convertion ~   ")
print ("===========================================")

while(1):
    suhu = input("*Maximal suhu yang dapat dikonversi = 280 Celcius \n\nSuhu Celcius yang ingin dikonversi = ")
    print("\n")

    if int(suhu) < 280 :
        tempC = int(suhu)
        tempF = 1.8*tempC+32
        print('%.2f'%tempC, "Celcius = ",'%.2f'%tempF, "Fahrenheit ")
        print ("===========================================")
    else :
        print("Suhu Celcius Tidak Sesuai Batas Maximal! \nBatas konversi maximal 280 derajat celcius")
        print ("===========================================")
