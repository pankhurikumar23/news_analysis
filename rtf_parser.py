import pickle
import os, glob

source_list = ['The Economic Times', 'The Hindu', 'Indian Express', 'Hindustan Times', 'The Times of India']
economic_times = []
hindu = []
express = []
hindustan_time = []
toi = []
count = [0, 0, 0, 0, 0, 0]

path = os.getcwd()
for filename in glob.glob("data/TripleTalaq/*.txt"):
    file = open(filename, "r", encoding="utf8", errors='ignore')
    contents = file.read()
    articles = contents.split("\n\n\n\n")
    count[5] += len(articles)
    print(filename + " " + str(len(articles)))

    for i in range(len(articles)):
        item = articles[i]
        if source_list[0] in item:
            count[0] += 1
            economic_times.append(item)
        elif source_list[1] in item:
            count[1] += 1
            hindu.append(item)
        elif source_list[2] in item:
            count[2] += 1
            express.append(item)
        elif source_list[3] in item:
            count[3] += 1
            hindustan_time.append(item)
        elif source_list[4] in item:
            count[4] += 1
            toi.append(item)
        # else:
        #     print(item)
        #     print("======================================================")

print(count)
outfile = open("data/TripleTalaq/EconomicTimes", 'wb')
pickle.dump(economic_times, outfile)
outfile.close()

outfile = open("data/TripleTalaq/Hindu", 'wb')
pickle.dump(hindu, outfile)
outfile.close()

outfile = open("data/TripleTalaq/IndianExpress", 'wb')
pickle.dump(express, outfile)
outfile.close()

outfile = open("data/TripleTalaq/HindustanTimes", 'wb')
pickle.dump(hindustan_time, outfile)
outfile.close()

outfile = open("data/TripleTalaq/TimesOfIndia", 'wb')
pickle.dump(toi, outfile)
outfile.close()

