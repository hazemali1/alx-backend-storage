-- ranks country orderd by number of fans
SELECT origin AS origin, fans AS nb_fans FROM metal_bands
ORDER BY SUM(fans) DESC;
