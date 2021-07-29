from runner import check_for_free_tickets, CASTLES, push

# Add a callback function, if free tickets available. I use PushOver (function "push") Should look like this:
"""
def notify(title, text):
    # Do something
"""

# Add your checks
check_for_free_tickets("07.08.2021", 2, CASTLES['Hohenschwangnau'], push)
check_for_free_tickets("08.08.2021", 2, CASTLES['Hohenschwangnau'], push)
check_for_free_tickets("09.08.2021", 2, CASTLES['Hohenschwangnau'], push)
check_for_free_tickets("07.08.2021", 2, CASTLES['Neuschwanstein'], push)
check_for_free_tickets("08.08.2021", 2, CASTLES['Neuschwanstein'], push)
check_for_free_tickets("09.08.2021", 2, CASTLES['Neuschwanstein'], push)

