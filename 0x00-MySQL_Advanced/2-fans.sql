-- ranks country orderd by number of fans
SELECT origin AS origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans)
