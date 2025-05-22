curso01 = int(input("Digite quantos acessos teve curso01: "))
curso02 = int(input("Digite quantos acessos teve curso02: "))
                     
if curso01 == curso02:
    print("empate")
elif curso01 > curso02:
    print("curso01 é maior")
else:
    print("curso02 é maior")