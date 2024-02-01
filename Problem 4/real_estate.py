
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    change_price = float(current_price - last_month_price)
    mortgage = float((current_price * 0.051) / 12)
    print ('This house is $'+f'{current_price:.0f}'+'. The change is $'+f'{change_price:.0f}'+' since last month.')
    print ('The estimated monthly mortgage is $'+f'{mortgage:.2f}'+'.')
    # Your code goes here
if __name__ == "__main__":
    real_estate()