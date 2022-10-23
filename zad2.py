import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('practice_lab_1.xlsx') # czytanie z pliku
dataNumpy = np.array(data) # tablica numpy pliku
columnsNames = list(data.columns) # nazwy kolumn kolumna 1', 'kolumna 2',...
rows = data.values # wartosci kolumn

"""
Zadanie 1.2. Indeksowanie zaawansowane tablic numpy
Pobierz ze strony plik z danymi wejściowymi dane_w_ekselu.xlsx.
Wczytaj dane z pliku do zmiennej typu pandas DataFrame.
Pobierz ze zmiennej DataFrame wartości jako dwuwymiarową tablicę numpy oraz nazwy kolumn jako listę.
Wykonaj poniższe zadania korzystają z konstrukcji wektorowych biblioteki numpy.

"""

"""
1. Znajdź tablicę dwuwymiarową, która będzie wynikiem różnicy dwóch tablic:
pierwsza będzie zawierała wszystkie kolumny oraz parzyste wiersze tablicy danych wejściowych,
druga – wszystkie kolumny i nieparzyste wiersze tablicy danych wejściowych.
Numeracja wierszy oraz kolumn zaczyna się od 0!
"""

#[w,k]
# ::2 - parzyste
# 1::2 - nieparzyste

arr1 = rows[::2,:] - rows[1::2,:]
#print(arr1)

"""
2. Przekształć dane w sposób następujący: od każdej wartości odejmij średnią obliczoną dla całej tablicy,
oraz podziel przez odchylenie standardowe wyznaczone dla całej tablicy.
Podpowiedź: skorzystaj z metod mean oraz std.
"""

arr2 = (rows - rows.mean()) / rows.std()
#print(arr2)

"""
3. Wykonaj zadanie z podpunktu 2 dla oddzielnych kolumn pierwotnej tablicy,
czyli wyznaczając średnią oraz odchylenie standardowe dla oddzielnych kolumn.
Podpowiedź: aby uniknąć dzielenia przez zero do arr.std(axis=0)
dodaj wynik funkcji np.spacing(arr.std(axis=0)).
"""

arr3 = (rows - rows.mean(axis=0)) / (rows.std(axis=0) + np.spacing(rows.std(axis=0)))
#print(arr2)

"""
4. Dla każdej kolumny pierwotnej tablicy policz współczynnik zmienności,
definiowany jako stosunek średniej do odchylenia standardowego,
zabezpiecz się przed dzieleniem przez 0 podobnie do poprzedniego punktu.
"""

arr4 = rows.mean(axis=0) / rows.std(axis=0) + np.spacing(rows.std(axis=0))
#print(arr4)

"""
5. Znajdź kolumnę o największym współczynniku zmienności.
"""

arr5 = np.argmax(arr4)
#print(arr5)

"""
6. Dla każdej kolumny pierwotnej tablicy policz liczbę elementów o wartości większej, niż średnia tej kolumny.
"""

arr6 = (rows > rows.mean(axis=0)).sum(axis=0)
#print(arr6)

"""
7. Znajdź nazwy kolumn w których znajduje się wartość maksymalna.
Podpowiedź: listę stringów można również przekształcić na tablicę numpy,
po czym można będzie dla niej zastosować maskę.
"""

maxRowValue = rows.max()
maxColumnValue = rows.max(axis=0)
columnsNames = np.array(columnsNames)
arr7 = columnsNames[maxColumnValue == maxRowValue]
#print(arr7)

"""
8. Znajdź nazwy kolumn w których jest najwięcej elementów o wartości 0.
Podpowiedź: wartości w tablicy wartości logicznych można sumować,
zakładając, że zawiera ona liczby całkowite, rzutowanie będzie wykonane automatycznie.
"""

mask = ((rows==0).sum(axis=0)).argmax()
arr8 = columnsNames[mask]
#print(arr8)

"""
9. Znajdź nazwy kolumn w których suma elementów na pozycjach parzystych jest większa od sumy elementów na pozycjach nieparzystych.
Wyświetl ich nazwy, postaraj się nie korzystać z pętli.
"""

mask = rows[::2,:].sum(axis=0) > rows[1::2,:].sum(axis=0)
arr9 = columnsNames[mask]
print(arr9)