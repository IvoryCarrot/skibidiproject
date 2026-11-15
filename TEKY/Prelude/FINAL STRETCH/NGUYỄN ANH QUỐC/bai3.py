du_lieu = input("Nhập các số: ")
ds = du_lieu.split(",")
tong = 0
so = 0
so1 = 0
int_ds = []
while so1 != len(ds):
    int_ds.append(int(ds[so1]))
    so1 += 1
while so != len(int_ds):
    tong += (int_ds[so])
    so += 1
print(f"Tổng: {tong}")
print("Lớn nhất:", max(int_ds))
int_ds.sort()
print("Danh sách tăng dần:", int_ds)