ESC_CHAR='*'
def encode(s):
    cnt = 1
    prev = ''
    encodedLis=[]
    for ch in s+'\0':
        if ch!=prev or cnt==254:
            if cnt==1:
                encodedLis.append(prev)
                if prev==ESC_CHAR:
                    encodedLis.append(prev)
            else:
                if prev==ESC_CHAR:
                    for i in range(cnt*2):
                        encodedLis.append(ESC_CHAR)
                else:
                    if cnt==2:
                        encodedLis.append(prev)
                        encodedLis.append(prev)
                    else:
                        encodedLis.append(ESC_CHAR)
                        encodedLis.append(prev)
                        encodedLis.append(cnt)
            prev=ch
            cnt=1
        else:
            cnt+=1
    encodedLis.pop(0)
    return encodedLis
def decode(s):
    pass

def run():
    s=input('압축할 문자열을 입력하세요.\n')
    encodedLis=encode(s)
    encodedStr=''
    for i in encodedLis:
        if type(i)==str:
            encodedStr+=i
        else:
            encodedStr+=str(i)
    print('압축 후 :',encodedStr)
    decodedStr=decode(encodedLis)
    print('복원 후 :',decodedStr)
    if s==decodedStr:
        print('압축 전과 복원 후가 일치합니다.')
    print('압축 전 용량 : {} * 1 byte = {} byte'.format(len(s),len(s)))
    print('압축 후 용량 : {} * 1 byte = {} byte'.format(len(encodedLis),len(encodedLis)))
    print('압축 후 기존 용량의 %.2f%%가 되었습니다.' % ((len(encodedLis)/len(s))*100))
run()
