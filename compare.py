import imagehash

def compare_hashes(data1, data2):
    count = 0
    for i1 in range(len(data1)):
        for i2 in range(len(data2)):
            d = data2[i2]-data1[i1]
            if (d < 100 or d > 235):
                c = 0
                while True:
                    d = data2[i2]-data1[i1]
                    if (d < 100 or d > 235):
                        c+=1
                        i1+=1
                        i2+=1
                        if (i1 >= len(data1) or i2 >= len(data2)):
                            i1 = min(i1,len(data1)-1)
                            i2 = min(i2,len(data2)-1)
                            break
                    else:
                        break
                count = max(count, c)
    
    avg_frames = (len(data1)+len(data2))/2
    percent = count / avg_frames
    return percent > 0.8