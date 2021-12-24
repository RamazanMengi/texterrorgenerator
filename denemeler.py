import re
import random
from nltk.tokenize import regexp_tokenize
import secrets


with open('wordsForInserts.txt', encoding="cp437") as f:
    wordsForInserts = f.readlines()
    print(len(wordsForInserts))


with open('Output2.txt', encoding="cp437") as f:
    corpus2 = f.readlines()
    listToStr7 = ' '.join([str(elem) for elem in corpus2])

with open('test3.txt') as f:
    corpus3 = f.readlines()
    listToStr2 = ' '.join([str(elem) for elem in corpus3])

text = 'Ama Cumhurbaşkanı’na haber verilmiyor. Kime? Darbenin hedef aldığı 1 No’lu kişiye! Bu olasılık 1000 kez 0’dır. Burada sorulacak soru şudur: Fidan ve Akar, Cumhurbaşkanı ile neler konuştular? Kaç saat haberleştiler ve hangi önlemleri kararlaştırdılar? Bizi anlatılmayan  karanlık saatler  veya darbe kronolojisinde gizlenen sayfalar burasıdır. ‘Başlarını kaldırdıkları anda ezilecekler..’ Tabii bir de darbenin kaç gün önceden bilindiği de bir sorudur. Çünkü darbecilerin haberleşme uygulaması ByLock, darbeden çok önce epey çözülmüştü ve  40 bin üyenin isimleri, yerleri, telefon numaralarına varıncaya kadar  tasnif edilmişti. MİT ve siyasi iktidar yapılanmadan haberli. Bilgiler Cumhurbaşkanı’na aktarılıyordu, taa mayıs ayında! Darbeye kalkışabilecekleri de, çok daha önce; mesela Fuat Uğur ’un iki makalesinden de biliniyordu. Devlet,  Başlarını kaldırdıkları anda ezilecekler. . diyordu. Fuat Uğur’un devletten aldığı duyumların tıpkısının aynısı gerçekleşti.'

def paragraphsplitter():
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', listToStr7)
    print(len(sentences))
    return sentences

def numberOfSelectedSentences():
    # this function input the number of senteces in corpus.
    percentage1 = int(input("Enter the percentage of words to be deleted: "))
    percentage2 = int(input("Enter the percentage of words to be moved(not to be greater to make the total more than 100: "))
    percentageToBeDeleted = int(len(sentencesSplitted)*(percentage1/100))
    percentageToBeMoved = int(len(sentencesSplitted)*(percentage2/100))
    percentageToBeInserted = len(sentencesSplitted)-percentageToBeDeleted-percentageToBeMoved
    return percentageToBeDeleted, percentageToBeMoved, percentageToBeInserted


def randomlyRemovedWords():
    result3 = ""
    for n in range(NOfDelete-1):
        sentenceToWords = regexp_tokenize(sentencesSplitted[n],"(\w[\w']*\w|\w)")  # sentence to words //NOT NECESSARY IF THE SENTENCES ARE AT LINE
        if len(sentenceToWords) <=2:
            listToStr = ' '.join([str(elem) for elem in sentenceToWords])
            listToStr2 = listToStr + "."
            result2 = re.sub(r'\s([?.!"](?:\s|$))',r'\1',listToStr2)
            result3 = result3 + result2 + ''
            result4 = result3.replace('.','. ',result3.count('.')).replace(',',', ',result3.count(','))
            result5 = (re.sub(' +',' ',result4))
        else:
            sentenceToWords.remove(secrets.choice(sentenceToWords))
            print(n, "nof delete: ", NOfDelete)
            listToStr = ' '.join([str(elem) for elem in sentenceToWords])
            listToStr2 = listToStr + "."
            result2 = re.sub(r'\s([?.!"](?:\s|$))',r'\1',listToStr2)
            result3 = result3 + result2 + ''
            result4 = result3.replace('.','. ',result3.count('.')).replace(',',', ',result3.count(','))
            result5 = (re.sub(' +',' ',result4))
    return result5

    # this function ranndomly selects the number of sentences

