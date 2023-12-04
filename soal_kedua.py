import math

jarak_miring = float(input("masukkan jarak miring(m): "))
azimut_AB = float(input("masukkan azimut(°): "))
lintang_A = float(input("masukkan lintang A(°): "))
tinggi_geodetic_A = float(input("tinggi geodetic(m): "))

def haversine_distance(lat1, lon1, lat2, lon2):
    # Mengonversi derajat ke radian
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Menghitung delta lintang dan bujur
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Rumus Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Jarak di elipsoida
    radius_of_earth = 6371000 # dalam meter
    distance = radius_of_earth * c
    return distance

# Menghitung koordinat titik B berdasarkan azimut dan jarak miring
azimut_AB_rad = math.radians(azimut_AB)
dlat_B = jarak_miring * math.cos(azimut_AB_rad) / 6371000 

# konversi jarak ke derajat lintang
dlon_B = jarak_miring * math.sin(azimut_AB_rad) / (6371000 * math.cos(math.radians(lintang_A)))
lat_A = lintang_A
lon_A = 0 # Misalkan titik A berada di meridian nol
lat_B = lat_A + math.degrees(dlat_B)
lon_B = lon_A + math.degrees(dlon_B)

# Menghitung jarak menggunakan rumus Haversine
jarak_elipsoida = haversine_distance(lat_A, lon_A, lat_B, lon_B)

# Menambahkan tinggi geodetik A ke jarak
jarak_elipsoida_dengan_tinggi = math.sqrt(jarak_miring**2 + tinggi_geodetic_A**2)

# Menampilkan hasil
print(f"Jarak di elipsoida (Haversine): {jarak_elipsoida:.2f} meter")
print(f"Jarak miring dengan tinggi geodetik (Pythagoras): {jarak_elipsoida_dengan_tinggi:.2f} meter")

