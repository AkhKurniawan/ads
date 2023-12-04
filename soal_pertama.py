import math

#masukkan data
L1 = float(input("masukkan L1: "))
L2 = float(input("masukkan L2: "))
B1 = float(input("masukkan B1: "))
B2 = float(input("masukkan B2: "))
h1 = float(input("masukkan h1(m): "))
h2 = float(input("masukkan h2(m): "))
jarak_23 = float(input("masukkan jarak(m): "))
sudut_123 = float(input("masukkan sudut: "))
zenith_21 = float(input("masukkan zenit_21: "))
zenith_23 = float(input("masukkan zenit_23: "))
R = 6371000

#menghitung azimuth 21 dan azimuth 23
azimuth_21 = math.atan2(math.sin(math.radians(L2) - math.radians(L1)), 
                        (math.cos(math.radians(B1)) * math.tan(math.radians(B2)) - 
                         math.sin(math.radians(B1)) * math.cos(math.radians(L2) - math.radians(L1))))
azimuth_23 = azimuth_21 + math.radians(sudut_123)
print("azimuth 21= ", azimuth_21)
print("azimuth 23= ", azimuth_23)

#menghitung koordinat titik 3
delta_h = h2 - h1
jarak_21 = jarak_23 * math.sin(math.radians(sudut_123)) / math.sin(math.radians(180) - zenith_21 - zenith_23)
print("delta H= ", delta_h)
print("jarak 21= ",jarak_21)

#koordinat titik 3
B3 = math.asin(math.sin(math.radians(B1)) * math.cos(jarak_21 / R) + 
               math.cos(math.radians(B1)) * math.sin(jarak_21 / R) * 
               math.cos(azimuth_21))
L3 = math.radians(L1) + math.atan2(math.sin(azimuth_21) * math.sin(jarak_21 / R) 
                                   * math.cos(math.radians(B1)), math.cos(jarak_21 / R) - 
                                   math.sin(math.radians(B1)) * math.sin(math.radians(B3)))
h3 = h1 + delta_h * jarak_21 / jarak_23

#konversi Ke degress
B3_deg = math.degrees(B3)
L3_deg = math.degrees(L3)

#Tampilkan hasil
print("Latitude koordinat titik 3  = " , L3_deg)
print("Longitude koordinat titik 3 = " , B3_deg)
print("Altitude koordinat titik 3  = " , h3)



