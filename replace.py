from opencc import OpenCC
import os
cc = OpenCC('s2twp')
path = input('ConEmu/Cmder Language Path: ')+'\\'
with open(path + 'ConEmu.l10n', 'r', encoding = 'utf-8') as fr:
    texts = fr.readlines()
    fr.close()

os.rename(path+'ConEmu.l10n',path+'ConEmu-BK.l10n')

texts[6] = texts[6].replace('简体中文', '繁體中文')

with open(path+'ConEmu.l10n','a+' , encoding = 'utf-8') as fw:
    for line in texts:
        if '"zh"' in line:
            fw.write(cc.convert(line))
        else:
            fw.write(line)
