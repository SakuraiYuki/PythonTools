#在指定path路徑下，將該層檔案名稱改成流水號

import os

def batch_rename_number(path):
    num = 1
    for fname in os.listdir(path):
        new_fname = str(num)+'.txt'
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        num = num + 1


batch_rename_number(r'D:\MyProject\pythonTool\test')

