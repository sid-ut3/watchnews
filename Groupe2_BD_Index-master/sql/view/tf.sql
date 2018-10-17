SELECT id_article, mot, COUNT(*) AS compte
FROM (
	SELECT
		a.id_article,
		m.mot
	FROM
		article a,
		position_mot pm,
		mot_racine m
	WHERE
		a.id_article = pm.id_article AND
		pm.id_racine = m.id_racine
) occurrences 
GROUP BY occurrences.id_article, occurrences.mot
