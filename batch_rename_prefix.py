#在指定path路徑下，將該層檔案及資料夾名稱前加上prefix字串

import os

def batch_rename(path, prefix):
    for fname in os.listdir(path):
        new_fname = prefix+fname
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))

batch_rename(r'D:\MyProject\pythonTool\test','bug')
