import os

import torch


def mkdir(path):#创建文件夹
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def show_cuda_imformation():#显示cuda的一些信息
    print("CUDA是否可用: {}".format(torch.cuda.is_available()))  # 查看CUDA是否可用
    print("可用的CUDA数量: {}".format(torch.cuda.device_count()))  # 查看可用的CUDA数量
    print("CUDA的版本号: {}".format(torch.version.cuda))  # 查看CUDA的版本号

show_cuda_imformation()