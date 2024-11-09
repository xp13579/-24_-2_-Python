# TODO Найдите количество книг, которое можно разместить на дискете
Vz = 1.44 * 1024**2
kol_str = 100
kol_strok = 50
kol_symb = 25

kol_symb_v_knige = kol_str * kol_strok * kol_symb

kol_koda_v_knige = kol_symb_v_knige * 4

itog = Vz // kol_koda_v_knige

print("Количество книг, помещающихся на дискету:", int(itog))