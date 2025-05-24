querys_sql={
    "top_rated_query": """
        SELECT m.title, m.vote_average, m.popularity, m.release_date
        FROM movie m
        ORDER BY m.vote_average DESC
;
        """,
    "genre_popularity_query":"""
    SELECT g.genre_name, m.title, m.popularity, m.vote_average
        FROM movie m
        JOIN movie_genres mg ON m.movie_id = mg.movie_id
        JOIN genre g ON mg.genre_id = g.genre_id
        ORDER BY g.genre_name, m.popularity DESC
;
        """,

    "country_rating_query":"""
        SELECT c.country_name, AVG(m.vote_average) as avg_rating, COUNT(m.movie_id) as movie_count
        FROM movie m
        JOIN production_country pc ON m.movie_id = pc.movie_id
        JOIN country c ON pc.country_id = c.country_id
        GROUP BY c.country_name
        HAVING movie_count > 5
        ORDER BY avg_rating DESC
;
    """,
    "movie_characters_with_actors":"""
    SELECT 
    m.title AS movie_title,
    mc.character_name,
    p.person_name AS actor_name
    FROM 
        movie_cast mc
    JOIN movie m ON mc.movie_id = m.movie_id
    JOIN person p ON mc.person_id = p.person_id;
    
""",
    "movie_production_companies":"""
    SELECT 
    m.title AS movie_title,
    pc.company_name
    FROM 
        movie_company mc
    JOIN movie m ON mc.movie_id = m.movie_id
    JOIN production_company pc ON mc.company_id = pc.company_id;
""",

    "most_expensive_movies":"""
        SELECT 
            title,
            budget
        FROM 
            movie
        ORDER BY 
            budget DESC
;
        
""",
    "available_languages_by_movie":"""
    SELECT 
        m.title AS movie_title,
        l.language_name,
        lr.language_role
    FROM 
        movie_languages ml
    JOIN movie m ON ml.movie_id = m.movie_id
    JOIN language l ON ml.language_id = l.language_id
    JOIN language_role lr ON ml.language_role_id = lr.role_id;
""",
}

