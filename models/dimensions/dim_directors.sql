
SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['director']) }} as director_key,
    director as director_name
FROM {{ ref('stg_netflix') }}
WHERE director IS NOT NULL


/*
SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['COALESCE(director, \'Unknown\')']) }} as director_key,
    COALESCE(director, 'Unknown') as director_name
FROM {{ ref('stg_netflix') }}
*/