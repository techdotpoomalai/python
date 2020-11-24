def filter(ref,temp,index):
    sets=""
    for d in range(0,len(temp)):
        if d==index:
            sets +=temp[d]
        else:                  
            if ref== temp[d].upper or ref==temp[d].lower or ref==temp[d]:
                continue
            else:
                sets +=temp[d]
    return(sets) 

# string="Hi this is Hudron welcome !"
string="welwcomel"
for c in range(0,len(string)):
    text=string
    text=filter(text[c],text,c)
    if string==text:
        break
    else:
        string=text
        print(text)
    
    # l-=1
