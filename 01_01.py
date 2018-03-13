if __name__ == '__main__':
    while True:
        print('\t1:+\n\t2:-\n\t3:*\n\t4:/\n\t0:Exit\n')
        choice = input('\tEnter choice:')
        if choice == '0':
            break
        op = {'1':'+','2':'-','3':'*','4':'/'}
        print()
        op1 = input('\tEnter first operand:')
        op2 = input('\tEnter second operand:')
        try:
            print('\t%.1f %s %.1f = %.1f\n' % (float(op1),op[choice],float(op2),float(eval(op1+op[choice]+op2))))
        except ZeroDivisionError:
            print('\tdivision by zero')
        except:
            print('\tunknown error')
                
