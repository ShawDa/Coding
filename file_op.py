# -*- coding:utf-8 -*-
# some file operation functions

import pickle
import xlwt
import xlrd
import scipy.io as scio


def save2txt(save, txt):
    # 将得到的结果保存在一个txt文件中,save:要保存的结果,如一个list或者dict;txt:保存的路径及文件名
    f1 = open(txt, "wb")
    pickle.dump(save, f1)
    f1.close()
    return 'save pickle done!'


def txt2save(txt):
    # 将保存的结果读取并返回
    f2 = open(txt, "rb")
    return_list = pickle.load(f2)
    f2.close()
    return return_list


def write_txt(some_list, txt):
    # 将某个list写入txt文件
    with open(txt, "w") as f:
        for info in some_list:
            f.write(str(info) + '\n')
        f.close()
    return 'write txt done!'


def read_txt(txt):
    # 读取txt内容,返回一个包含每行数据的list
    return_list = []
    for line in open(txt, 'r'):
        line = line.strip()
        return_list.append(line)
    return return_list


def write_excel(some_dict, xls):
    # 将一个dict信息写入excel中
    wb = xlwt.Workbook()
    ws = wb.add_sheet('one sheet')
    n = 0
    for k, v in some_dict.items():
        ws.write(n, 0, k)
        ws.write(n, 1, v)
        n += 1
    wb.save(xls)
    return 'write excel done!'


def read_excel(xls, sheet):
    # 读取excel中的信息,返回所有行数-列数-值的三元组list
    data = xlrd.open_workbook(xls)
    table = data.sheet_by_name(sheet)
    rows = table.nrows  # 行数
    cols = table.ncols  # 列数
    return_list = []
    for i in range(rows):
        for j in range(cols):
            # print(i, j, table.cell(i, j).value)
            return_list.append((i, j, table.cell(i, j).value))
    return return_list


def read_mat(mat_path):
    # 读取一个.mat文件,返回一个dict
    data = scio.loadmat(mat_path)
    return data


if __name__ == '__main__':
    # test_dict = {'a':3, 'b':2, 'c':1}
    # write_excel(test_dict, 'data/example.xls')
    # print(read_excel('data/example.xls', 'one sheet'))

    # test_list = ['How are you?', 'Fine! Thank you, and you?', 'Fine, too!']
    # write_txt(test_list, 'data/example.txt')
    # print(read_txt('data/example.txt'))

    data = read_mat('/data1/Pose_Estimation&Keypoint/lsp_dataset/joints.mat')
    array = data['joints']
    print(array.shape)
    import numpy as np
    np.save('/data1/Pose_Estimation&Keypoint/lsp_dataset/joints.npy', array)
    data = np.load('/data1/Pose_Estimation&Keypoint/lsp_dataset/joints.npy')
    print(data)
    pass
