# f = open("myfile.txt","r")
# print(f.read())
# print(f.readline())
# print(f.readline())
# f.close()

# with open("myfile.txt","r") as f:
#         print(f.read(2))
        
# with open("myfile.txt","r") as f:
#         for x in f:
#             print(x)
            
# with open("myfile.txt","a") as f:
#     f.write("\nThank you")
    
# with open("myfile.txt") as f:
#         print(f.read())
        
# with open("myfile.txt","w") as f:
#     f.write("Ajay --- IGNORE ---")
    
# with open("myfile.txt") as f:
#         print(f.read())
        
# f = open("myfile.txt","x")

import os
# os.remove("myfile.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist")