#membuat contoh list
hari = ["senin","selasa","rabu","kamis"]

#menampilkan list dengan perulangan
for i in hari :
	print(i)

i = 0
while i < len(hari) :
	print(i)
	i += 1

#mengupdate salah satu list
hari [2] = "minggu"
print (hari)

#menghapus salah satu list
hari.pop()
print (hari)
del hari [1 : 3]
print (hari)
hari.remove ("senin")

#menambahkan list
hari. append ("senin")
print (hari)

hari.extend (["selasa","sabtu"])
print (hari)

hari.insert (3,"minggu")
print (hari)