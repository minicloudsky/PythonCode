#!/usr/bin/env python
# coding=utf-8
import os

class ScanFile:
    base_dir = '/'
    path_list = []
    file_list = []
    ignore_dirs = []
    
    def __init__(self,base_dir,ignore_dirs):
        self.base_dir = base_dir
        self.ignore_dirs = ignore_dirs

    # scan dir
    def list_dir(self, path):
        if os.path.isdir(path):
            dirs = os.listdir(path)
            for dir in dirs:
                if dir in self.ignore_dirs:
                    continue
                sub_path = path + '/' + dir
                #sub_path = dir
                if os.path.isdir(sub_path):
                    self.path_list.append(sub_path)
                    self.list_dir(sub_path)
                if os.path.isfile(sub_path):
                     self.file_list.append(path+'/'+dir)
                    #self.file_list.append(sub_path)
    def get_path_list(self):
        self.list_dir(self.base_dir)
        return self.path_list

    def get_file_list(self):
        self.list_dir(self.base_dir)
        return self.file_list


if __name__ == '__main__':
    path = '/usr/local/docker-nginx'
    ignore_dirs = ['黑马python2017就业班','node_modules','log']
    file = ScanFile(path,ignore_dirs)
    path_list = file.get_path_list()
    file_list = file.get_file_list()
    print(path_list)
    # print(file_list)
