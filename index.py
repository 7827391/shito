import random
date=['石头','剪刀','布']
def play():
    print('0.石头1.剪刀2.布')
    wj=int(input('请选择:'))
    rj=random.randint(0,2)
    print('你的选择是,'+date[wj])
    print('电脑的选择是,'+date[rj])
    if wj==0 and rj==1:
     print('玩家胜利')
    elif wj==1 and rj==2:
     print('玩家胜利')
    elif wj==2 and rj==0:
     print('玩家胜利')
    if wj==0 and rj==2:
     print('电脑胜利')
    elif wj==1 and rj==0:
     print('电脑胜利')
    elif wj==2 and rj==1:
     print('电脑胜利')
    else:
      print('平局')   
play()
