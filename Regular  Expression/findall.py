import re
p = re.compile('[a-t]')
print(p.findall("Aye, said Mr.Gibenson stark "))
print(p.findall("aye, said Mr.Gibenson stark "))