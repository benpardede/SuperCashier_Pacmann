# **Super Cashier Program**

### **Bernart Marihot Pardede, Analytics and Data Science Batch 14**

# 1. **Latar Belakang Masalah**

Seorang pemilik salah satu supermarket besar di salah satu kota di Indonesia yang membutuhkan sistem kasir yang dapat self-service di supermarket miliknya. Customer yang datang bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur lainnya. Pemilik tersebut membutuhkan programmer untuk membuatkan fitur-fitur tersebut agar bisa menerapkan sistem self-service di supermarket miliknya.

# 2. **Objective & Requirement**

Goals yang ingin di capai pada projek ini adalah membuat Super Cashier Program untuk memberikan self-experience kepada customer untuk bisa bebas dalam menentukan barang, jumlah, dan harga yang ingin dibeli, sehingga requirements yang dibutuhkan adalah sebagai berikut : 

a. Fitur untuk membuat ID Transaksi sebagai user dan keranjang untuk menampilkan daftar belanjaan

b. Fitur untuk menambah item yang ingin dibeli oleh user

c. Fitur untuk menggani nama barang yang ada ke dalam keranjang

d. Fitur untuk mengganti jumlah barang yang ada ke dalam keranjang

e. Fitur untuk mengganti jumlah barang yang ada di dalam keranjang

f. Fitur untuk mengganti harga barang yang ada di dalam keranjang

g. Fitur untuk menghapus item belanjaan di dalam keranjang

h. Fitur untuk menampilkan total belanjaan dan nominal yang perlu dibayarkan


# 3. **Alur Program**

![Super Cashier Flow](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/3ecf4092-ee22-4b56-ac42-c1ac3ae1fcb5)

# 4. **Penjelasan Code**

Adapun fitur-fitur atau fungsi yang dapat dijalankan pada program ini adalah :

- [x] Class Transaction()

  Merupakan inisiasi untuk membuat keranjang belanjaan yang digunakan oleh customer.
![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/fe235032-6697-4fe5-a5a1-aed7730269aa)

- [x] def Add_item(self)

  Merupakan fungsi yang digunakan untuk menambah barang ke dalam keranjang.
![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/4a453f11-f365-491d-a81c-ea4a7924ebfe)


- [x] def update_item(self)

  Merupakan fungsi yang digunakan untuk mengganti nama barang yang ada di dalam keranjang.
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/46b0c031-8715-49d3-b3df-a2bd7c90d5dd)

- [x] def update_qty(self)

  Merupakan fungsi yang digunakan untuk mengganti jumlah barang yang ada di dalam keranjang.
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/57d4da7a-4cb2-4571-a236-93608936dc6d)

- [x] def update_price(self)

  Merupakan fungsi yang digunakan untuk mengganti harga barang yang ada di dalam keranjang.
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/9fcf74e0-f053-4f57-8e88-5ecd26cda1cc)

- [x] def delete_item(self)

  Merupakan fungsi yang digunakan untuk menghapus barang yang ada di dalam keranjang.
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/1ce182e4-a8dc-494f-96a0-c0f6c614c713)

- [x] def reset_keranjang(self)

  Merupakan fungsi yang digunakan untuk menghapus semua barang yang ada di dalam keranjang.
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/4e4aabfc-ec21-4f19-873d-39dc85f14830)

- [x] def check_order(self)

  Merupakan fungsi yang digunakan untuk melakukan pemeriksaan barang apakah daftar belanja sudah sesuai atau belum.
![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/70793a0d-1c47-4d27-83f3-93f457d0dc26)

- [x] def total_price(self)

  Merupakan fungsi yang digunakan untuk memperlihatkan daftar belanjaan serta total harga yang harus dibayarkan.
![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/d02b929d-b6e7-46b3-8d6b-0177cb49f27a)



# 5. **TEST CASE SUPER CASHIER**

- [x] Membuat Object Transactions
      
![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/468ea0d2-6c8f-4e01-abee-c708ca205f44)

### **Test 1 :**

  Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut :
      - Nama Item : Ayam Goreng, Qty : 2, Harga : 20000
      - Nama Item : Pasta Gigi, Qty : 3. Harga : 15000

  **Output :** 

![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/7c9caf70-db43-4e0a-8d0f-9512badb3759)

### **Test 2 :**

  Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan
  method delete_item() untuk menghapus item. item yang dihapuskan adalah **Pasta Gigi.**:
  
  **Output :**  
  
![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/ad998db4-5f8b-4cd1-860c-5f787ea107ee)

### **Test 3 :**

  Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! 
  Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_keranjang() untuk menghapus semua
  item yang sudah ditambahkan:
  
  **Output :**  
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/9ae467e9-18c3-4111-93ea-ebb490c4570e)

### **Test 4 :**

  Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli. 
  
  **Output :**  
  ![image](https://github.com/benpardede/SuperCashier_Pacmann/assets/67301642/2dd81782-f53f-44ec-81a9-6ec74bd070a8)
