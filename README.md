# Are there any free tickets at Neuschwanstein or Hohenschwangnau?
I would like to visit Neuschwanstein Castle. But the castle does not want. Tickets are almost no more because of the pandemic. Or maybe there are?  
This scraper checks regularly if there are free tickets available and sends me a push notification to my smartphone.

## Installation
Create virtual env and install requirements  
`pip install -r requirements.txt`

## Configuration
### Add Timeslot
Open `src/main.py` and call the function `check_for_free_tickets`  
```python
check_for_free_tickets("08.10.2021", 2, CASTLES['Hohenschwangnau'], notify)
```
Parameters:
* `date`: Date of your visit
* `quantity`: How many tickets?
* `casle`: Which castle? Use `CASTLES['Neuschwanstein']` or `CASTLES['Hohenschwangnau']`
* `callback`: Add a Callback Function to get a notification

### Add Callback function
Create in `src/main.py` a callback function. It should look like this one:
```python
def notify(title, text):
    print(title)
    print(text)
```
In this function you can send you an e-mail, a slack notification or what else. I use [Pushover](https://pushover.net/). If you d'like to use it too, add the callback function `push`:  
```python
check_for_free_tickets("08.10.2021", 2, CASTLES['Hohenschwangnau'], push)
```
**Important**: You need to add your credentials to `.env` (have a look at the template `.env_template`)