# Stack is LIFO(Last in First out)
browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

print(browsing_session.pop())
# Falsy
# 1. 0
# 2. ""
# 3. None
if not browsing_session:
    print("Disable back button")