#Mengimpor library yang dibutuhkan
import numpy as np # library untuk pemrosesan array
import imageio # library untuk membaca citra
import matplotlib.pyplot as plt # library untuk menampilkan citra
import cv2 # library untuk pemrosesan citra menggunakan OpenCV
#Membaca citra menggunakan opencv dan disimpan pada variabel img
img = cv2.imread('download.jpeg')
#Membaca citra dan menyimpan ukuran serta tipe datanya
img_height = img.shape[0]#menyimpan data di variable img_height
img_width = img.shape[1]#menyimpan data di variable img_width
img_channel = img.shape[2]#menyimpan data di variable img_channel
img_type = img.dtype#type img 
# membuat array kosong untuk citra hasil pemrosesan
img_brightness = np.zeros(img.shape, dtype=np.uint8)
# fungsi untuk meningkatkan kecerahan citra
def brighter(nilai):#definisi yang diberikan adalah fungsi Python yang disebut brighter yang meningkatkan kecerahan gambar.
    #Fungsi mengambil nilai parameter tunggal yang merupakan jumlah kecerahan yang akan ditambahkan ke setiap piksel dalam gambar.
    for y in range(0, img_height):# melalui setiap piksel pada gambar dengan mengulangi tinggi dan lebar gambar. 
        for x in range(0, img_width):
            red = img[y][x][0]# Untuk setiap piksel, nilai warna merah, hijau, dan biru diekstraksi menggunakan pengindeksan larik. 
            green = img[y][x][1]
            blue = img[y][x][1]
            gray = (int(red) + int(green) + int(blue)) / 3# Kemudian, nilai rata-rata dari nilai warna tersebut dihitung dan disimpan dalam variabel yang disebut abu-abu.
            gray += nilai#Selanjutnya nilai keabuan dinaikkan atau diturunkan dengan nilai nilai agar citra lebih terang. 
            if gray > 255:# Jika nilai abu-abu yang dihasilkan lebih besar dari 255, maka dibatasi pada 255 untuk mencegah luapan. 
                gray = 255
            if gray < 0:# jika nilai abu-abu yang dihasilkan kurang dari 0, itu dibatasi pada 0 untuk mencegah aliran bawah.
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)#  nilai kecerahan baru untuk piksel disimpan dalam larik baru yang disebut img_brightness, yang berisi nilai piksel baru sebagai tupel (abu-abu, abu-abu, abu-abu) di mana setiap nilai mewakili nilai kecerahan untuk warna merah, hijau, dan biru saluran warna, masing-masing.

    # menampilkan citra asli dan hasil pemrosesan
brighter(-100)#Selanjutnya nilai keabuan diturunkan dengan nilai nilai agar citra lebih terang. 
plt.imshow(img_brightness) # menampilkan citra  hasil pemrosesan yang disimpan di variable img_brightness
plt.title("Brightness -100")#nama judul gambar
plt.show()#fungsi menampilkan
brighter(100)#Selanjutnya nilai keabuan dinaikkan dengan nilai nilai agar citra lebih terang. 
plt.imshow(img_brightness) # menampilkan citra asli dan hasil pemrosesan
plt.title("Brightness 100")#nama judul gambar
plt.show()#fungsi menampilkan

