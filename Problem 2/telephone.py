def telephone():
    phone_number = int(input())
    phone_number1 = int(phone_number/10000000)
    phone_number2 = int((phone_number - phone_number1 * 10000000) / 10000)
    phone_number3 = phone_number % 10000
    print ('('+f'{phone_number1:.0f}'+') '+f'{phone_number2:.0f}'+'-'+ f'{phone_number3:.0f}')
    ''' Type your code here. '''
if __name__ == "__main__":
    telephone()