#input nilai λt dan M
lambda_t = float(input("Masukkan nilai λt: "))
M = int(input("Masukkan nilai M: "))
# Nilai e yang diberikan soal
e = 2.71828
#tampilkan perulangan untuk n = 0 hingga M
for n in range (M + 1) :
    #hitung faktorial
    faktorial = 1
    for i in range (1, n + 1):
         faktorial *= i

#hitung (P(N(t) = n)
    p_n = (e**(-lambda_t)* (lambda_t**n)) / faktorial  
#hasil
    print(f"(P(N(t) ={n} )= {p_n}")