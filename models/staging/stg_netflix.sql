/*
#1
SELECT DISTINCT
    show_id,
    type,
    title,
    director,
    country,
    date_added,
    release_year,
    rating
FROM {{ source('raw', 'netflix_titles') }}

#2
WITH source AS (
    SELECT * FROM {{ source('raw', 'netflix_titles') }}
),
deduped AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY show_id ORDER BY date_added DESC) as row_num
    FROM source
)
SELECT * EXCEPT(row_num)
FROM deduped
WHERE row_num = 1
*/

-- models/staging/stg_netflix.sql
SELECT * FROM {{ source('raw', 'netflix_titles') }}
WHERE director IS NOT NULL 
  AND country IS NOT NULL