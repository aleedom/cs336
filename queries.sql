SELECT l.Drinker,count(s.beer) 
FROM BarBeerDrinker.likes as l ,BarBeerDrinker.sells as s 
WHERE s.bar='Caravan' and s.beer=l.beer 
group by l.Drinker 
having count(l.beer) = (SELECT Count(*) FROM BarBeerDrinker.sells where sells.bar='Caravan')