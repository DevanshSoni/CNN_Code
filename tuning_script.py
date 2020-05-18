#!/usr/bin/env python
# coding: utf-8

# In[9]:


# import os
import re


# In[10]:


file=open("/model_files/Pneumonia Detection using CNN .py")
content=file.read()


# In[11]:


lines = content.split("\n")


# In[12]:


ep=0
kernel_1=0
kernel_2=0
pool_size_1=0
pool_size_2=0


# In[14]:


epoch="epochs=*\d{1,3}"
pattern2=r"filters=*\d{1,3}"
pattern3=r"kernel_size=\(\d{1,3},\d{1,3}\)"
pattern4=r"pool_size=\(\d{1,3},\d{1,3}\)"

ep=0
kernel_1=0
kernel_2=0
pool_size_1=0
pool_size_2=0
check=0

index=0
layers = []
count=0
for i in range(len(lines)):
    if 'model.add(Convolution2D(' in lines[i] and 'model.add(MaxPooling2D(' in lines[i+1]:
        print(lines[i])
        print(lines[i+1])
        layers.extend([lines[i],lines[i+1]])
        count+=1
        index=i+2
print("Count is ",count)
layers=[layers[-2],layers[-1]]
if count < 3:
    print("Added One CRP Layer")
    print("Now total number of CRP Layers is ",count+1)
    lines.insert(index,layers[0])
    lines.insert(index+1,layers[1])
elif count ==3:
    for i in range(len(lines)):
        if 'model.add(Convolution2D(' in lines[i]:
            kernel_size=lines[i].index('kernel_size')
            filters=re.findall(pattern2,lines[i])
            kernel=re.findall(pattern3,lines[i])
            temp_line=lines[i]
            if len(filters)>0:
                new_filter=int(filters[0].split("=")[-1])+5
            if len(kernel)>0:
                a=kernel[0].split("=")[-1]
                b=a.split(",")
                kernel_1=int(b[0].split('(')[1])+2
                kernel_2=int(b[1].split(')')[0])+2
            
            if check > 0:
                lines[i]="model.add(Convolution2D(filters={},kernel_size=({},{}),activation='relu'))".format(new_filter,kernel_1,kernel_2)
            
            check+=1
        elif 'model.add(MaxPooling2D(' in lines[i]:
            pool_size=lines[i].index('pool_size')
            result4=re.findall(pattern4,lines[i])
            if len(result4)>0:
                a=result4[0].split("=")[-1]
                b=a.split(",")
                pool_size_1=str(int(b[0].split('(')[1])+2)
                pool_size_2=str(int(b[1].split(')')[0])+2)
            lines[i] = "model.add(MaxPooling2D(pool_size=({},{})))".format(pool_size_1,pool_size_2)
            
        elif 'epochs' in lines[i]:
            result=re.findall(epoch,lines[i])
            if len(result)>0:
                ep=int(result[0].split("=")[-1])+5
            lines[i]="epochs={},".format(ep)  
                
print("Insert CRP layer at Index {} if Number of CRP Layers are less than 3".format(index))
print("Layers ",layers)
file.close()


# In[15]:


for line in lines:
    print(line)


# In[ ]:





# In[16]:


content=""
for new_line in lines:
    content=content+new_line+"\n"
file=open("/model_files/Pneumonia Detection using CNN .py","w")
file.write(content)
file.close()

# os.system("cd /model_files/ && git add . && git commit -m 'Hyper Parameters Tunned' && git push")
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




