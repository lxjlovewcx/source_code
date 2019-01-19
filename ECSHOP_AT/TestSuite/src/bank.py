import gas;
def bank(bankID,bankcardID,gascardID,cost,month):
    result = gas.withhold(bankID, bankcardID,gascardID, cost, month)
    if(result=='数据正确'):
        return '扣款成功'  
    else:
        return result

'''
    tc1:001,goldcard001,gas001,129,4    扣款成功
    tc2:002,goldcard001,gas001,129,4    银行编号不正确
    tc3:001,goldcard002,gas001,129,4    银行卡号不正确
    tc4:……
    tc5：……
    ……
    ……
    设计以上的测试用例，依据的是设计文档中的说明，利用等价类、边界值这类
    用例设计方法设计。
'''