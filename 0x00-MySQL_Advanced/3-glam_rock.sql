-- old bands
SELECT band_name AS band_name, COALESCE(split, 2022) - formed AS lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
