from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from collections import Counter
import itertools
import wikipedia

#BUILD the corpuses

#User definition - meaning 1
corpus1 = "A user is a person who uses a computer or network service. Users generally use a system or a software product without the technical expertise required to fully understand it. Power users use advanced features of programs, though they are not necessarily capable of computer programming and system administration. A user often has a user account and is identified to the system by a username (or user name). Other terms for username include login name, screenname (or screen name), nickname (or nick) and handle, which is derived from the identical Citizen's Band radio term. Some software products provide services to other systems and have no direct end users."

#Accountancy - meaning 2
corpus2 = "An account (in book-keeping) refers to assets, liabilities, income, expenses, and equity, as represented by individual ledger pages, to which changes in value are chronologically recorded with debit and credit entries. These entries, referred to as postings, become part of a book of final entry or ledger. Examples of common financial accounts are sales, accounts receivable, mortgages, loans, PP&E, common stock, sales, services, wages, and payroll. A chart of accounts provides a listing of all financial accounts used by particular business, organization, or government agency. The system of recording, verifying, and reporting such information is called accounting. Practitioners of accounting are called accountants. A personal account is an account for use by an individual for that person's own needs. It is a relative term to differentiate them from those accounts for corporate or business use. The term personal account may be used generically for financial accounts at banks and for service accounts such as accounts with the phone company, or even for e-mail accounts. A deposit account is a savings account, current account or any other type of bank account that allows money to be deposited and withdrawn by the account holder. These transactions are recorded on the bank's books, and the resulting balance is recorded as a liability for the bank and represents the amount owed by the bank to the customer. Some banks may charge a fee for this service, while others may pay the customer interest on the funds deposited."

#Tokenize corpuses
token1 = word_tokenize(corpus1.lower())
token2 = word_tokenize(corpus2.lower())

#Build bigrams
bigrams1 = ngrams(token1, 2)
bigrams2 = ngrams(token2, 2)

#Build frequency profile
fp1 = Counter(bigrams1)
fp2 = Counter(bigrams2)

#Construct models
model1 = [(i, fp1[i]) for i in fp1]
model2 = [(j, fp2[j]) for j in fp2]

"""for i in model2:
    print("\t".join( (str(i[1]), i[0][0], i[0][1], "account2" )))

for i in model1:
    print("\t".join( (str(i[1]), i[0][0], i[0][1], "account1" )))"""

#TEST corpora
test1 = "A user account is a location on a network server used to store a computer username, password, and other information. A user account allows or does not allow a user to connect to a network, another computer, or other share. Any network that has multiple users requires user accounts. A good example of a user account is an Internet or your e-mail account."
test2 = "What should I do if my bank account is hacked? If you notice any strange or unusual activity on your bank statement, notify your bank immediately. Don’t worry about cyber attacks, banks are well protected. There are constant attacks on banks via the Internet. Almost everyday, a bank will be susceptible to hackers. That’s where the money is so people naturally go after it. A threat of a cyber attack should not be a reason to deter from using a financial institution despite there being multiple reasons in doing so. Here’s how to find out if you’ve been hacked and how you can regain control of your bank account. How will you know if you’ve been hacked? trange purchases that appear on your bank statement may be the first clue that a hacker has infiltrated your account. Always read credit card and bank statements. Allow some time to comprehend what each line means and whether or not your remember completing that transaction. Sometimes the people that steal your card will make seemingly insignificant purchases to test and see if your card works before going to larger transactions. Depending on your bank, they will notify you of suspicious activity and automatically cancel fraudulent charges and then give you a new card. Lost or stolen card numbers. Don’t wait for your bank to realise. It's your account, so you're in charge of managing it. Check it regularly in order to avoid a mishap. The first step the bank will take is freezing your account so no-one can access your account. If you go to your local bank branch, they will give you a temporary card, otherwise it will be sent to you in the mail. Most banks will refund your lost money after you complete a form admitting that you didn't take part in the theft. Despite that, here are several reasons why you shouldn't worry about hackers and what to do if it does happen to you: Banks are liable If a hacker steals any funds from a bank, the bank is liable to pay the money back to the customer. The customer will never lose money. In the event of a cyber attack, the hacker would try to use customer computers and take out a fraction of funds in order to avoid detection. If lots of computers did this, it would add up to a lot of stolen cash. Banks are improving security Since banks are constantly under attack, they need to improve every aspect of their security so they have the latest software designed to protect you and your money. Every attack doesn’t make the news, but generally the big ones do. Banks are constantly improving their systems for detecting and dealing with these problems. Ensure your account is not vulnerable Most banking websites allow you to activate a feature called remember your password when you log in via the Internet. You can then skip several layers of security the next time you log in since the bank recognises your computer’s IPv4 address - a unique identifier for each Internet connection. Malware is a tool that hackers use to imitate your IPv4 address so they can gain access to your bank account. Often you don't even know that they have control over your bank account. It’s best to disable the “remember your computer” feature. Make sure that you take precautions when banking online."

#Tokenize corpuses
tokentest1 = word_tokenize(test1.lower())
tokentest2 = word_tokenize(test2.lower())

#Build bigrams
bigramstest1 = ngrams(tokentest1, 2)
bigramstest2 = ngrams(tokentest2, 2)

#Build frequency profile
fptest1 = Counter(bigramstest1)
fptest2 = Counter(bigramstest2)

#Construct models
modeltest1 = [(i, fptest1[i]) for i in fptest1]
modeltest2 = [(j, fptest2[j]) for j in fptest2]

for i in modeltest1:
    print("\t".join( (str(i[1]), i[0][0], i[0][1], "account1")))

for j in modeltest2:
    print("\t".join((str(j[1]), j[0][0], j[0][1], "account2")))