# bri RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)
# membuat array kosong untuk citra hasil pemrosesan Fungsi tersebut kemudian membuat larik bernama img_rgbbright yang memiliki bentuk yang sama dengan gambar masukan dan bertipe np.uint8.
# fungsi rgb
def rgbbrighter(nilai):
#definis yang diberikan adalah fungsi Python yang disebut rgbbrighter yang meningkatkan kecerahan gambar dengan saluran warna RGB.
#Fungsi mengambil nilai parameter tunggal yang merupakan jumlah kecerahan yang akan ditambahkan ke setiap piksel dalam gambar.   
    for y in range(0, img_height):#Selanjutnya, fungsi beralih melalui setiap piksel pada gambar dengan mengulangi tinggi dan lebar gambar. 
        #Untuk setiap piksel, nilai warna merah, hijau, dan biru diekstraksi menggunakan pengindeksan larik. 
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:   
                red = 255   # Jika nilai abu-abu yang dihasilkan lebih besar dari 255, maka dibatasi pada 255 untuk mencegah luapan.
            if red < 0:     # jika nilai abu-abu yang dihasilkan kurang dari 0, itu dibatasi pada 0 untuk mencegah aliran bawah.
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255 # Jika nilai abu-abu yang dihasilkan lebih besar dari 255, maka dibatasi pada 255 untuk mencegah luapan.
                # jika nilai abu-abu yang dihasilkan kurang dari 0, itu dibatasi pada 0 untuk mencegah aliran bawah.
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbright[y][x] = (red, green, blue)#nilai kecerahan baru untuk piksel disimpan dalam larik img_rgbbright sebagai tupel (merah, hijau, biru) di mana setiap nilai mewakili nilai kecerahan untuk saluran warna merah, hijau, dan biru.
# menampilkan
rgbbrighter(-100)#nilai kecerahan turun
plt.imshow(img_rgbbright)#menampilkan img yang sudah dirubah kecerahan
plt.title("Brightness -100")#judul
plt.show()#fungsi penampil
rgbbrighter(100)#nilai kecerahan naik
plt.imshow(img_rgbbright)#menampilkan img yang sudah dirubah kecerahan
plt.title("Brightness 100")#judul
plt.show()#fungsi penampil
img_contras = np.zeros(img.shape, dtype=np.uint8)# membuat array numpy baru bernama img_contras dengan bentuk yang sama dengan gambar input img dan tipe data np.uint8. Larik ini akan digunakan untuk menyimpan gambar yang disesuaikan kontrasnya.
def contrass(nilai):# mendefinisikan fungsi Python baru yang disebut contrass yang mengambil nilai parameter tunggal, yang merupakan jumlah kontras yang akan ditambahkan ke setiap piksel dalam gambar.
    for y in range(0, img_height):# memulai loop bersarang yang mengulang setiap piksel dalam gambar dengan mengulang melalui tinggi dan lebar gambar.
        for x in range(0, img_width):# melanjutkan perulangan bersarang yang dimulai pada baris sebelumnya.
            red = img[y][x][0]# mengekstrak nilai warna merah dari piksel saat ini pada posisi (x, y) di gambar input img.
            green = img[y][x][1]# mengekstrak nilai warna hijau dari piksel saat ini pada posisi (x, y) dalam gambar input img.
            blue = img[y][x][2]# mengekstrak nilai warna biru dari piksel saat ini pada posisi (x, y) dalam gambar input img.
            gray = (int(red) + int(green) + int(blue)) / 3# menghitung nilai skala abu-abu rata-rata dari piksel saat ini dengan menjumlahkan nilai warna merah, hijau, dan biru, mengubahnya menjadi bilangan bulat, dan dibagi 3.
            gray += nilai# menambahkan nilai nilai ke nilai skala abu-abu piksel saat ini untuk meningkatkan kontrasnya.
            if gray > 255:# memeriksa apakah nilai skala abu-abu yang dihasilkan lebih besar dari 255.
                gray = 255# menetapkan nilai skala abu-abu menjadi 255 jika lebih besar dari 255 untuk mencegah luapan.
            img_contras[y][x] = (gray, gray, gray)# menetapkan nilai piksel yang disesuaikan kontras dalam larik img_contras sebagai tupel (abu-abu, abu-abu, abu-abu) di mana setiap nilai mewakili nilai skala abu-abu untuk warna merah , masing-masing saluran warna hijau, dan biru.

# menampilkan
contrass(20)# memanggil fungsi kontras dengan parameter 20 untuk menyesuaikan kontras gambar input.
plt.imshow(img_contras)# menampilkan gambar dengan penyesuaian kontras yang disimpan dalam larik img_contras menggunakan fungsi imshow matplotlib.
plt.title("contrass 20")#menetapkan judul plot saat ini menjadi "contrass 20" menggunakan fungsi judul matplotlib.
plt.show()# menampilkan plot saat ini di layar.
contrass(100)# memanggil fungsi kontras dengan parameter 100 untuk menyesuaikan kontras gambar input.
plt.imshow(img_contras)# menampilkan gambar dengan penyesuaian kontras yang disimpan dalam larik img_contras
plt.title("contrass 100")#menetapkan judul plot contrass 100
plt.show()# menampilkan plot saat ini di layar.

img_contrasrgb = np.zeros(img.shape, dtype=np.uint8)# Membuat variabel img_contrasrgb yang berisi array numpy dengan ukuran yang sama dengan img dan tipe data uint8, sehingga img_contrasrgb akan menyimpan gambar dengan nilai piksel antara 0-255 dan tipe data yang sama dengan gambar asli img.
# fungsi rgb
def rgbcontrass(nilai):# mendefinisikan fungsi Python baru yang disebut contrass yang mengambil nilai parameter tunggal, yang merupakan jumlah kontras yang akan ditambahkan ke setiap piksel dalam gambar.
    for y in range(0, img_height):# memulai loop bersarang yang mengulang setiap piksel dalam gambar dengan mengulang melalui tinggi dan lebar gambar.
        for x in range(0, img_width):# melanjutkan perulangan bersarang yang dimulai pada baris sebelumnya.
            red = img[y][x][0]#mengambil nilai merah dari img
            red += nilai#merah ditambah sejumlah nilai
            if red > 255:#jika nilai merah lebih dari 255 maka dibuat jadi 255
                red = 255
            green = img[y][x][1]#mengambil nilai hijau dari img
            green += nilai#ditambah sejumlah nilai
            if green > 255:#jika nilai hijau lebih dari 255 maka dibuat jadi 255
                green = 255
            blue = img[y][x][2]#mengambil nilai biru dari img
            blue += nilai#ditambah sejumlah nilai
            if blue > 255:#jika nilai biru lebih dari 255 maka dibuat jadi 255
                blue = 255
            img_contrasrgb[y][x] = (red, green, blue)# menetapkan nilai piksel yang disesuaikan kontras dalam larik img_contrasrgb
