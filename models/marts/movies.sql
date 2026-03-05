/* 
#1
SELECT *
FROM {{ ref('stg_netflix') }}
WHERE type = 'Movie'
*/

WITH stg AS (
    SELECT * FROM {{ ref('stg_netflix') }}
    WHERE type = 'Movie'
) 

SELECT
    stg.show_id,
    stg.title,
    {{ dbt_utils.generate_surrogate_key(['stg.director']) }} as director_key,
    {{ dbt_utils.generate_surrogate_key(['stg.country']) }} as location_key,
    stg.release_year,
    stg.date_added,
    stg.rating
FROM stg

/*
#3
WITH stg AS (
    SELECT * FROM {{ ref('stg_netflix') }}
    WHERE type = 'Movie'
)

SELECT
    show_id,
    title,
    -- We must generate the director_key here using the same logic as the dimension
    {{ dbt_utils.generate_surrogate_key(['COALESCE(director, \'Unknown\')']) }} as director_key,
    {{ dbt_utils.generate_surrogate_key(['COALESCE(country, \'Unknown\')']) }} as location_key,
    release_year,
    date_added,
    rating
FROM stg
*/
