Для внесения изменений в BD использовались запросы:

from task1.models import Buyer, Game

Buyer.objects.create(name='Vlad', balance='30000', age='34')
Buyer.objects.create(name='Anatoly', balance='20000', age='44') 
Buyer.objects.create(name='Roman', balance='2000', age='12')

Game.objects.create(title='Atomic Heart', cost='3000', size='26.3', description='Russian game', age_limited='1') 
Game.objects.create(title='Cyberpunk 2077', cost='3500', size='35', description='Game of the year', age_limited='1')
Game.objects.create(title='Cuphead', cost='2000', size='12', description='Mind-blowing game', age_limited='0') 

Game.objects.get(id=1).buyer.set(('1', '2'))       
Game.objects.get(id=2).buyer.set(('1'))      
Game.objects.get(id=3).buyer.set(('1', '3'))
