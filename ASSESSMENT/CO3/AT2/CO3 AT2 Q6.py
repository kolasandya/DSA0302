start_vb = 0.5
book_given_vb = 0.6

start_nn = 0.5
book_given_nn = 0.4

vb_probability = start_vb * book_given_vb
nn_probability = start_nn * book_given_nn

print("P(book, VB) =", vb_probability)
print("P(book, NN) =", nn_probability)

if vb_probability > nn_probability:
    print("HMM selects: book/VB")
else:
    print("HMM selects: book/NN")
