alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']

key = [22, 0, 11, 13, 20, 19]

text = """the nearly global ubiquitous use of computers in every aspect of life makes understanding the behind the screens technology at once easy to ignore and difficult to understand in the main if the desktop laptop tablet or mobile device does what we expect it to do we give little thought to the bits and bytes that scurry behind the screen to make it operate on the occasion that we find ourselves contemplating what magic makes these devices so incredibly powerful we of necessity metaphorically throw
""".lower()

output = ""

keyPos = 0

for character in text:
    space = True
    for i in range(0, len(alphabet), 1):
        if alphabet[i] == character:
            space = False
            swap = i + key[keyPos]
            if swap > len(alphabet) - 1:
                swap = swap - len(alphabet)
            output = output + alphabet[swap]
            keyPos = keyPos + 1
            if (keyPos + 1) > len(key):
                keyPos = 0
    if space == True:
        output = output + " "
        
print(output)