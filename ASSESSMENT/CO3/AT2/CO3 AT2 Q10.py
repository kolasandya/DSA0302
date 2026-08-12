words = ["economic", "growth", "increases", "employment"]

initial = ["JJ", "NN", "NNS", "NN"]
correct = ["JJ", "NN", "VBZ", "NN"]

print("Word\tInitial\tCorrect")
for i in range(len(words)):
    print(words[i], "\t", initial[i], "\t", correct[i])
