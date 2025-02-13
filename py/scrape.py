import requests
from bs4 import BeautifulSoup

# URL website yang telah kamu buat (jika dijalankan secara lokal, gunakan localhost, misalnya http://localhost:8000/index.html)
url = 'https://www.kompas.com/tag/pendidikan'

# Mengambil konten halaman menggunakan requests
response = requests.get(url)

if response.status_code == 200:
    # Parsing konten HTML dari halaman web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Menyaring elemen berdasarkan ID atau class tertentu
    # Contoh: Ambil semua elemen <div> dengan class 'content'
    content = soup.find_all('a', class_='article__link')

    # Jika menggunakan ID
    # content = soup.find('div', id='specific-id')

    # Membuka file CryptoCurrency.txt untuk menulis hasil
    with open("ScrapeData.txt", "w", encoding="utf-8") as file:

    # Menulis judul atau header di file
        file.write("Hasil Scraping Judul Berita:\n\n")
        for div in content:
            print(div.text)
            
            # Menulis setiap elemen <h1> ke dalam file
            file.write(div.text + "\n")  # Menambahkan teks setiap elemen <h1> ke dalam file

    print("Data telah disimpan ke dalam ScrapeData.txt")
else:
    print("Gagal mengambil halaman. Status Code:", response.status_code)