import requests
import re
header = {
    'cookie': 't=6745edc5e3a67fd923483141eb5d55b7; cna=dv4vFBNrFiACAd2wgab+NwRP; thw=cn; tg=0; enc=aGfeiIPdNLBuNm7qRlH%2B0jAr%2FRVAosbRZs2%2FBGEUdCqjqzAPg1XPhPsHKGZzNMnO%2B%2FD3YgHkw7g5Hfza2PnGtw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=212253601265562838; ucn=unsz; _tb_token_=bNzdXJnB7lA96TdXE2Gt; cookie2=13af0046265d1bceb73a437e01d6de1e; _m_h5_tk=005b24a3683a02bc06c8e4d6fa3e89b6_1546870730212; _m_h5_tk_enc=be017fadde2e5825aae282d5c46ee217; munb=3412930255; v=0; unb=3412930255; sg=%E5%AD%905a; _l_g_=Ug%3D%3D; skt=5fdb08770d3d816d; cookie1=BdKGgV5Aldb4YiMKsKb%2BE59nunSauz1nt%2BXItglXSWI%3D; csg=d4b43812; uc3=vt3=F8dByRIpaYogCizIZ0k%3D&id2=UNQ2kslvVuaYSg%3D%3D&nk2=tqGxS%2F7BJ6dbpf2WvhRupT8%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU0NjkyNDI0MA%3D%3D; tracknick=%5Cu77BB%5Cu5F7C%5Cu6DC7%5Cu5965_%5Cu6709%5Cu532A%5Cu541B%5Cu5B50; lgc=%5Cu77BB%5Cu5F7C%5Cu6DC7%5Cu5965_%5Cu6709%5Cu532A%5Cu541B%5Cu5B50; _cc_=Vq8l%2BKCLiw%3D%3D; dnk=%5Cu77BB%5Cu5F7C%5Cu6DC7%5Cu5965_%5Cu6709%5Cu532A%5Cu541B%5Cu5B50; _nk_=%5Cu77BB%5Cu5F7C%5Cu6DC7%5Cu5965_%5Cu6709%5Cu532A%5Cu541B%5Cu5B50; cookie17=UNQ2kslvVuaYSg%3D%3D; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=W5iHLLyFe3xm&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTYMDKfRzU87A%3D%3D&tag=8&lng=zh_CN; mt=ci=23_1; whl=-1%260%260%261546925771929; isg=BAkJY9OLsYzhNkrmSV6XVKvVGDWj_v3ib6_Ei6t-kPAv8ikE86aMWPRjMRZhqpXA; l=aBv4FD55ysIvxfsXkMa5zV6pR707y8ZPeJZX1MakDTEhNPeS7RXy1T-o-VwW7_qC5BJguK-5F',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
url = 'https://buyertrade.taobao.com/trade/itemlist/asyncBought.htm?action=itemlist/BoughtQueryAction&event_submit_do_query=1&_input_charset=utf8'
url2 = 'https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z02.1.a2109.d1000368.41d6782dCI5Vdb&nekot=1470211439694'
num = [i for i in range(1,16)]
print(num)
data = {
    'pageNum': 2,
    'pageSize': 15,
    'prePageNo': 1,
}
response = requests.get('https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z02.1.a2109.d1000368.41d6782dCI5Vdb&nekot=1470211439694')
print(response.text)