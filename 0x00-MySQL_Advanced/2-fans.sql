-- ranks country orderd by number of fans
SELECT origin, SUM(fans) AS origin, nb_fans FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans)
