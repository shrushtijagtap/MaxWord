#word={}
file = open("text.txt", 'r')
for line in file:
    line_w=line.lower().split(" ")
    word={}
    for w in line_w:
        if w in word.keys():
            word[w]=word[w]+1
        else:
            word[w]=1
    maxkey=max(word, key=word.get) #for finding max occured word in every line
    print(maxkey, word[maxkey]) #for printing max occured word in every line


#for max occured word in whole file
#maxkey=max(word, key=word.get)
#print(maxkey, word[maxkey])