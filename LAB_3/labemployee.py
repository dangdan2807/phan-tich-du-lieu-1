'''
Khai báo đối tượng Employee có: 
Các thuộc tính (fields, states) sau
- mã số (code)
- tên (name)
- tuổi (age)
- lương (salary)
Các phương thức (behaviors, methods)
- Tổng thu nhập hằng năm sau thuế (income) biết rằng tax = 10%
- In ra thông tin của nhân viên (display)
- Tăng lương cho nhân viên (increaseSalary), biết rằng số lương tăng phải lớn hơn 0
- (Sinh viên tự viết) Giảm lương cho nhân viên (decreaseSalary), biết rằng số lương giảm phải lớn hơn 0 và không vượt quá 20% lương hiện tại
============= YÊU CẦU CHƯƠNG TRÌNH==============
Khai báo biến danh sách (list) nhân viên (dsNhanVien) để lưu trữ các nhân viên và viết chương trình menu thực hiện các chức năng bên dưới 
- Opt-1: Tải danh sách nhân viên từ file dbemp_input.db
- Opt-2: Thêm nhân viên vào danh sách
- Opt-3: Hiển thị danh sách nhân viên
- Opt-4: Hiển thị thông tin của một nhân viên khi biết mã nhân viên
- Opt-5: Chỉnh sửa thông tin một nhân viên
- Opt-6: Xóa một nhân viên ra khỏi danh sách
- Opt-7: Tăng lương cho một nhân viên
- Opt-8: Giảm lương cho một nhân viên
- Opt-9: Tính số lượng nhân viên (countEmp) và xuất ra màn hình
- Opt-10: Tính tổng tiền lương của công ty phải trả hàng tháng (sumSalary) và xuất ra màn hình
- Opt-11: Tính trung bình lương của nhân viên (avgSalary) và xuất ra màn hình
- Opt-12: Tính độ tuổi trung bình của nhân viên (avgAge) và xuất ra màn hình
- Opt-13: Tính tuổi lớn nhất của các nhân viên (maxAge) và hiển thị danh sách nhân viên có tuổi lớn nhất
- Opt-14: Sắp xếp danh sách nhân viên tăng dần theo lương
- Opt-15: Vẽ biểu đồ tương quan lương theo độ tuổi
- Opt-16: Vẽ biểu đồ so sánh lương trung bình của các nhóm tuổi: nhỏ hơn 35, từ 35 đến 50, hơn 50 trở lên
- Opt-17: Vẽ biểu đồ thể hiện phần trăm tổng lương trên các nhóm tuổi như Opt-16
- Opt-18: Vẽ biểu đồ thể hiện phần trăm số lượng nhân viên theo các nhóm tuổi như Opt-16 
- Opt-19: Lưu danh sách nhân viên xuống file dbemp_output.db, biết rằng mỗi nhân viên là một dòng và các thông tin nhân viên được phân cách bởi dấu '-'
- Opt-Khác: Thoát chương trình
'''
import matplotlib.pyplot as plt
import numpy as np
import Employee as emp

menu_options = {
    1: 'Load data from file',
    2: 'Add new employee',
    3: 'Display list of employee',
    4: 'Show employee details',
    5: 'Update employee information',
    6: 'Delete employee',
    7: 'Increase salary of employee',
    8: 'Decrease salary of employee',
    9: 'Show total employee a month',
    10: 'Show total salary a month',
    11: 'Show average of salary a month',
    12: 'Show average of age',
    13: 'Show maximum age',
    14: 'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16: 'Draw average of salary chart by age group',
    17: 'Draw percentage of salary by age group',
    18: 'Draw percentage of total employee by age group',
    19: 'Store data to file',
    'Others': 'Exit program'
}

# Khai báo biến lưu trữ những nhân viên
dsNhanVien = []


def print_menu():
    print('------------------------')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    print('------------------------')


PATH = './LAB_3/dbemp'


def loadDataFromFile():
    fr = open(PATH + '_input.db', mode='r', encoding='utf-8')
    for line in fr:
        stripLine = line.strip('\n')
        ds = stripLine.split(',')
        maso = ds[0]
        ten = ds[1]
        tuoi = int(ds[2])
        luong = float(ds[3])
        nv = emp.Employee(maso, ten, tuoi, luong)
        dsNhanVien.append(nv)
    fr.close()


