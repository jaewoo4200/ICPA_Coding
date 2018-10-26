freq=dict()
charDict=dict()

def addFreq(c):
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1

def makeList(s):
    for i in s:
        addFreq(i)
    lis=[]
    for i in freq:
        lis.append([freq[i],[i]])

    while len(lis)>2:
        lis.sort(key=lambda x:x[0])
        a=lis.pop(0)
        b=lis.pop(1)
        lis.append([a[0]+b[0],[a[1],b[1]]])
    return [lis[1][1],lis[0][1]]

def makeCharDict(lis,code):
    if len(lis)==1:
        charDict[lis[0]]=code
        return
    makeCharDict(lis[0],code+'0')
    makeCharDict(lis[1],code+'1')

def getChar(lis,s):
    if len(lis)==1:
        return lis[0]
    return getChar(lis[int(s[0])],s[1:])

def encode(s):
    charLis=makeList(s)
    makeCharDict(charLis,'')
    encoded=''
    for i in s:
        encoded+=charDict[i]
    return charLis,encoded

def decode(lis,encodedStr):
    nowLis=lis
    decodedStr=''
    for i in encodedStr:
        newLis=nowLis[int(i)]
        if len(newLis)==1:
            decodedStr+=newLis[0]
            nowLis=lis
        else:
            nowLis=newLis
    return decodedStr
            
        

def run():
    s=input('압축할 문자열을 입력해주세요.\n')
    charLis,encodedStr=encode(s)
    print('변환 후 :',encodedStr)
    decodedStr=decode(charLis,encodedStr)
    print('복원 후 :',decodedStr)
    if s==decodedStr:
        print('변환 전과 복원 후가 일치합니다.')
    beforeMem=len(s)*8
    afterMem=len(encodedStr)+len(str(charLis))*8
    print('압축 전 용량 : {} * 1 byte = {} * 8 bit = {} bit'.format(len(s),len(s),beforeMem))
    print('압축 후 용량 : {} * 1 bit = {} bit'.format(len(encodedStr),afterMem))
    print('압축 후 기존 용량의 %.2f%%가 되었습니다.' % ((afterMem/beforeMem)*100))

run()
