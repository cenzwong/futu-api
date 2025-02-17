# from futu import *

# quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # 创建行情对象
# print(quote_ctx.get_market_state('US.LIST20883'))  # 获取港股 HK.00700 的快照数据
# quote_ctx.close() # 关闭对象，防止连接条数用尽

# from futu import *
# quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

# ret, data = quote_ctx.get_plate_list(Market.US, Plate.CONCEPT)
# if ret == RET_OK:
#     print(data)
#     print(data['plate_name'][0])    # 取第一条的板块名称
#     print(data['plate_name'].values.tolist())   # 转为 list
# else:
#     print('error:', data)
# quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽


from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_plate_stock('US.LIST20883')
if ret == RET_OK:
    print(data)
    print(data['stock_name'][0])    # 取第一条的股票名称
    print(data['stock_name'].values.tolist())   # 转为 list
else:
    print('error:', data)
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
