
def caffeine():
    caffeine_mg = float(input())
    mg6hours = float(caffeine_mg / 2)
    mg12hours = float(mg6hours / 2)
    mg24hours = float(mg12hours / 2 /2)
    print ('After 6 hours: '+ f'{mg6hours:.2f}'+' mg')
    print ('After 12 hours: '+ f'{mg12hours:.2f}'+' mg')
    print ('After 24 hours: '+ f'{mg24hours:.2f}'+' mg')
    ''' Type your code here. '''
    
if __name__ == "__main__":
    caffeine()