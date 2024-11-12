SELECT * FROM db_juego.juego;

-- Consulta 1: Juegos en el top 10
SELECT nombre_juego
FROM juego
WHERE ranking_juego <= 10;

-- Consulta 2: Juegos con más de 30.5 unidades vendidas
SELECT nombre_juego
FROM juego
WHERE total_distribuido > 30.5;

-- consulta extra: Juegos con mas de 9 en critica
SELECT nombre_juego, puntaje_critica, total_distribuido, año_juego
FROM juego
WHERE puntaje_critica >= 9;

-- Joins 1
SELECT nombre_juego, nombre_desarrollador
FROM Juego 
JOIN Desarrollador ON desarrollador_juego = id_desarrollador;

-- joins 2
SELECT nombre_juego, nombre_plataforma,nombre_editor
FROM Juego 
JOIN Plataforma ON plataforma_juego = id_plataforma
JOIN editor ON editor_juego = id_editor
WHERE puntaje_critica > 8;

-- joins extras: mostrar datos de juegos superiores a 9 en critica
SELECT ranking_juego, nombre_juego, puntaje_critica, puntaje_usuario, total_distribuido, año_juego, nombre_plataforma,nombre_editor, nombre_desarrollador
FROM juego 
JOIN desarrollador ON desarrollador_juego = ID_desarrollador
JOIN Plataforma ON plataforma_juego = id_plataforma
JOIN editor ON editor_juego = id_editor
WHERE puntaje_critica >= 9
