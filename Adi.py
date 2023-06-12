import numpy as np
import pandas as pd

"""1. Simular N variables aleatorias independientes con distribuci´on exponencial de par´ametro λ = 2 para
N = 100, 200, 400, 600, 800. Calcular los intervalos de confianza del 90%, 95% y 99% para μ con
varianza desconocida. Graficar los intervalos para cada confianza, en funci´on de N .
2. Simular 400 variables aleatorias independientes con distribuci´on exponencial de par´ametro λ = 2.
Considerando la muestra calcular el intervalo de confianza del 95% para μ asumiendo varianza de-
sconocida. Volver a hacer esta simulaci´on y este intervalo 100 veces. Para cada simulaci´on fijarse si el
verdadero valor de μ est´a o no en el intervalo, mostrar esta informaci´on con alg´un gr´afico.
3. Simular N (con N = 100, 200, 300, 400) v.a.i.i.d. con distribuci´on Poisson de par´ametro λ = 1/2. Para
cada valor de N hacer los histogramas de frecuencias relativas sabiendo que la distribuci´on es discreta
y conociendo su rango. ¿Importa el ancho de banda?
4. Simular N (con N = 100, 200, 300, 400) v.a.i.i.d. con distribuci´on Uniforme en el intervalo [2, 5]. Para
cada valor de N hacer los histogramas de probabilidad con anchos de banda 2, 1 y 0.5.
5. Simular N = 400 v.a.i.i.d. con distribuci´on normal μ = 2, σ2 = 1/2 y N v.a.i.i.d. con distribuci´on
normal μ = −1 y σ2 = 1/4. Considerar los datos que vienen de sumar lugar a lugar cada una de estas
simulaciones. De estos nuevos datos, calcular la media y la varianza muestral. Interpretar. Graficar
el histograma de probabilidad con ancho de banda 0.5, 1 y 4. ¿Qu´e observa?
6. Simular 20 variables aleatorias independientes llamadas Xi, i = 1, 2, . . . , 20 cada una con distribuci´on
normal de par´ametros μi = i y σ2 = 1
i , i = 1, 2, . . . , 20. Sean U = P20
i=1 Xi y Z = U −E(U )
√V ar(U ) . Volver a
realizar este procedimiento de manera independiente para obtener 100 muestras de la variable aleatoria
Z. Utilizando la muestra de Z graficar el histograma de probabilidad. Hint: Recordar la f´ormula para
la esperanza y la varianza de suma de normales, la cual est´a en la clase de distribuciones especiales.
7. Simular N = 200 v.a.i.i.d. una con distribuci´on normal de par´ametros μ = 2 y σ2 = 3. Usar estos datos
para calcular un intervalo de confianza de nivel 90%, 95% y 99% para la varianza. ¿Cu´al intervalo es
mas grande y cual mas chico? ¿A qu´e se debe esto?.
1"""
