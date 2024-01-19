-- index on name and score
CREATE INDEX idx_name_first ON names(name(1));
CREATE INDEX idx_name_first_score ON names(score(1));
