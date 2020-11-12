#[1 1 2 3 5 8 13 ...]

fibo=[0,1]
s=0 #s=sayaç

while len(fibo)<30:
    a=fibo[s]+fibo[s+1]
    fibo.append(a)
    s += 1

print(*fibo,sep=" ")
  
    
