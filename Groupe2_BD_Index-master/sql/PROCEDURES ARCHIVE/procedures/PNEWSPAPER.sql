DROP PROCEDURE IF EXISTS PNEWSPAPER;
DELIMITER |
CREATE PROCEDURE PNEWSPAPER (IN VNAME_NEWSPAPER VARCHAR(50),IN VLINK_NEWSPAPER VARCHAR(255),IN VLINK_LOGO VARCHAR(255))
BEGIN
     INSERT INTO newspaper(id_newspaper,name_newspaper,link_newspaper,link_logo) VALUES (NULL,VNAME_NEWSPAPER,VLINK_NEWSPAPER,VLINK_LOGO);
END|

DELIMITER ;
CALL PNEWSPAPER("LIBERATION","HTTP liberation","http image");