def getIndexEmployeeByMaSo(maSo):
    index = None
    i = 0
    for item in dsNhanVien:
        if (item.code == maSo):
            index = i
            break
        i += 1
    return index


while (True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Input choice: '))
    except:
        print('Invalid input, try again')
        continue
    # Check what choice was entered and act accordingly
    if userChoice == 1:
        loadDataFromFile()

    elif userChoice == 2:
        # nhập thông tin
        maSo = input("Input code: ")
        ten = input("Input name: ")
        tuoi = int(input("Input age: "))
        luong = float(input("Input salary: "))
        # tạo và thêm vào cuối danh sách
        nv = emp.Employee(maSo, ten, tuoi, luong)
        dsNhanVien.append(nv)

    elif userChoice == 3:
        for item in dsNhanVien:
            item.display()

    elif userChoice == 4:
        # nhập id
        maSo = input("Input code: ")
        # get index của nhân viên trong danh sách
        index = getIndexEmployeeByMaSo(maSo)
        if index is None:
            print("Nothing here")
        else:
            dsNhanVien[index].display()

    elif userChoice == 5:
        # nhập id
        maSo = input("Input code: ")
        # get index của nhân viên trong danh sách
        index = getIndexEmployeeByMaSo(maSo)
        # kiểm tra và cập nhật thông tin nhân viên
        if index is None:
            print("Nothing here")
        else:
            dsNhanVien[index].name = input("Input name: ")
            dsNhanVien[index].age = int(input("Input age: "))
            dsNhanVien[index].salary = float(input("Input salary: "))

    elif userChoice == 6:
        # nhập id
        maSo = input("Input code: ")
        # get index của nhân viên trong danh sách
        index = getIndexEmployeeByMaSo(maSo)
        if index is None:
            print("Nothing here")
        else:
            # xoá nhân viên tại vị trí index
            dsNhanVien.pop(index)

    elif userChoice == 7:
        # nhập id
        maSo = input("Input code: ")
        # get index của nhân viên trong danh sách
        index = getIndexEmployeeByMaSo(maSo)
        if index is None:
            print("Nothing here")
        else:
            # thêm lương của nhân viên
            amount = float(input("Input amount: "))
            dsNhanVien[index].increaseSalary(amount)

    elif userChoice == 8:
        # nhập id
        maSo = input("Input code: ")
        # get index của nhân viên trong danh sách
        index = getIndexEmployeeByMaSo(maSo)
        if index is None:
            print("Nothing here")
        else:
            # giảm lương của nhân viên
            amount = float(input("Input amount: "))
            dsNhanVien[index].decreaseSalary(amount)

    elif userChoice == 9:
        print('Number of employees:', len(dsNhanVien))

    elif userChoice == 10:
        sumSalary = 0.0
        # tính tổng lương
        for item in dsNhanVien:
            sumSalary = sumSalary + item.salary
        print(f'Total salary a month: {sumSalary:.2f}')

    elif userChoice == 11:
        length = len(dsNhanVien)
        sumSalary = 0.0
        # tính tổng lương
        for item in dsNhanVien:
            sumSalary = sumSalary + item.salary
        # tính tổng tb lương
        avgSalary = sumSalary/length

        print(f'Average of salary: {avgSalary:.2f}')

    elif userChoice == 12:
        length = len(dsNhanVien)
        sumAge = 0.0
        for item in dsNhanVien:
            sumAge = sumAge + item.age
        avgAge = sumAge/length

        print(f'Average of age: {avgAge:.2f}')

    elif userChoice == 13:
        maxAge = dsNhanVien[0].age
        for item in dsNhanVien:
            if (maxAge < item.age):
                maxAge = item.age

        print(f'Maximum age: {maxAge}')
        # for item in dsNhanVien:
        #     if (maxAge == item.age):
        #         item.display()

    elif userChoice == 14:
        length = len(dsNhanVien)
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if (dsNhanVien[i].salary > dsNhanVien[j].salary):
                    # hoán vị
                    tmp = dsNhanVien[i]
                    dsNhanVien[i] = dsNhanVien[j]
                    dsNhanVien[j] = tmp

    elif userChoice == 15:
        arrTuoi = []
        arrLuong = []
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)

        # Vẽ đồ thị
        plt.figure(figsize=(15, 5))

        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")

        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()

    elif userChoice == 16:
        arrAgeGroup = ['less than 35', 'from 35 to 50', 'more than 50']
        arrAvgSalary = [0.0, 0.0, 0.0]
        arrCount = [0.0, 0.0, 0.0]
        for item in dsNhanVien:
            if (item.age < 35):
                arrAvgSalary[0] += item.salary
                arrCount[0] += 1.0
            elif (item.age >= 35 or item.age <= 50):
                arrAvgSalary[1] += item.salary
                arrCount[1] += 1.0
            else:
                arrAvgSalary[2] += item.salary
                arrCount[2] += 1.0
        if (arrCount[0] > 0):
            arrAvgSalary[0] = arrAvgSalary[0] / arrCount[0]
        if (arrCount[1] > 0):
            arrAvgSalary[1] = arrAvgSalary[1] / arrCount[1]
        if (arrCount[2] > 0):
            arrAvgSalary[2] = arrAvgSalary[2] / arrCount[2]

        # vẽ biểu đồ
        plt.bar(arrAgeGroup, arrAvgSalary, color="green")
        plt.title('Average of salary chart age by group')
        plt.xlabel('Levels of age')
        plt.ylabel('Average of salary')
        plt.show()

    elif userChoice == 17:
        arrAgeGroup = ['less than 35', 'from 35 to 50', 'more than 50']
        arrAvgSalary = [0.0, 0.0, 0.0]
        noiBat = [0, 0.2, 0]
        length = len(dsNhanVien)
        for item in dsNhanVien:
            if (item.age < 35):
                arrAvgSalary[0] += item.salary
            elif (item.age >= 35 or item.age <= 50):
                arrAvgSalary[1] += item.salary
            else:
                arrAvgSalary[2] += item.salary
        if (arrAvgSalary[0] > 0):
            arrAvgSalary[0] = arrAvgSalary[0] / length
        if (arrAvgSalary[1] > 0):
            arrAvgSalary[1] = arrAvgSalary[1] / length
        if (arrAvgSalary[2] > 0):
            arrAvgSalary[2] = arrAvgSalary[2] / length

        # vẽ biểu đồ
        plt.figure(figsize=(10, 5))
        plt.pie(arrAvgSalary, labels=arrAgeGroup,
                explode=noiBat, shadow=True, startangle=45)
        plt.axis("equal")
        plt.legend(title='Levels of age', loc="upper right")
        plt.title('Percentage of salary by age group')
        plt.show()

    elif userChoice == 18:
        arrAgeGroup = ['less than 35', 'from 35 to 50', 'more than 50']
        arrCount = [0.0, 0.0, 0.0]
        noiBat = [0, 0.2, 0]
        length = len(dsNhanVien)
        for item in dsNhanVien:
            if (item.age < 35):
                arrCount[0] += 1
            elif (item.age >= 35 or item.age <= 50):
                arrCount[1] += 1
            else:
                arrCount[2] += 1
        if (arrCount[0] > 0):
            arrCount[0] = arrCount[0] / length
        if (arrCount[1] > 0):
            arrCount[1] = arrCount[1] / length
        if (arrCount[2] > 0):
            arrCount[2] = arrCount[2] / length

        # vẽ biểu đồ
        plt.figure(figsize=(10, 5))
        plt.pie(arrCount, labels=arrAgeGroup,
                explode=noiBat, shadow=True, startangle=45)
        plt.axis("equal")
        plt.legend(title='Levels of age', loc="upper right")
        plt.title('Percentage of total employee by age group')
        plt.show()

    elif userChoice == 19:
        fw = open(PATH + "_output.db", mode="w", encoding='utf-8')
        for item in dsNhanVien:
            fw.write(
                f'{item.code},{item.name},{item.age},{item.salary:.0f}\n')
        fw.close()
        print('Store file successfully')
    else:
        print('BYE BYE')
        break
