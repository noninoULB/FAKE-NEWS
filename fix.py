
fi = open("fake_real_news.csv", "r", encoding="utf-8")

string = ""

for line in fi:

	string += line

fi.close()

string = string.replace("\n","")
string = string.replace("FAKE", "FAKE\n")
string = string.replace("REAL", "REAL\n")
string = string.replace("label", "label\n")

fi2 = open("fakegen.csv", "a", encoding="utf-8")

fi2.write(string)

fi2.close()