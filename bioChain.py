"""Раскодирует геномную последовательность состоящую из букв и цифр."""
def bio_chain(chain):
    """На входе код из символов и цифр."""
    summ, count, k = list(), str(), str()
    for i in range(len(chain)):
        if chain[i].isalpha():
            k = chain[i]
        else:
            continue
        for j in range(i+1, len(chain)):
            if chain[j].isdigit():
                count += chain[j]
            elif chain[j].isalpha():
                break
        summ.append(k * int(count))
        count = str()

    print(*summ, sep='')

n = input('Введите цепочку ''\n')
bio_chain(n)
