from opencc import OpenCC
cc = OpenCC('s2twp')

with open(r'C:\cmder\vendor\conemu-maximus5\ConEmu\ConEmu.l10n', 'r', encoding = 'utf-8') as fr:
    texts = fr.readlines()
    fr.close()

texts[6] = texts[6].replace('简体中文', '繁體中文')

with open('tmp.txt','a+' , encoding = 'utf-8') as fw:
    for line in texts:
        if '"zh"' in line:
            fw.write(cc.convert(line))
        else:
            fw.write(line)
