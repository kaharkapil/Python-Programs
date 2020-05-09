import os,fnmatch



def filesrch(pattern,path):
    result=[]
    for root,dirs,files in os.walk(path):
         for name in files:
              if fnmatch.fnmatch(name,pattern):
                  result.append(os.path.join(root,name))
    
    print('\n',result)
#filesrch('*.txt','C:/Users/user/Desktop/Python Programs')
#filesrch('*.txt','G:/')  
     
     
