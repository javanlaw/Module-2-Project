
SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['country']) }} as location_key,
    country
FROM {{ ref('stg_netflix') }}
WHERE country IS NOT NULL

/*
SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['COALESCE(country, \'Unknown\')']) }} as location_key,
    COALESCE(country, 'Unknown') as country
FROM {{ ref('stg_netflix') }}
*/

