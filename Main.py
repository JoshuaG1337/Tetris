import time, random, os, threading
#No stackoverflow, all my homies hate stackoverflow!
def console(n, hold):
  if n == "L":
    n1 = '   []     '
    n2 = '   []     '
    n3 = '   [][]   '
    n4 = '          '
  elif n == "J":
    n1 = '     []   '
    n2 = '     []   '
    n3 = '   [][]   '
    n4 = '          '
  elif n == "S":
    n1 = '   []     '
    n2 = '   [][]   '
    n3 = '     []   '
    n4 = '          '
  elif n == "Z":
    n1 = '     []   '
    n2 = '   [][]   '
    n3 = '   []     '
    n4 = '          '
  elif n == "O":
    n1 = '          '
    n2 = '   [][]   '
    n3 = '   [][]   '
    n4 = '          '
  elif n == "I":
    n1 = '    []    '
    n2 = '    []    '
    n3 = '    []    '
    n4 = '    []    '
  else:
    n1 = '          '
    n2 = '  [][][]  '
    n3 = '    []    '
    n4 = '          '
  if hold == "L":
    h1 = '   []     '
    h2 = '   []     '
    h3 = '   [][]   '
    h4 = '          '
  elif hold == "J":
    h1 = '     []   '
    h2 = '     []   '
    h3 = '   [][]   '
    h4 = '          '
  elif hold == "S":
    h1 = '   []     '
    h2 = '   [][]   '
    h3 = '     []   '
    h4 = '          '
  elif hold == "Z":
    h1 = '     []   '
    h2 = '   [][]   '
    h3 = '   []     '
    h4 = '          '
  elif hold == "O":
    h1 = '          '
    h2 = '   [][]   '
    h3 = '   [][]   '
    h4 = '          '
  elif hold == "I":
    h1 = '    []    '
    h2 = '    []    '
    h3 = '    []    '
    h4 = '    []    '
  elif hold == "T":
    h1 = '          '
    h2 = '  [][][]  '
    h3 = '    []    '
    h4 = '          '
  else:
    h1 = '          '
    h2 = '          '
    h3 = '          '
    h4 = '          '
  return f""" __________    ______________________    __________
|   HOLD   |   |{locs[0]}{locs[1]}{locs[2]}{locs[3]}{locs[4]}{locs[5]}{locs[6]}{locs[7]}{locs[8]}{locs[9]}|   |   NEXT   |
|{h1}|   |{locs[10]}{locs[11]}{locs[12]}{locs[13]}{locs[14]}{locs[15]}{locs[16]}{locs[17]}{locs[18]}{locs[19]}|   |{n1}|
|{h2}|   |{locs[20]}{locs[21]}{locs[22]}{locs[23]}{locs[24]}{locs[25]}{locs[26]}{locs[27]}{locs[28]}{locs[29]}|   |{n2}|
|{h3}|   |{locs[30]}{locs[31]}{locs[32]}{locs[33]}{locs[34]}{locs[35]}{locs[36]}{locs[37]}{locs[38]}{locs[39]}|   |{n3}|
|{h4}|   |{locs[40]}{locs[41]}{locs[42]}{locs[43]}{locs[44]}{locs[45]}{locs[46]}{locs[47]}{locs[48]}{locs[49]}|   |{n4}|
‾‾‾‾‾‾‾‾‾‾‾‾   |{locs[50]}{locs[51]}{locs[52]}{locs[53]}{locs[54]}{locs[55]}{locs[56]}{locs[57]}{locs[58]}{locs[59]}|   ‾‾‾‾‾‾‾‾‾‾‾‾
               |{locs[60]}{locs[61]}{locs[62]}{locs[63]}{locs[64]}{locs[65]}{locs[66]}{locs[67]}{locs[68]}{locs[69]}|
               |{locs[70]}{locs[71]}{locs[72]}{locs[73]}{locs[74]}{locs[75]}{locs[76]}{locs[77]}{locs[78]}{locs[79]}|
               |{locs[80]}{locs[81]}{locs[82]}{locs[83]}{locs[84]}{locs[85]}{locs[86]}{locs[87]}{locs[88]}{locs[89]}|
               |{locs[90]}{locs[91]}{locs[92]}{locs[93]}{locs[94]}{locs[95]}{locs[96]}{locs[97]}{locs[98]}{locs[99]}|
               |{locs[100]}{locs[101]}{locs[102]}{locs[103]}{locs[104]}{locs[105]}{locs[106]}{locs[107]}{locs[108]}{locs[109]}|
               |{locs[110]}{locs[111]}{locs[112]}{locs[113]}{locs[114]}{locs[115]}{locs[116]}{locs[117]}{locs[118]}{locs[119]}|
               |{locs[120]}{locs[121]}{locs[122]}{locs[123]}{locs[124]}{locs[125]}{locs[126]}{locs[127]}{locs[128]}{locs[129]}|
               |{locs[130]}{locs[131]}{locs[132]}{locs[133]}{locs[134]}{locs[135]}{locs[136]}{locs[137]}{locs[138]}{locs[139]}|
               |{locs[140]}{locs[141]}{locs[142]}{locs[143]}{locs[144]}{locs[145]}{locs[146]}{locs[147]}{locs[148]}{locs[149]}|
               |{locs[150]}{locs[151]}{locs[152]}{locs[153]}{locs[154]}{locs[155]}{locs[156]}{locs[157]}{locs[158]}{locs[159]}|
               |{locs[160]}{locs[161]}{locs[162]}{locs[163]}{locs[164]}{locs[165]}{locs[166]}{locs[167]}{locs[168]}{locs[169]}|
               |{locs[170]}{locs[171]}{locs[172]}{locs[173]}{locs[174]}{locs[175]}{locs[176]}{locs[177]}{locs[178]}{locs[179]}|
               |{locs[180]}{locs[181]}{locs[182]}{locs[183]}{locs[184]}{locs[185]}{locs[186]}{locs[187]}{locs[188]}{locs[189]}|
               |{locs[190]}{locs[191]}{locs[192]}{locs[193]}{locs[194]}{locs[195]}{locs[196]}{locs[197]}{locs[198]}{locs[199]}|
               ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""

locs = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]

g_pl = False

def inp():
  while True:
    inp1 = str(input(": "))
    if inp1 == "a" or inp1 == "d" or inp1 == "x" or inp1 == "z" or inp1 == "c" or inp1 == " ":
      global g_pl 
      g_pl = inp1

def game(locs):
  tpool = ["L", "J", "S", "Z", "O", "I", "T"]
  type = tpool[random.randint(0,6)]
  hold = False
  pl = 4
  dir = "v"
  canhold = 0
  delay = 0.4
  while True:
    n = tpool[random.randint(0, 6)]
    while True:
      stop = False
      clear = 0
      clearrow = 0
      threading.Thread(target=inp).start()
      global g_pl
      time.sleep(delay)
      if type == "L":
        if dir == "v" and pl < 169 and locs[pl+30] != "[]" and locs[pl+31] != "[]":
          for i in range(3):
            locs[pl+i*10] = "  "
          locs[pl+21] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = ">"
            else:
              dir = "<"
        elif dir == ">" and pl < 188 and locs[pl+10] == "  " and locs[pl+11] != "[]" and locs[pl+12] != "[]":
          for i in range(3):
            locs[pl+i] = "  "
          locs[pl-8] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "^"
            else:
              dir = "v"
        elif dir == "^" and pl < 169 and locs[pl+31] != "[]" and locs[pl+10] != "[]":
          for i in range(3):
            locs[pl+1+i*10] = "  "
          locs[pl] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "<"
            else:
              dir = ">"
        elif dir == "<" and pl < 179 and locs[pl+20] != "[]" and locs[pl+11] != "[]" and locs[pl+12] != "[]":
          for i in range(3):
            locs[pl+i] = "  "
          locs[pl+10] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "v"
            else:
              dir = "^"
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          if dir == "v":
            for i in range(3):
              locs[pl+i*10] = "[]"
            locs[pl+21] = "[]"
          elif dir == ">":
            for i in range(3):
              locs[pl+i] = "[]"
            locs[pl-8] = "[]"
          elif dir == "^":
            for i in range(3):
              locs[pl+1+i*10] = "[]"
            locs[pl] = "[]"
          else:
            for i in range(3):
              locs[pl+i] = "[]"
            locs[pl+10] = "[]"
      elif type == "J":
        if dir == "v" and pl < 170 and locs[pl+30] != "[]" and locs[pl+29] != "[]":
          for i in range(3):
            locs[pl+i*10] = "  "
          locs[pl+19] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = ">"
            else:
              dir = "<"
        elif dir == ">" and pl < 177 and locs[pl+10] != "[]" and locs[pl+11] != "[]" and locs[pl+22] != "[]":
          for i in range(3):
            locs[pl+i] = "  "
          locs[pl+12] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "^"
            else:
              dir = "v"
        elif dir == "^" and pl < 169 and locs[pl+30] != "[]" and locs[pl+11] != "[]":
          for i in range(3):
            locs[pl+i*10] = "  "
          locs[pl+1] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "<"
            else:
              dir = ">"
        elif dir == "<" and pl < 179 and locs[pl+20] != "[]" and locs[pl+21] != "[]" and locs[pl+22] != "[]":
          for i in range(3):
            locs[pl+i+10] = "  "
          locs[pl] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "v"
            else:
              dir = "^"
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          if dir == "v":
            for i in range(3):
              locs[pl+i*10] = "[]"
            locs[pl+19] = "[]"
          elif dir == ">":
            for i in range(3):
              locs[pl+i] = "[]"
            locs[pl+12] = "[]"
          elif dir == "^":
            for i in range(3):
              locs[pl+i*10] = "[]"
            locs[pl+1] = "[]"
          else:
            for i in range(3):
              locs[pl+i+10] = "[]"
            locs[pl] = "[]"
      elif type == "S":
        if dir == "v" and pl < 169 and locs[pl+20] != "[]" and locs[pl+31] != "[]":
          for i in range(2):
            locs[pl+i*10] = "  "
          for i in range(2):
            locs[pl+(i+1)*10+1] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            else:
              dir = ">"
        elif dir == ">" and pl < 179 and locs[pl+11] != "[]" and locs[pl+19] != "[]":
          for i in range(2):
            locs[pl+i] = "  "
          for i in range(2):
            locs[pl+9+i] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            else:
              dir = "v"
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          if dir == "v":
            for i in range(2):
              locs[pl+i*10] = "[]"
            for i in range(2):
              locs[pl+(i+1)*10+1] = "[]"
          else:
            for i in range(2):
              locs[pl+i] = "[]"
            for i in range(2):
              locs[pl+9+i] = "[]"
      elif type == "Z":
        if dir == "v" and pl < 170 and locs[pl+20] != "[]" and locs[pl+29] != "[]":
          for i in range(2):
            locs[pl+i*10] = "  "
          for i in range(2):
            locs[pl+i*10+9] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            else:
              dir = ">"
        elif dir == ">" and pl < 178 and locs[pl+10] != "[]" and locs[pl+21] != "[]" and locs[pl+22] != "[]":
          for i in range(2):
            locs[pl+i] = "  "
          for i in range(2):
            locs[pl+11+i] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            else:
              dir = "v"
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          if dir == "v":
            for i in range(2):
              locs[pl+i*10] = "[]"
            for i in range(2):
              locs[pl+i*10+9] = "[]"
          else:
            for i in range(2):
              locs[pl+i] = "[]"
            for i in range(2):
              locs[pl+11+i] = "[]"
      elif type == "O":
        if pl < 179 and locs[pl+20] != "[]" and locs[pl+21] != "[]":
          for i in range(2):
            locs[pl+i*10] = "  "
          for i in range(2):
            locs[pl+i*10+1] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          for i in range(2):
            locs[pl+i*10] = "[]"
          for i in range(2):
            locs[pl+i*10+1] = "[]"
      elif type == "I":
        if dir == "v" and pl < 160 and locs[pl+40] != "[]":
          for i in range(4):
            locs[pl+i*10] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            else:
              dir = ">"
        elif dir == ">" and pl < 187 and locs[pl+10] != "[]" and locs[pl+11] != "[]" and locs[pl+12] != "[]" and locs[pl+13] != "[]":
          for i in range(4):
            locs[pl+i] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            else:
              dir = "v"
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          if dir == "v":
            for i in range(4):
              locs[pl+i*10] = "[]"
          else:
            for i in range(4):
              locs[pl+i] = "[]"
      else:
        if dir == "v" and pl < 179 and locs[pl+10] != "[]" and locs[pl+21] != "[]" and locs[pl+12] != "[]":
          for i in range(3):
            locs[pl+i] = "  "
          locs[pl+11] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = ">"
            else:
              dir = "<"
        elif dir == ">" and pl < 169 and locs[pl+30] != "[]" and locs[pl+21] != "[]":
          for i in range(3):
            locs[pl+i*10] = "  "
          locs[pl+11] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1            
            elif g_pl == "z":
              dir = "^"
            else:
              dir = "v"
        elif dir == "^" and pl < 179 and locs[pl+19] != "[]" and locs[pl+20] != "[]" and locs[pl+21] != "[]":
          for i in range(3):
            locs[pl+i+9] = "  "
          locs[pl] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "<"
            else:
              dir = ">"
        elif dir == "<" and pl < 169 and locs[pl+19] != "[]" and locs[pl+30] != "[]":
          for i in range(3):
            locs[pl+i*10] = "  "
          locs[pl+9] = "  "
          if g_pl != False:
            if g_pl == "a":
              pl -= 1
            elif g_pl == "d":
              pl += 1
            elif g_pl == "c" and canhold == 0:
              stop = True
              canhold = 1
            elif g_pl == "z":
              dir = "v"
            else:
              dir = "^"
        else:
          stop = True
          type = n
          pl = 4
        if stop == False:
          pl+=10
          if dir == "v":
            for i in range(3):
              locs[pl+i] = "[]"
            locs[pl+11] = "[]"
          elif dir == ">":
            for i in range(3):
              locs[pl+i*10] = "[]"
            locs[pl+11] = "[]"
          elif dir == "^":
            for i in range(3):
              locs[pl+i+9] = "[]"
            locs[pl] = "[]"
          else:
            for i in range(3):
              locs[pl+i*10] = "[]"
            locs[pl+9] = "[]"
      if (g_pl == " "):
        delay = 0;
      g_pl = False
      if stop == True:
        delay = 0.4
        for i in range(20):
          if locs[i*10:i*10+10] == ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]']:
            clear += 1
            clearrow = i
        if clear > 0:
          for i in range(clearrow-clear):
            locs[clearrow*10-i*10:clearrow*10+10-i*10] = locs[clearrow*10-(i+clear)*10:clearrow*10+10-(i+clear)*10]
        if canhold == 1:
          if hold == False:
            hold = type
            type = n
            pl = 4
            n = tpool[random.randint(0, 6)]
          else:
            hold, type = type, hold
            pl = 4
          canhold = 2
        elif canhold == 2:
          canhold = 0
          n = tpool[random.randint(0, 6)]
        n = tpool[random.randint(0, 6)]
        dir = "v"
      os.system("clear")
      print(console(n, hold))
if __name__ == "__main__":
  game(locs)
