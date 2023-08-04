helicoptero,policial,fugitivo,direcao = map(int,input().split())

while fugitivo != helicoptero:
    fugitivo += direcao
    if fugitivo < 0:
        fugitivo = 15
    if fugitivo > 15:
        fugitivo = 0
    if policial == fugitivo:
        break
if fugitivo == policial:
    print("n")
else:
    print("s")
