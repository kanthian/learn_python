formatter = "%r %r %r %r" #variable with raw value formatter

print formatter % (1, 2, 3, 4) #it'll output numbers with spaces
print formatter % ("one", "two", "three", "four") #words with quotes
print formatter % (True, False, False, True) #as is
print formatter % (formatter, formatter, formatter, formatter) #treat variable
#as string
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #with single quotes as string
