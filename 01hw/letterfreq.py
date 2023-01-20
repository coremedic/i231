## i231 letter frequancy program ##
# fix path issues
import sys
sys.path.append("../")

from collections import Counter
import res.res as res

letters = (
    """While confined here in the Birmingham city jail, I came across your recent
statement calling my present activities “unwise and untimely.” Seldom do I
pause to answer criticism of my work and ideas. If I sought to answer all
the criticisms that cross my desk, my secretaries would have little time for
anything other than such correspondence in the course of the day, and I would
have no time for constructive work. But since I feel that you are men of
genuine good will and that your criticisms are sincerely set forth, I want to
try to answer your statement in what I hope will be patient and reasonable
terms.
Moreover, I am cognizant of the interrelatedness of all communities and states.
I cannot sit idly by in Atlanta and not be concerned about what happens in
Birmingham. Injustice anywhere is a threat to justice everywhere. We are
caught in an inescapable network of mutuality, tied in a single garment of
destiny. Whatever affects one directly, affects all indirectly. Never again can we
afford to live with the narrow, provincial “outside agitator” idea. Anyone who
lives inside the United States can never be considered an outsider anywhere
within its bounds.
You deplore the demonstrations taking place in Birmingham. But your state-
ment, I am sorry to say, fails to express a similar concern for the conditions
that brought about the demonstrations. I am sure that none of you would
want to rest content with the superficial kind of social analysis that deals
merely with effects and does not grapple with underlying causes."""
)

rep = {"[": "", "]": "", ",": "", "'": "", " ": "", ".": "", "\n": "", "\"": ""}
letters_filtered = (res.replace_all(letters, rep)).lower()

total = len(letters_filtered)

count = Counter(letters_filtered)
for l in "abcdefghijklmnopqrstuvwxyz":
    p = count[l] / total
    print(f"{l} : {count[l]}  {p:.2f}")
print(f"total {total}")