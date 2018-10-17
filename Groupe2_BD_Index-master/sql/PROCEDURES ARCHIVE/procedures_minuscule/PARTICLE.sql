DROP PROCEDURE IF EXISTS particle/
	CREATE PROCEDURE particle (IN vdate_publication DATE, IN vrate_positivity FLOAT,
	IN vrate_negativity FLOAT, IN vrate_joy FLOAT, IN vrate_fear FLOAT, IN vrate_sadness FLOAT,
	IN vrate_angry FLOAT, IN vrate_surprise FLOAT, IN vrate_disgust FLOAT, IN vid_newspaper INT, OUT vid_article INT)

BEGIN

	INSERT INTO article (id_article, date_publication, rate_positivity, rate_negativity, rate_joy, 
	rate_fear, rate_sadness, rate_angry, rate_surprise, rate_disgust, id_newspaper) 
	VALUES (NULL,vdate_publication,vrate_positivity,vrate_negativity,vrate_joy,vrate_fear,
	vrate_sadness,vrate_angry,vrate_surprise,vrate_disgust,vid_newspaper);
	SELECT LAST_INSERT_ID() INTO vid_article;

END/       

CALL particle("2017-12-31",0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,1,@vid_article)/
SELECT @vid_article/
