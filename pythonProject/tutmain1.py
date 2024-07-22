



def add(a,b):
    return a + b + 5

o=add(6,4)
print(o)
# we are coping the functions from tutmain1 to tutmain 2 from using import function



if __name__ == '__main__':         # this functions is not imported in tutmain 2 bcz of main function
    def god(c,d):        # this function will work on tutmain 1 only if we imoport the avove function of add will
                          # import not this one
        return c-d
    h=god(7,6)
    print(h)