def randomlyMovedWords():
    result = ""
    for n in range(NOfDelete+1,NOfDelete+NOfMoved):
        sentenceToWords = regexp_tokenize(sentencesSplitted[n],"(\w[\w']*\w|\w)")
        if len(sentenceToWords) <= 2:
            listToStr = ' '.join([str(elem) for elem in sentenceToWords])  # turns into string from list
            listToStr2 = listToStr + "."  # it adds dot to the end
            result = result + " " + listToStr2  # gives a space after the sentence        except IndexError:
        else:
            randomWordsToBeReplaced = random.sample(range(0,len(sentenceToWords)-1),2)
            # print('random words::   ',randomWordsToBeReplaced)
            print(n, "Nof moved words: ", NOfMoved)
            word1 = randomWordsToBeReplaced[0]
            word2 = randomWordsToBeReplaced[1]
            sentenceToWords[word1],sentenceToWords[word2] = sentenceToWords[word2],sentenceToWords[word1]  # swapping words
            listToStr = ' '.join([str(elem) for elem in sentenceToWords])  # turns into string from list
            listToStr2 = listToStr + "."  # it adds dot to the end
            result = result + " " + listToStr2  #gives a space after the sentence        except IndexError:
    return result

def wordInserter():
    result = ""
    for n in range(NOfDelete+NOfMoved+1,NOfDelete+NOfMoved+NOfInserted):
        sentenceToWords = regexp_tokenize(sentencesSplitted[n],"(\w[\w']*\w|\w)")
        if len(sentenceToWords) <= 2:
            listToStr = ' '.join([str(elem) for elem in sentenceToWords])  # turns into string from list
            theNDestroyer = listToStr.strip().replace('\n','')
            listToStr2 = theNDestroyer + "."  # it adds dot to the end
            result = result + " " + listToStr2  # gives a space after the sentence
        else:
            print(n, "Nof moved words: ", NOfInserted)
            randomWordNumberFromList = random.randint(0,len(wordsForInserts)-1)
            randomWordFromList = wordsForInserts[randomWordNumberFromList]
            numberOfRandomWords = random.randint(0,len(sentenceToWords))
            sentenceToWords.insert(numberOfRandomWords,randomWordFromList)
            listToStr = ' '.join([str(elem) for elem in sentenceToWords])  # turns into string from list
            theNDestroyer = listToStr.strip().replace('\n','')
            listToStr2 = theNDestroyer + "."  # it adds dot to the end
            result = result + " " + listToStr2  # gives a space after the sentence
    return result



sentencesSplitted = paragraphsplitter()

NOfSentences = numberOfSelectedSentences()
NOfDelete = NOfSentences[0]
NOfMoved = NOfSentences[1]
NOfInserted = NOfSentences[2]
print("Number Of Senteces: ", NOfSentences)
print('the code is here 1')
newSentecesWDeletedW = randomlyRemovedWords()
print("The Sentences With Deleted Words: ", newSentecesWDeletedW)

newSentencesWMovedW = randomlyMovedWords()
print("The Sentences With Moved Words: ", newSentencesWMovedW)
print('the code is here 2')

newsentencesWInsertedW = wordInserter()
print("New Sentences With Inserted Words: ",newsentencesWInsertedW)
print('the code is here 3')

errorfulCorpus0 = newSentecesWDeletedW+newSentencesWMovedW+newsentencesWInsertedW
errorfulCorpus = re.sub(' +', ' ', errorfulCorpus0)
print("The errorful corpus: ",errorfulCorpus)
print('the code is here 4')

with open("Output.txt", "w") as text_file:
    text_file.write(errorfulCorpus)

print("Line 1 is:  Completed")
print("Test 2: Completed")