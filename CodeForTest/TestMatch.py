import re,os

keytoparameter={"sum":"{-s num $<2-n> |-M num $<2-n>|-m num num |-d num num}"}
TypeToReg={'int':'-？\d*.','ip_10':'\d+\.\d+\.\d+\.\d+','string':'[A-za-z0-9]+'}
pattern_ip=re.compile(TypeToReg['ip_10'])
pattern1=re.compile(r"(-s )((-?\d*.){2,8})|(-M )((-?\d*.){2,8})|(-m )((-?\d*.){2})|(-d )((-?\d*.){2})")
pattern2=re.compile(r"((-s) (-?\d*.){2,5}|(-M) (-?\d*.){2,5}|(-m) (-?\d*.) (-?\d*.)|(-d) (-?\d*.) (-?\d*.))")

#print(str)

while(1):
    Input=input("请输入命令\n")
    m=pattern2.match(Input)
    '''if m:
        com="sum.exe "+ Input
        os.system(com)
    '''
    print(m)





