print(*[[x,chr((ord(x)-52)%26+65),chr((ord(x)-84)%26+97)][(64<ord(x)<123)+(96<ord(x)<123)] for x in input()],sep='')