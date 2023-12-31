# -*- coding: utf-8 -*-
"""main.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QaTpMkumi8LC-8gnImlZ_oloKJh_u5QC
"""

class Transaction:
  def __init__(self):
    """
    Membuat class Transaction untuk menyimpan metode seperti penambahan barang, jumlah barang, hingga total barang.
    langkah awal adalah dengan melakukan inisialisasi atribut keranjang,
    sebagai wadah untuk menyimpan barang yang ingin dibeli
    """
    self.keranjang = dict()

  def add_item(self):
      """
      Adalah fungsi untuk melakukan penambahan barang yang ingin dibeli ke dalam atribut keranjang
      """
      try :
         ulang = int(input('Mau beli berapa Barang ? '))
         for i in range(ulang):
          item_name = input("Masukkan nama barang: ").lower()
          item_qty = int(input("Masukkan jumlah produk: "))
          item_price = int(input("Masukkan harga produk: "))
          self.keranjang.update({item_name : [item_qty, item_price]})
         return f'Item yang dibeli adalah {self.keranjang}'
      except ValueError:
        print('Inputan salah, masukkan dengan angka')

  def update_item(self):
    """
    Adalah fungsi untuk mengganti nama Item jika ingin diadakannya perubahan.
    """
    try :
      item_name = input("Masukkan nama barang yang ingin diubah : ").lower()
      if item_name in self.keranjang :
        new_item = input("Masukkan nama barang baru : ").lower()
        self.keranjang[new_item] = self.keranjang.pop(item_name)
      else:
        print(f"{item_name} tidak ada dalam daftar")
    except Exception as e :
      print(e)

  def update_qty(self):
    """
    Adalah fungsi untuk mengganti jumlah barang jika ingin diadakannya perubahan.
    """
    try :
      item_name = input("Masukkan nama barang yang ingin diubah : ").lower()
      if item_name in self.keranjang :
        new_qty = int(input("Masukkan jumlah produk: "))
        self.keranjang[item_name][0] = new_qty
      else :
          print(f'{item_name} tidak ada dalam daftar')
    except ValueError:
        print('Inputan salah, masukkan dengan angka')

  def update_price(self):
    """
    Adalah fungsi untuk mengganti harga barang jika ingin diadakannya perubahan.
    """
    item_name = input("Masukkan nama barang yang ingin diubah : ").lower()
    if item_name in self.keranjang :
      new_price = int(input("Masukkan harga produk: "))
      self.keranjang[item_name][1] = new_price
    else :
      print(f'{item_name} tidak ada dalam daftar')

  def delete_item(self):
    """
    Adalah fungsi untuk menghapus barang.
    """
    item_name = input("Masukkan nama barang yang ingin diubah : ").lower()
    if item_name in self.keranjang :
      self.keranjang.pop(item_name)
    else :
      print(f'{item_name} tidak ada dalam daftar')
    return f'{self.keranjang}'

  def reset_keranjang(self):
    """
    Adalah fungsi untuk menghapu semua daftar barang belanjaan.
    """
    self.keranjang = {}
    return f'Belanjaan anda telah kosong'

  def check_order(self):
    """
    Adalah fungsi untuk memastikan barang belanjaan sudah benar.
    """
    try :
      for key, value in self.keranjang.items():
        item_name = key
        item_qty = value[0]
        item_price = value[1]

      if type(item_name) == str and type(item_qty) == int and type(item_price) == int:
        print("Pemesananan sudah benar")
      else:
        print("Terdapat kesalahan input data/pesanan")
    except Exception as e :
      print(e)

  def total_price(self):
     self.total_price = 0
     for value in self.keranjang.values():
          item_qty = value[0]
          item_price = value[1]
          self.total_price += (item_qty * item_price)

     if self.total_price >= 200_000 :
      print(f'Item yang dibeli adalah {self.keranjang}.\nAnda mendapatkan diskon 5%, total yang harus anda bayarkan adalah sebesar Rp. {self.total_price - (self.total_price*0.05)}')
     elif self.total_price >= 300_000 :
      print(f'Item yang dibeli adalah {self.keranjang}.\nAnda mendapatkan diskon 8%, total yang harus anda bayarkan adalah sebesar Rp. {self.total_price - (self.total_price*0.08)}')
     elif self.total_price >= 500_000 :
          print(f'Item yang dibeli adalah {self.keranjang}.\nAnda mendapatkan diskon 10%, total yang harus anda bayarkan adalah sebesar Rp. {self.total_price - (self.total_price*0.1)}')
     else :
      print(f'total yang harus anda bayar adalah sebesar Rp. {self.total_price}')
