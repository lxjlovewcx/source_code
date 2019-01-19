## 扣费(String 银行编号,String 银行卡号,String 煤气卡号,double 费用,int 扣款月份);
def withhold(bankID,bankcardID,gascardID,cost,month):
    if(bankID=='001'):
        if(bankcardID=='goldcard001'):
            if(gascardID=='gas001'):
                if(cost>=0):
                    if(month>=1 and month<=12):
                        return '数据正确'
                    else:
                        return '扣款月份不正确'
                else:
                    return '扣款金额不正确'
            else:
                return '煤气卡号不正确'
        else:
            return '银行卡号不正确'
    else:
        return "银行编号不正确"

