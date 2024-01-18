-- ranks country orderd by number of fans
SELECT origin AS origin, SUM(fans) AS nb_fans FROM metal_bands
ORDER BY origin, nb_fans DESC;