# menampilkan
rgbcontrass(20)# memanggil fungsi kontras dengan parameter 20 untuk menyesuaikan kontras gambar input.
plt.imshow(img_contrasrgb)# menampilkan gambar dengan penyesuaian kontras
plt.title("contrass 20")#judulplot
plt.show()# menampilkan plot saat ini di layar.
rgbcontrass(100)# memanggil fungsi kontras dengan parameter 100 untuk menyesuaikan kontras gambar input.
plt.imshow(img_contrasrgb)# menampilkan gambar dengan penyesuaian kontras
plt.title("contrass 100")
plt.show()# menampilkan plot saat ini di layar.

img_autocontrass = np.zeros(img.shape, dtype=np.uint8)# Membuat variabel img_autocontras yang berisi array numpy dengan ukuran yang sama dengan img dan tipe data uint8, sehingga img_contrasrgb akan menyimpan gambar dengan nilai piksel antara 0-255 dan tipe data yang sama dengan gambar asli img.

def autocontrass():#Mendefinisikan sebuah fungsi bernama "autocontrass"
    xmax = 300#Mendefinisikan variabel "xmax" dan menginisialisasinya dengan nilai 300
    xmin = 0# Mendefinisikan variabel "xmin" dan menginisialisasinya dengan nilai 0
    d = 0#Mendefinisikan variabel "d" dan menginisialisasinya dengan nilai 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):#Memulai loop bersarang untuk iterasi pada setiap baris gambar
        for x in range(0, img_width):#melanjutkan loop untuk iterasi pada setiap kolom gambar
            red = img[y][x][0]#Mendefinisikan variabel "red" dan mengambil nilai warna merah pada posisi piksel (x,y).
            green = img[y][x][1]#Mendefinisikan variabel "green" dan mengambil nilai warna hijau pada posisi piksel (x,y).
            blue = img[y][x][2]#Mendefinisikan variabel "blue" dan mengambil nilai warna biru pada posisi piksel (x,y).
            gray = (int(red) + int(green) + int(blue)) / 3#Menghitung nilai rata-rata dari ketiga warna RGB untuk mendapatkan warna abu-abu.
            if gray < xmax:#Memeriksa jika nilai gray kurang dari nilai xmax.
                xmax = gray#Jika ya, maka nilai xmax akan diubah menjadi nilai gray.
            if gray > xmin:#Memeriksa jika nilai gray lebih dari nilai xmin.
                xmin = gray#Jika ya, maka nilai xmin akan diubah menjadi nilai gray.
    d = xmin-xmax#Menghitung selisih antara nilai xmin dan xmax dan menyimpannya ke dalam variabel "d".
    for y in range(0, img_height):#Memulai loop untuk iterasi pada setiap baris gambar.
        for x in range(0, img_width):#melanjutkan loop untuk iterasi pada setiap kolom gambar.
            red = img[y][x][0]#Mendefinisikan variabel "red" dan mengambil nilai warna merah pada posisi piksel (x,y).
            green = img[y][x][1]#Mendefinisikan variabel "green" dan mengambil nilai warna hijau pada posisi piksel (x,y).
            blue = img[y][x][2]#Mendefinisikan variabel "blue" dan mengambil nilai warna biru pada posisi piksel (x,y).
            gray = (int(red) + int(green) + int(blue)) / 3# Menghitung nilai rata-rata dari ketiga warna RGB untuk mendapatkan warna abu-abu.
            gray = int(float(255/d) * (gray-xmax))#Menghitung nilai kontras untuk setiap piksel menggunakan rumus (255/d) * (gray-xmax) dan mengkonversinya menjadi integer.
            img_autocontrass[y][x] = (gray, gray, gray)#Menetapkan nilai kontras yang telah dihitung pada setiap piksel dan menyimpannya

        autocontrass()# memanggil fungsi  untuk menyesuaikan kontras gambar input.
        plt.imshow(img_autocontrass)# menampilkan gambar dengan penyesuaian kontras
        plt.title("Contrass Autolevel")#judul
        plt.show()# menampilkan plot saat ini di layar.
