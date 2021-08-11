class FileOperation:

    def __init__(self, filename, operation):
        try:
            file=open(filename.replace(',','.'),'r+')
            self.file=file
            self.operation=operation
        except Exception as e:
            print(str(e))
            input()
        
        
    def result(self):
        
        Filelines=self.file
        operation=self.operation
        file1=open("positive.txt","w")
        file2=open("negative.txt","w")
        for line in Filelines:
            
            
            if line !='\n' and line !='':
                num1 = int( line.split(' ')[0])
                num2 = int( line.split(' ')[1])

                if (operation == "*"):
                    res = num1 * num2
                    resOp=str(num1) + " * (" + str(num2) + ") = " + str(res)
                    if (res < 0):
                        file2.write(resOp + "\n")
                    else:
                        file1.write(resOp + "\n")
                        
                elif (operation == "/"):
                    if (num2 == 0):
                        file2.write(str(num1) + " / (" + str(num2) + ") = " + " can't divide by zero"+"\n")
                    else:
                        res = num1 / num2
                        resOp=str(num1) + " / (" + str(num2) + ") = " + str(res)
                        if (res < 0):
                            file2.write(resOp + "\n")
                        else:
                            file1.write(resOp + "\n")
                            
                elif (operation == "+"):
                    res = num1 + num2
                    resOp=str(num1) + " + (" + str(num2) + ") = " + str(res)
                    if (res < 0):
                        file2.write(resOp + "\n")
                    else:
                        file1.write(resOp + "\n")
                        
                elif (operation == "-"):
                    res = num1 - num2
                    resOp=str(num1) + " - (" + str(num2) + ") = " + str(res)
                    if (res < 0):
                        file2.write(resOp + "\n")
                    else:
                        file1.write(resOp + "\n")

                        

        
filename  = input("Filename  ( input.txt ):  ")
operation = input("Operation  ( + , - , * , / ):  ")
FileOperation1=FileOperation(filename,operation)
FileOperation1.result()























            
