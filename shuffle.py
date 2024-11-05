import random
import argparse
import json

# Data mahasiswa
'''
names = [ "Ahmad Fauzi", "Budi Santoso", "Citra Dewi", "Dewi Ayu", "Eko Prasetyo", "Fajar Nugroho", "Gita Permata", "Heri Susanto", "Indah Lestari", "Joko Widodo", "Kiki Amalia", "Lina Marlina", "Maya Sari", "Nina Anggraini", "Oscar Sihombing", "Putri Wahyuni", "Rina Melati", "Siti Nurhaliza", "Tono Suharto", "Yuni Kartika"]
'''

def fisher_yates_shuffle(arr):
    """
    Mengacak urutan elemen dalam daftar menggunakan algoritma Fisher-Yates.

    Parameters:
    arr (list): Daftar yang akan diacak.

    Returns:
    list: Daftar yang sudah diacak.
    """
    n = len(arr)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def bagi_kelompok(names, num_groups):
    """
    Membagi daftar nama mahasiswa menjadi beberapa kelompok.

    Parameters:
    names (list): Daftar nama mahasiswa yang akan dibagi.
    num_groups (int): Jumlah kelompok yang diinginkan.

    Returns:
    list: Daftar kelompok yang masing-masing berisi beberapa nama mahasiswa.
    """
    # Acak urutan nama mahasiswa
    shuffled_names = fisher_yates_shuffle(names)
    
    # Membuat list kosong untuk setiap kelompok
    groups = [[] for _ in range(num_groups)]
    
    # Menghitung ukuran dasar setiap kelompok dan sisa nama yang tidak bisa dibagi rata
    group_size = len(names) // num_groups
    extra = len(names) % num_groups
    
    index = 0
    for i in range(num_groups):
        # Menambahkan nama sesuai ukuran dasar setiap kelompok
        for j in range(group_size):
            groups[i].append(shuffled_names[index])
            index += 1
        # Menambahkan satu nama ekstra ke beberapa kelompok pertama jika ada sisa nama
        if extra > 0:
            groups[i].append(shuffled_names[index])
            index += 1
            extra -= 1
    
    return groups

# Contoh penggunaan
#num_groups = 9  # Misal ingin dibagi menjadi 9 kelompok

parser = argparse.ArgumentParser()
# parser.print_help()


parser.add_argument("jumlah_group",help="Tentukan Jumlah Grupnya", type=int, default=10)b
parser.add_argument("data",help="Lokasi File datanya (json)", type=str, default="data.json")

args = parser.parse_args()
num_groups = args.jumlah_group
djs = args.data

#ambil data
with open(djs,'r') as file :
    dt = json.load(file)

names = dt


kelompok = bagi_kelompok(names, num_groups)
for i, group in enumerate(kelompok):
    print(f"Kelompok {i+1}: {group}")

