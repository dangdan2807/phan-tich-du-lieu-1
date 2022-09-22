'''
(*) Sinh viên tự thực hành
Viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
Others- Thoát
'''

import Rectangle as rect

menu_options = {
    1: 'Đọc dữ liệu từ file input.db',
    2: 'Thêm mới hình chữ nhật',
    3: 'Hiển thị danh sách hình chữ nhật',
    4: 'Lưu danh sách hình chữ nhật xuống file demo4output.db',
    'Others': 'Thoát chương trình'
}


def print_menu():
    print('\n----------------------')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


dsHCN = []

while (True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng, hãy nhập lại.....')
        continue

    # Check what choice was entered and act accordingly
    if userChoice == 1:
        fr = open('./codehcn_sv/input.db', mode='r', encoding='utf-8')
        print('Đang đọc dữ liệu ...')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cr, cd)
            dsHCN.append(hcn)
        fr.close()
        print('Đã đọc dữ liệu xong')
    elif userChoice == 2:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dài: '))
        hcn = rect.Rectangle(cr, cd)
        dsHCN.append(hcn)
    elif userChoice == 3:
        for item in dsHCN:
            item.display()
    elif userChoice == 4:
        print('Đang ghi vào file demo4output.db')
        fw = open("./codehcn_sv/demo4output.db", mode="w", encoding='utf-8')
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close()
        print('Đã ghi file xong')
    else:
        print('Thoát chương trình BYE BYE')
        break
