## i231 letter frequancy program ##
# fix path issues
import sys
sys.path.append("../")

from collections import Counter
import res.res as res

letters = (
    """Fru luyhna snkxyn exqieqfkeg egu kt wkmjefuhg ql uduha ygjuwf kt nqtu myoug elvuhg-
fylvqls fru xurqlv-fru-gwhuulg fuwrlknksa yf klwu uyga fk qslkhu ylv vqttqwenf fk
elvuhgfylv. Ql fru myql, qt fru vugofkj, nyjfkj, fyxnuf, kh mkxqnu vudqwu vkug cryf cu
ubjuwf qf fk vk, cu sqdu nqffnu frkesrf fk fru xqfg ylv xafug fryf gwehha xurqlv fru gwhuul
fk myou qf kjuhyfu. Kl fru kwwygqkl fryf cu tqlv kehgundug wklfumjnyfqls cryf mysqw
myoug frugu vudqwug gk qlwhuvqxna jkcuhten, cu, kt luwuggqfa, mufyjrkhqwynna frhkc
keh rylvg ej ql ubwnymyfqkl fryf fruhu qg pegf fkk mewr fuwrlknksa whymmuv qlfk keh
unuwfhklqwg tkh yla klu juhgkl fk shygj."""
)

rep = {"[": "", "]": "", ",": "", "'": "", " ": "", ".": "", "\n": "", "\"": ""}
letters_filtered = (res.replace_all(letters, rep)).lower()

total = len(letters_filtered)

count = Counter(letters_filtered)
for l in "abcdefghijklmnopqrstuvwxyz":
    p = count[l] / total
    print(f"{l} : {count[l]}  {p:.2f}")
print(f"total {total}")