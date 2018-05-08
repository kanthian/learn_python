x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x #binary?
print y #i do

print "I said: %r." % x
print "I said: %s." % x
print "I also said: '%s'." % y
print "I also said: '%r'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
joke_evaluation2 = "Isn't that joke so funny?! %d"

print joke_evaluation % hilarious
print joke_evaluation2 % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
