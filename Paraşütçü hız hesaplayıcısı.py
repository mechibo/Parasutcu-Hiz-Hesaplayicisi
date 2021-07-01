v1 = float(input("İlk hız :"))
g = 9.81
c = 12.5
m = float(input("Paraşütçü kütlesi : "))
ti1 = int(input("Şu anki zaman :"))
ti2 = int(input("İstenilen zaman :"))

hız = v1 + (g - (c/m)*v1)*(ti2 - ti1)


print("Paraşütçü hızı {} m/s'dir".format(hız))












