def module():
    item = {}
    for i in range(10):
        item['letter'] =  chr(70+i)
        item['num'] = 70+i
        yield item


a = module()
for i in a:
    print(i)